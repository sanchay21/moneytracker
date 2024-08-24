from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///moneytrack.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()

class user(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    data_type = db.Column(db.String(15), nullable=False)
    amount = db.Column(db.Integer)
    desc = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno}. {self.data_type} - {self.amount}"

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