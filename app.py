
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

# Call init_db to create the database before running the application
init_db()

@app.route('/')
def index():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", ('World',))
        conn.commit()  # Commit the changes to the database
    return render_template('index.html', name='World')

if __name__ == '__main__':
    app.run(debug=True)
