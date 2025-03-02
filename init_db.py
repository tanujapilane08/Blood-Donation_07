import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     job_title TEXT NOT NULL,
                     company TEXT NOT NULL,
                     location TEXT NOT NULL)''')
conn.commit()
conn.close()
print("Database setup complete.")
