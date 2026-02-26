import sqlite3
from datetime import datetime

DB_NAME = "fim.db"

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS baseline (
            file_path TEXT PRIMARY KEY,
            file_size INTEGER,
            checksum TEXT,
            last_modified TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_record(path, size, checksum, modified):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO baseline
        VALUES (?, ?, ?, ?, ?)
    """, (path, size, checksum, modified, datetime.now()))

    conn.commit()
    conn.close()

def get_all_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM baseline")
    records = cursor.fetchall()
    conn.close()
    return records
