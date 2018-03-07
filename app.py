from flask import (Flask, render_template, 
    session, redirect, url_for, escape, request, send_from_directory)
from flask_wtf import Form
from CMS import *
from flask_cache_buster import CacheBuster


config = {
     'extensions': ['.js', '.css', '.csv'],
     'hash_size': 10
}
cache_buster = CacheBuster(config=config)


app = Flask(__name__)
cache_buster.register_cache_buster(app)

app.config['UPLOAD_FOLDER'] = '/nexmoj'

def tog_lang(lang):
    if lang == 'en':
        return 'ar'
    return 'en'

@app.route('/')
def home():    
    return render_template('index1.html', D_INDEX=D_INDEX, LANG=LANG, LANGUAGE=LANGUAGE )


@app.route('/lang')
def lang():
    global LANG
    LANG = tog_lang(LANG)
    return render_template('index1.html', D_INDEX=D_INDEX, LANG=LANG, LANGUAGE=LANGUAGE )

@app.route('/logged')
def logged():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login')
def login():
    return render_template('login.html', D_INDEX=D_INDEX, LANG=LANG, LANGUAGE=LANGUAGE)
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('logged'))
    return '''
        <form method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>
        '''

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', D_INDEX=D_INDEX, LANG=LANG, LANGUAGE=LANGUAGE)

@app.route('/consult')
def consult():
    return render_template('consult.html', D_INDEX=D_INDEX, LANG=LANG, LANGUAGE=LANGUAGE)

@app.route('/account')
def account():
    return render_template('account.html', D_INDEX=D_INDEX, LANG=LANG, LANGUAGE=LANGUAGE)

@app.route('/account/upload')
def upload():
    return render_template('upload.html', D_INDEX=D_INDEX, LANG=LANG, LANGUAGE=LANGUAGE)


@app.route('/logout')
def logout():
# remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/nexmoj/<filename>')
def welcome_call(filename):
    print(app.config['UPLOAD_FOLDER'])
    return send_from_directory('nexmoj', filename)

# set the secret key. keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run(debug=False)


