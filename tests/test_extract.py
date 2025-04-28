import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from utils.extract import get_page_url, parse_product, scrape_page, extract_data

class TestExtractFunctions(unittest.TestCase):
    def test_get_page_url(self):
        """Test pembuatan URL berdasarkan nomor halaman."""
        self.assertEqual(get_page_url(1), 'https://fashion-studio.dicoding.dev/')
        self.assertEqual(get_page_url(2), 'https://fashion-studio.dicoding.dev/page2')
        self.assertEqual(get_page_url(3), 'https://fashion-studio.dicoding.dev/page3')

    def test_parse_product(self):
        """Test fungsi parse_product dengan HTML produk yang valid."""
        html = """
        <div class="collection-card">
            <div class="product-title">Test Product</div>
            <div class="price-container">$10</div>
            <p>Rating: 4.5</p>
            <p>Red, Blue</p>
            <p>Size: M</p>
            <p>Gender: Unisex</p>
        </div>
        """
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.select_one('.collection-card')
        product = parse_product(element)
        
        self.assertEqual(product["Title"], "Test Product")
        self.assertEqual(product["Price"], "$10")
        self.assertEqual(product["Rating"], "4.5")
        self.assertEqual(product["Colors"], "Red, Blue")
        self.assertEqual(product["Size"], "M")
        self.assertEqual(product["Gender"], "Unisex")
        self.assertIn("Timestamp", product)

    @patch('utils.extract.requests.get')
    def test_scrape_page_success(self, mock_get):
        """Test fungsi scrape_page dengan respons HTML yang mengandung produk."""
        html = """
        <html>
          <body>
            <div class="collection-card">
              <div class="product-title">Test Product</div>
              <div class="price-container">$10</div>
              <p>Rating: 4.5</p>
              <p>Red, Blue</p>
              <p>Size: M</p>
              <p>Gender: Unisex</p>
            </div>
          </body>
        </html>
        """
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.text = html
        mock_get.return_value = fake_response

        result = scrape_page(1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["Title"], "Test Product")

    @patch('utils.extract.requests.get')
    def test_scrape_page_no_products(self, mock_get):
        """Test fungsi scrape_page saat tidak ada produk ditemukan."""
        html = "<html><body><p>Tidak ada produk di sini</p></body></html>"
        fake_response = MagicMock(status_code=200, text=html)
        mock_get.return_value = fake_response

        result = scrape_page(1)
        self.assertEqual(result, [])

    @patch('utils.extract.requests.get')
    def test_extract_data(self, mock_get):
        """
        Test fungsi extract_data dengan menghasilkan 1 produk per halaman.
        """
        html = """
        <html>
          <body>
            <div class="collection-card">
              <div class="product-title">Test Product</div>
              <div class="price-container">$10</div>
              <p>Rating: 4.5</p>
              <p>Red, Blue</p>
              <p>Size: M</p>
              <p>Gender: Unisex</p>
            </div>
          </body>
        </html>
        """
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.text = html
        mock_get.return_value = fake_response
        with patch('utils.extract.time.sleep', return_value=None):
            result = extract_data(1, 3)
        self.assertEqual(len(result), 3)