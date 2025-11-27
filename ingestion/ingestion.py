import requests
import sqlite3
import time
from config import API_URL, DATABASE_NAME, TABLE_NAME, STREAM_INTERVAL

def create_table():
    """Create the crypto_prices table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()

    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            price REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def fetch_and_store():
    """Fetch crypto prices from API and store in the database."""
    print("Starting crypto price ingestion...")
    
    while True:
        try:
            response = requests.get(API_URL)
            response.raise_for_status()  # Raise exception for bad responses
            data = response.json()

            conn = sqlite3.connect(DATABASE_NAME)
            cur = conn.cursor()

            for item in data:
                cur.execute(
                    f"INSERT INTO {TABLE_NAME} (symbol, price) VALUES (?, ?)",
                    (item["symbol"], float(item["price"]))
                )

            conn.commit()
            conn.close()

            print(f"Inserted batch of {len(data)} records into DB.")
            time.sleep(STREAM_INTERVAL)

        except requests.exceptions.RequestException as req_err:
            print("Request error:", req_err)
            time.sleep(STREAM_INTERVAL)
        except Exception as e:
            print("Error:", e)
            time.sleep(STREAM_INTERVAL)


if __name__ == "__main__":
    create_table()
    fetch_and_store()
