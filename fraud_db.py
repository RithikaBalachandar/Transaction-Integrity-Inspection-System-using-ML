import sqlite3

# Connect to (or create) the database file 'fraud.db'
conn = sqlite3.connect('fraud.db')
cursor = conn.cursor()
