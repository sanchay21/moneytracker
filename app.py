from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flask import session

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///moneytrack.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()
app.secret_key = 'the random string'
class moneydata(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    data_type = db.Column(db.String(15), nullable=False)
    amount = db.Column(db.Integer)
    desc = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno}. {self.data_type} - {self.amount}"
    
class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30), nullable=False)
    upass = db.Column(db.String(30), nullable=False)

    def __repr__(self) -> str:
        return f"{self.user_id}. {self.uname}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']

        register=user(uname=username, upass=password)
        db.session.add(register)
        db.session.commit()

        session['username']=username
        session['password']=password
        return redirect('home')
    else:
        return render_template('signup.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    username=session['username']
    password=session['password']
    print(username)

    if request.method == 'POST':
        data_type=request.form['data_type']
        amount=request.form['amount']
        desc=request.form['desc']
        NewMoneyData=moneydata(data_type=data_type, amount=amount, desc=desc)
        db.session.add(NewMoneyData)
        db.session.commit()
    moneyData = moneydata.query.all()
    
    return render_template('home.html', moneyData=moneyData)
    
@app.route('/showdata')
def showdata(): 
    userData = user.query.all()
    return render_template('home.html', userData=userData)

@app.route('/clear_session')
def clear_sess():
    session.clear()

if __name__ == "__main__":
    app.run(debug=True, port=1000) 