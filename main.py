# Python_Railway_System
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)#flask constructor takes name of current module(__name__)as a argument(DunDuck)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/train_system'
db = SQLAlchemy(app)



class Index(db.Model):
    '''tno,t_name,from,to,departs,arrive,duration,fare'''
    tno = db.Column(db.Integer, primary_key=True)
    t_name = db.Column(db.String(20), nullable=False)
    t_from = db.Column(db.String(20), nullable=False)
    to = db.Column(db.String(20), nullable=False)
    departs = db.Column(db.DateTime, nullable=False)
    arrive = db.Column(db.DateTime,  nullable=False)
    duration = db.Column(db.DateTime,  nullable=False)
    fare = db.Column(db.String(20),  nullable=False)

class Signup(db.Model):
    ''''`u_no`, `first_name`, `last_name`, `mobile_no`, `email`, `address`, `state`, `zip`'''
    __tablename__ = 'sign_up'
    u_no = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    mobile_no = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    zip = db.Column(db.Integer, nullable=True)
 

@app.route('/',methods=['GET','POST'])
def home():
     user = Index.query.all()
     return render_template('index.html',user=user)

@app.route('/log-in_')
def log_in():
    return render_template('log-in_.html')

@app.route("/sign_up",methods=['GET','POST'])
def signup():
    if(request.method=='POST'):
        '''getting data from sign up html code'''
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        mobile_no=request.form.get('mobile_no')
        email=request.form.get('email')
        address=request.form.get('address')
        state=request.form.get('state')
        zip=request.form.get('zip')
        '''`first_name`, `last_name`, `mobile_no`, `email`, `address`, `state`, `zip`'''
        '''assigning data to  sign_up table'''
        entry=Signup(first_name=fname, last_name=lname, mobile_no=mobile_no,email=email,address=address,state=state,zip=zip)
        db.session.add(entry)
        db.session.commit()
    return render_template('sign_up.html')

app.run(debug=True)
