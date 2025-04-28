import os
import pandas as pd
from typing import List, Dict
from google.oauth2 import service_account
from googleapiclient.discovery import build
from sqlalchemy import create_engine

CSV_FILENAME = os.getenv("CSV_FILENAME")
GSHEET_SERVICE_ACCOUNT_FILE = os.getenv("GSHEET_SERVICE_ACCOUNT_FILE")
GSHEET_SPREADSHEET_ID = os.getenv("GSHEET_SPREADSHEET_ID")
GSHEET_RANGE = os.getenv("GSHEET_RANGE")
POSTGRESQL_URL = os.getenv("POSTGRESQL_URL")

def load_to_csv(cleaned_data: List[Dict[str, any]], filename: str = CSV_FILENAME) -> None:
    """
    Menyimpan data bersih ke dalam file CSV.
    """
    if not cleaned_data:
        print("[WARN] Tidak ada data untuk disimpan ke CSV.")
        return

    try:
        df = pd.DataFrame(cleaned_data)
        df.to_csv(filename, index=False, encoding="utf-8")
        print(f"[INFO] Data berhasil disimpan ke file CSV: {filename}")
    except Exception as error:
        print(f"[ERROR] Gagal menyimpan data ke CSV: {error}")


def load_to_google_sheets(cleaned_data: List[Dict[str, any]]) -> None:
    """
    Menyimpan data bersih ke Google Sheets.
    """
    if not cleaned_data:
        print("[WARN] Tidak ada data untuk disimpan ke Google Sheets.")
        return

    try:
        df = pd.DataFrame(cleaned_data)
        values = [df.columns.tolist()] + df.values.tolist()

        creds = service_account.Credentials.from_service_account_file(
            GSHEET_SERVICE_ACCOUNT_FILE,
            scopes=["https://www.googleapis.com/auth/spreadsheets"],
        )
        service = build("sheets", "v4", credentials=creds)

        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=GSHEET_SPREADSHEET_ID,
                range=GSHEET_RANGE,
                valueInputOption="RAW",
                body=body,
            )
            .execute()
        )

        print(f"[INFO] Data berhasil disimpan ke Google Sheets: {result.get('updatedCells')} sel diperbarui.")

    except Exception as error:
        print(f"[ERROR] Gagal menyimpan data ke Google Sheets: {error}")


def load_to_postgresql(cleaned_data: List[Dict[str, any]]) -> None:
    """
    Menyimpan data bersih ke PostgreSQL.
    """
    if not cleaned_data:
        print("[WARN] Tidak ada data untuk disimpan ke PostgreSQL.")
        return

    try:
        engine = create_engine(POSTGRESQL_URL)
        df = pd.DataFrame(cleaned_data)
        df.to_sql("fashion_data", con=engine, if_exists="replace", index=False)
        print("[INFO] Data berhasil disimpan ke PostgreSQL.")
    except Exception as error:
        print(f"[ERROR] Gagal menyimpan data ke PostgreSQL: {error}")
        