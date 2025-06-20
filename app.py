from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "TA_CLE_SECRETE"

def get_db():
    conn = sqlite3.connect('utilisateurs.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    if 'user_email' in session:
        return render_template('accueil.html', email=session['user_email'])
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        mdp = request.form['mot_de_passe']
        hashed = generate_password_hash(mdp)

        conn = get_db()
        try:
            conn.execute("INSERT INTO utilisateurs (email, mot_de_passe) VALUES (?,?)", (email, hashed))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Cet e‑mail est déjà utilisé."
        finally:
            conn.close()
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        mdp = request.form['mot_de_passe']

        conn = get_db()
        user = conn.execute("SELECT * FROM utilisateurs WHERE email=?", (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['mot_de_passe'], mdp):
            session['user_email'] = email
            return redirect(url_for('home'))
        return "Identifiants incorrects."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

