import time
import requests
from datetime import datetime
from typing import List, Dict
from bs4 import BeautifulSoup

def get_page_url(page: int) -> str:
    """
    Membuat URL berdasarkan nomor halaman.
    """
    try:
        if not isinstance(page, int):
            raise TypeError("Parameter 'page' harus bertipe int.")
        if page < 1:
            raise ValueError("Parameter 'page' harus bernilai minimal 1.")

        if page == 1:
            return 'https://fashion-studio.dicoding.dev/'
        return f'https://fashion-studio.dicoding.dev/page{page}'
    except Exception as e:
        print(f"[ERROR] Gagal membuat URL untuk page {page}: {e}")
        raise


HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/120.0.0.0 Safari/537.36'
    )
}

def parse_product(product_element) -> Dict[str, str]:
    """Ekstrak data produk dari elemen HTML dan mengembalikan sebagai dictionary."""
    try:
        title = product_element.select_one('.product-title').get_text(strip=True)
        price = product_element.select_one('.price-container')
        price = price.get_text(strip=True) if price else "N/A"

        details = product_element.find_all('p')
        rating = details[0].get_text(strip=True).replace('Rating: ', '') if len(details) > 0 else "N/A"
        colors = details[1].get_text(strip=True) if len(details) > 1 else "N/A"
        size = details[2].get_text(strip=True).replace('Size: ', '') if len(details) > 2 else "N/A"
        gender = details[3].get_text(strip=True).replace('Gender: ', '') if len(details) > 3 else "N/A"

        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "Timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        print(f"[ERROR] Gagal mem-parsing produk: {e}")
        return {
            "Title": "N/A",
            "Price": "N/A",
            "Rating": "N/A",
            "Colors": "N/A",
            "Size": "N/A",
            "Gender": "N/A",
            "Timestamp": datetime.now().isoformat()
        }

def scrape_page(page: int) -> List[Dict[str, str]]:
    """Melakukan scraping pada satu halaman dan mengembalikan daftar produk."""
    url = get_page_url(page)
    print(f"[INFO] Scraping halaman {page}: {url}")
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        product_elements = soup.select('.collection-card')
        
        if not product_elements:
            print(f"[WARNING] Tidak ada produk ditemukan di halaman {page}")
            return []

        return [parse_product(element) for element in product_elements]
    
    except requests.Timeout:
        print(f"[ERROR] Timeout saat mengakses halaman {page}")
    except requests.ConnectionError:
        print(f"[ERROR] Koneksi gagal saat mengakses halaman {page}")
    except requests.HTTPError as e:
        print(f"[ERROR] HTTP error ({e.response.status_code}) pada halaman {page}")
    except Exception as parse_error:
        print(f"[ERROR] Gagal memproses halaman {page}: {parse_error}")
    
    return []

def extract_data(start_page: int = 1, end_page: int = 50) -> List[Dict[str, str]]:
    """Scrape data dari beberapa halaman dan mengembalikan sebagai list of dictionaries."""
    all_products = []
    for page in range(start_page, end_page + 1):
        try:
            products = scrape_page(page)
            all_products.extend(products)
            time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Gagal mengekstrak data dari halaman {page}: {e}")
    print(f"[INFO] Total produk yang diekstrak: {len(all_products)}")
    return all_products
