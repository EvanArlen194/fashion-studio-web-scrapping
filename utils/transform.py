import re
from typing import List, Dict

EXCHANGE_RATE = 16000

INVALID_VALUES = {"Unknown Product", "Invalid Rating", "Not Rated", "Price Unavailable", "N/A", None}

def clean_price(price_str: str) -> float:
    """Mengonversi harga dari format dolar ke rupiah atau None jika gagal."""
    try:
        if price_str.startswith("$"):
            return float(price_str.replace("$", "").strip()) * EXCHANGE_RATE
    except Exception as e:
        print(f"[ERROR] Gagal membersihkan harga '{price_str}': {e}")
    return None

def clean_rating(rating_str: str) -> float:
    """Mengonversi rating ke float atau None jika tidak valid."""
    try:
        match = re.search(r"[\d.]+", rating_str)
        if match:
            return float(match.group())
    except Exception as e:
        print(f"[ERROR] Gagal membersihkan rating '{rating_str}': {e}")
    return None

def clean_colors(colors_str: str) -> int:
    """Mengonversi jumlah warna ke integer atau 0 jika tidak valid."""
    try:
        digits = ''.join(filter(str.isdigit, colors_str))
        return int(digits) if digits else 0
    except Exception as e:
        print(f"[ERROR] Gagal membersihkan warna '{colors_str}': {e}")
        return 0

def transform_data(raw_data: List[Dict[str, str]]) -> List[Dict[str, any]]:
    """
    Membersihkan dan memproses data hasil scraping.
    """
    cleaned_data = []
    seen = set()

    for item in raw_data:
        try:
            title = item.get("Title", "").strip()
            price_str = item.get("Price", "").strip()
            rating_str = item.get("Rating", "").strip()
            colors_str = item.get("Colors", "").strip()
            size = item.get("Size", "").strip()
            gender = item.get("Gender", "").strip()

            if any(value in INVALID_VALUES for value in [title, price_str, rating_str, colors_str, size, gender]):
                continue

            price_value = clean_price(price_str)
            rating_value = clean_rating(rating_str)
            colors_value = clean_colors(colors_str)

            if price_value is None or rating_value is None:
                continue

            unique_key = (title, price_value, rating_value, colors_value, size, gender)
            if unique_key in seen:
                continue
            seen.add(unique_key)

            cleaned_item = {
                "Title": title,
                "Price": price_value,
                "Rating": rating_value,
                "Colors": colors_value,
                "Size": size,
                "Gender": gender,
                "Timestamp": item.get("Timestamp", "")
            }
            cleaned_data.append(cleaned_item)

        except Exception as conv_error:
            print(f"[ERROR] Gagal membersihkan data: {conv_error}")
            continue

    print(f"[INFO] Total data setelah transformasi: {len(cleaned_data)}")
    return cleaned_data
