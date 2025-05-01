import sqlite3
from datetime import datetime

DB_NAME = 'journal.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def create_entry(title, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO entries (title, content)
        VALUES (?, ?)
    ''', (title, content))
    conn.commit()
    conn.close()

def get_all_entries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_entry(entry_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries WHERE id = ?', (entry_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_entry(entry_id, title, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE entries
        SET title = ?, content = ?
        WHERE id = ?
    ''', (title, content, entry_id))
    conn.commit()
    conn.close()

def delete_entry(entry_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
    conn.commit()
    conn.close()

