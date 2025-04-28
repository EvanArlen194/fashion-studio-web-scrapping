import unittest
from unittest.mock import patch, MagicMock
from utils.load import load_to_csv, load_to_google_sheets, load_to_postgresql

sample_data = [
    {
        "Title": "Shirt A",
        "Price": 160000.0,
        "Rating": 4.5,
        "Colors": 3,
        "Size": "M",
        "Gender": "Unisex",
        "Timestamp": "2024-04-05T12:00:00"
    }
]


class TestLoad(unittest.TestCase):
    @patch("utils.load.pd.DataFrame.to_csv")
    def test_load_to_csv_success(self, mock_to_csv):
        """Test load_to_csv berhasil menyimpan file CSV tanpa error."""
        load_to_csv(sample_data, filename="test.csv")
        mock_to_csv.assert_called_once()

    @patch("utils.load.pd.DataFrame.to_csv", side_effect=Exception("File error"))
    def test_load_to_csv_error(self, mock_to_csv):
        """Test load_to_csv menangani error saat menyimpan file CSV."""
        load_to_csv(sample_data)
        mock_to_csv.assert_called_once()

    @patch("utils.load.service_account.Credentials.from_service_account_file")
    @patch("utils.load.build")
    def test_load_to_google_sheets_success(self, mock_build, mock_creds):
        """Test load_to_google_sheets berhasil update Google Sheets."""
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        mock_service.spreadsheets.return_value.values.return_value.update.return_value.execute.return_value = {
            "updatedCells": 7
        }

        load_to_google_sheets(sample_data)
        mock_build.assert_called_once()
        mock_service.spreadsheets.return_value.values.return_value.update.return_value.execute.assert_called_once()

    @patch("utils.load.build", side_effect=Exception("Google Sheets Error"))
    def test_load_to_google_sheets_error(self, mock_build):
        """Test load_to_google_sheets menangani error dari API Google."""
        load_to_google_sheets(sample_data)
        mock_build.assert_called_once()

    @patch("utils.load.create_engine")
    def test_load_to_postgresql_success(self, mock_engine):
        """Test load_to_postgresql menyimpan data ke DB tanpa error."""
        mock_conn = MagicMock()
        mock_engine.return_value.begin.return_value.__enter__.return_value = mock_conn

        load_to_postgresql(sample_data)
        mock_engine.assert_called_once()

    @patch("utils.load.create_engine", side_effect=Exception("DB error"))
    def test_load_to_postgresql_error(self, mock_engine):
        """Test load_to_postgresql menangani error koneksi database."""
        load_to_postgresql(sample_data)
        mock_engine.assert_called_once()