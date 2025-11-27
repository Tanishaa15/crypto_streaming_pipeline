import sqlite3
import pandas as pd
from config import DATABASE_NAME, TABLE_NAME

def get_latest_data(limit=100):
    """Fetch latest crypto data from sqlite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    
    query = f"""
        SELECT * 
        FROM {TABLE_NAME}
        ORDER BY timestamp DESC
        LIMIT ?
    """
    
    df = pd.read_sql_query(query, conn, params=(limit,))
    conn.close()
    return df
