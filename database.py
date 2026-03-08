import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
user_id INTEGER PRIMARY KEY,
balance INTEGER DEFAULT 0,
ref_by INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS settings(
key TEXT,
value TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS withdraw(
user_id INTEGER,
amount INTEGER,
status TEXT
)
""")

conn.commit()
