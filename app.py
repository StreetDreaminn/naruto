from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(
    database="postgres",
    host="127.0.0.1",
    user="postgres",
    password="test123",
    port="5432")
    
    return conn

@app.route('/')
def home():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM naruto ORDER BY id")
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('home.html', data=data)

@app.route('/changes')
def changes():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM naruto ORDER BY id")
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('updating.html', data=data)

@app.route('/character-page')
def new_naruto_character():
    return render_template('data.html')

@app.route('/new-character', methods=['POST'])
def create():
    conn = db_conn()
    cur = conn.cursor()
    first_name = request.form['first_name']

    cur.execute("SELECT first_name FROM naruto WHERE first_name = '%s'" % first_name)
    check = cur.fetchall()

    if check[0][0] != []:
        return render_template('error_page.html')

    last_name = request.form['last_name']
    age = request.form['age']
    rank = request.form['rank']
    sex = request.form['sex']
    affiliation = request.form['affiliation']
    primary_chakra_nature = request.form['primary_chakra_nature']
    secondary_chakra_nature = request.form['secondary_chakra_nature']
    genjutsu = request.form['genjutsu']
    ninjutsu = request.form['ninjutsu']
    taijutsu = request.form['taijutsu']
    cur.execute(
        "INSERT INTO naruto (first_name, last_name, age, rank, sex, \
        affiliation, primary_chakra_nature, secondary_chakra_nature, \
        genjutsu, ninjutsu, taijutsu) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (first_name, last_name, age, rank, sex, affiliation, primary_chakra_nature, 
        secondary_chakra_nature, genjutsu, ninjutsu, taijutsu))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('home'))

@app.route('/update', methods=['POST'])
def update():
    conn = db_conn()
    cur = conn.cursor()
    id = request.form['id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    rank = request.form['rank']
    sex = request.form['sex']
    affiliation = request.form['affiliation']
    primary_chakra_nature = request.form['primary_chakra_nature']
    secondary_chakra_nature = request.form['secondary_chakra_nature']
    genjutsu = request.form['genjutsu']
    ninjutsu = request.form['ninjutsu']
    taijutsu = request.form['taijutsu']

    cur.execute(
        "UPDATE naruto SET \
        first_name=%s, \
        last_name=%s, \
        age=%s, \
        rank=%s, \
        sex=%s, \
        affiliation=%s, \
        primary_chakra_nature=%s, \
        secondary_chakra_nature=%s, \
        genjutsu=%s, \
        ninjutsu=%s, \
        taijutsu=%s \
        WHERE id =%s", (first_name, last_name, age, rank, sex, affiliation, primary_chakra_nature, 
        secondary_chakra_nature, genjutsu, ninjutsu, taijutsu, id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('home'))

@app.route('/delete', methods=['POST'])
def delete():
    conn = db_conn()
    cur = conn.cursor()

    id = request.form['id']

    cur.execute("DELETE FROM naruto WHERE id=%s" % id)
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)