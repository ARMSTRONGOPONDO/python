import pyotp
import sqlite3
import hashlib
import uuid
from flask import Flask, request

app = Flask(__name__)
db_name = "test.db"

@app.route('/')
def index():
    return "welcome to the hands on lab for password evolution systems!"

@app.route('/signup/v1', methods=['POST'])
def signup_v1():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_PLAIN
                 (USERNAME TEXT PRIMARY KEY NOT NULL,
                  PASSWORD TEXT NOT NULL);''')
    conn.commit()
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return "username and password are required", 400
    
    try:
        c.execute("INSERT INTO USER_PLAIN (USERNAME, PASSWORD) VALUES (?, ?)", (username, password))
        conn.commit()
        print('username:', username, 'password:', password)
        return "signup success"
    except sqlite3.IntegrityError:
        return "username has been registered."
    finally:
        conn.close()

def verify_plain(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = ?"
    c.execute(query, (username,))
    records = c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == password

@app.route('/login/v1', methods=['POST'])
def login_v1():
    if request.method == 'POST':
        if verify_plain(request.form['username'], request.form['password']):
            return 'login success'
        else:
            return 'Invalid username/password'
    else:
        return 'Invalid Method'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
