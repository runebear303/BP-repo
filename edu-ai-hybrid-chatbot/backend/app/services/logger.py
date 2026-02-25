import sqlite3
from config import DB_PATH

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS logs (q TEXT, a TEXT)")
conn.commit()

def log_chat(q, a):
    c.execute("INSERT INTO logs VALUES (?,?)", (q, a))
    conn.commit()