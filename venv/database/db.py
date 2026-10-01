import sqlite3

conn = sqlite3.connect("venv/dialogs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

def save_message(user_id, role, content) -> None:
    cursor.execute(
        "INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)",
        (user_id, role, content)
    )
    conn.commit()

def get_history(user_id, limit=10):
    cursor.execute(
        "SELECT role, content FROM messages WHERE user_id = ? ORDER BY id DESC LIMIT ?",
        (user_id, limit)
    )

    return cursor.fetchall()[::-1]
