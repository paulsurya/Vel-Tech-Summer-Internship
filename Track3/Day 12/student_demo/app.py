from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(r'C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\Track3\Day 12\student_demo\students.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            name      TEXT NOT NULL,
            roll      TEXT NOT NULL,
            dept      TEXT NOT NULL,
            year      TEXT NOT NULL,
            email     TEXT NOT NULL,
            phone     TEXT NOT NULL,
            gender    TEXT NOT NULL,
            dob       TEXT NOT NULL,
            address   TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    success = False
    if request.method == 'POST':
        name    = request.form['name']
        roll    = request.form['roll']
        dept    = request.form['department']
        year    = request.form['year']
        email   = request.form['email']
        phone   = request.form['phone']
        gender  = request.form['gender']
        dob     = request.form['dob']
        address = request.form['address']

        conn = sqlite3.connect(r'C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\Track3\Day 12\student_demo\students.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO students (name, roll, dept, year, email, phone, gender, dob, address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, roll, dept, year, email, phone, gender, dob, address))
        conn.commit()
        conn.close()
        success = True

    return render_template('register.html', success=success)

@app.route('/students')
def students():
    conn = sqlite3.connect(r'C:\Users\pauls\OneDrive\desktop\Vel-Tech-Summer-Internship\Track3\Day 12\student_demo\students.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    rows = c.fetchall()
    conn.close()

    student_list = []
    for row in rows:
        student_list.append({
            'id'     : row[0],
            'name'   : row[1],
            'roll'   : row[2],
            'dept'   : row[3],
            'year'   : row[4],
            'email'  : row[5],
            'phone'  : row[6],
            'gender' : row[7],
            'dob'    : row[8],
            'address': row[9]
        })

    return render_template('students.html', students=student_list)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)