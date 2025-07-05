import sqlite3
import json
from datetime import datetime

def parse_date_safe(date_str):
    if date_str is None:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

conn = sqlite3.connect('owosch.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vegetables (
    vegetable_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    vegetable_name TEXT,
    vegetable_price REAL,
    vegetable_harvest DATE           
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS production (
    production_id INTEGER PRIMARY KEY AUTOINCREMENT,
    production_name TEXT,
    production_popularity TEXT,
    production_delivery DATE
);
""")

with open("vegetable.json", "r", encoding="utf-8") as f:
    vegetables = json.load(f)

    for vegetable in vegetables:
        cursor.execute("""
            INSERT INTO vegetables (
                vegetable_name, vegetable_price, vegetable_harvest
            ) VALUES (?, ?, ?)
        """, (
            vegetable.get("vegetable_name"),
            vegetable.get("vegetable_price"),
            parse_date_safe(vegetable.get("vegetable_harvest"))
        ))

        veg_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO production (
                production_name, production_popularity, production_delivery
            ) VALUES (?, ?, ?)
        """, (
            vegetable.get("production_name"),
            vegetable.get("production_popularity"),
            parse_date_safe(vegetable.get("production_delivery"))
        ))

conn.commit()
conn.close()