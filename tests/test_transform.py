import unittest
from utils.transform import (
    clean_price, clean_rating, clean_colors, transform_data
)

class TestTransformData(unittest.TestCase):
    """
    Unit test untuk fungsi-fungsi dalam modul transform.py.
    """

    def test_clean_price_valid(self):
        """Test clean_price() dengan input valid dolar."""
        self.assertEqual(clean_price("$10"), 160000.0)
        self.assertEqual(clean_price("$0"), 0.0)

    def test_clean_price_invalid(self):
        """Test clean_price() dengan input non-dolar atau tidak valid."""
        self.assertIsNone(clean_price("100"))
        self.assertIsNone(clean_price("Free"))
        self.assertIsNone(clean_price(""))

    def test_clean_rating_valid(self):
        """Test clean_rating() untuk input rating valid."""
        self.assertEqual(clean_rating("4.5"), 4.5)
        self.assertEqual(clean_rating("3"), 3.0)

    def test_clean_rating_invalid(self):
        """Test clean_rating() untuk input rating tidak valid."""
        self.assertIsNone(clean_rating("Invalid Rating"))
        self.assertIsNone(clean_rating("Not Rated"))
        self.assertIsNone(clean_rating(""))

    def test_clean_colors(self):
        """Test clean_colors() untuk ekstraksi angka dari string warna."""
        self.assertEqual(clean_colors("3 Colors"), 3)
        self.assertEqual(clean_colors("Red, Blue, Green"), 0)
        self.assertEqual(clean_colors("2"), 2)
        self.assertEqual(clean_colors(""), 0)

    def test_transform_data_success(self):
        """Test transform_data() pada data valid dan lengkap."""
        raw_data = [
            {
                "Title": "Shirt 1",
                "Price": "$20",
                "Rating": "4.5",
                "Colors": "3 Colors",
                "Size": "M",
                "Gender": "Unisex",
                "Timestamp": "2024-04-05T12:00:00"
            }
        ]
        result = transform_data(raw_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["Price"], 320000.0)
        self.assertEqual(result[0]["Rating"], 4.5)
        self.assertEqual(result[0]["Colors"], 3)

    def test_transform_data_invalid_values(self):
        """Test transform_data() untuk baris dengan nilai tidak valid."""
        raw_data = [
            {"Title": "Unknown Product", "Price": "$10", "Rating": "4", "Colors": "1", "Size": "M", "Gender": "Unisex"},
            {"Title": "Shirt", "Price": "Price Unavailable", "Rating": "4", "Colors": "1", "Size": "M", "Gender": "Unisex"},
            {"Title": "Shirt", "Price": "$10", "Rating": "Invalid Rating", "Colors": "1", "Size": "M", "Gender": "Unisex"},
        ]
        result = transform_data(raw_data)
        self.assertEqual(result, [])

    def test_transform_data_duplicate_removal(self):
        """Test transform_data() untuk menghapus data duplikat berdasarkan key unik."""
        raw_data = [
            {
                "Title": "Product A",
                "Price": "$10",
                "Rating": "5",
                "Colors": "2 Colors",
                "Size": "L",
                "Gender": "Male",
                "Timestamp": "2024-04-05T12:00:00"
            },
            {
                "Title": "Product A",
                "Price": "$10",
                "Rating": "5",
                "Colors": "2 Colors",
                "Size": "L",
                "Gender": "Male",
                "Timestamp": "2024-04-05T12:01:00"
            }
        ]
        result = transform_data(raw_data)
        self.assertEqual(len(result), 1)