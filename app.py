from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__ , template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"{username}, {password}"
    else:
        return "Go To Signup Page"

if __name__ == "__main__":
    app.run(debug=True, port=1000) 