from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_google_sheets, load_to_postgresql

def main():
    try:
        raw_data = extract_data(start_page=1, end_page=50)
    except Exception as error:
        print(f"[ERROR] Proses extract gagal: {error}")
        return

    try:
        cleaned_data = transform_data(raw_data)
    except Exception as error:
        print(f"[ERROR] Proses transform gagal: {error}")
        return

    try:
        load_to_csv(cleaned_data)
    except Exception as error:
        print(f"[ERROR] Proses load ke CSV gagal: {error}")

    try:
        load_to_google_sheets(cleaned_data)
    except Exception as error:
        print(f"[ERROR] Proses load ke Google Sheets gagal: {error}")

    try:
        load_to_postgresql(cleaned_data)
    except Exception as error:
        print(f"[ERROR] Proses load ke PostgreSQL gagal: {error}")

if __name__ == "__main__":
    main()