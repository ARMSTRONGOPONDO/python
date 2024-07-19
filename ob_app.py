from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error
import time

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='obituary'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def index():
    return render_template('obituary_form.html')

@app.route('/submit', methods=['POST'])
def submit_obituary():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    date_of_death = request.form['date_of_death']
    content = request.form['content']
    author = request.form['author']
    slug = generate_unique_slug(name)

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO obituaries (name, date_of_birth, date_of_death, content, author, submission_date, slug) VALUES (%s, %s, %s, %s, %s, NOW(), %s)"
        values = (name, date_of_birth, date_of_death, content, author, slug)
        try:
            cursor.execute(sql, values)
            conn.commit()
            message = "Obituary submitted successfully!"
        except Error as e:
            message = f"Error: {e}"
        cursor.close()
        conn.close()
    else:
        message = "Database connection failed"

    return render_template('obituary_form.html', message=message)

@app.route('/view')
def view_obituaries():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM obituaries")
        obituaries = cursor.fetchall()
        cursor.close()
        conn.close()
    else:
        obituaries = []
    
    return render_template('obituary_view.html', obituaries=obituaries)

def generate_slug(name):
    return '-'.join(name.lower().split())

def generate_unique_slug(name):
    slug = generate_slug(name)
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        while True:
            cursor.execute("SELECT COUNT(*) FROM obituaries WHERE slug = %s", (slug,))
            if cursor.fetchone()[0] == 0:
                break
            slug = f"{slug}-{int(time.time())}"
        cursor.close()
        conn.close()
    return slug

if __name__ == '__main__':
    app.run(debug=True)
