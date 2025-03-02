import sqlite3

conn = sqlite3.connect("jobs.db")  # Create database
cursor = conn.cursor()

# Create table for jobs
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company TEXT,
    location TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized successfully.")
