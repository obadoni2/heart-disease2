from flask import Flask, render_template, redirect, url_for, request, session, g, flash
from flask_sqlalchemy import SQLAlchemy 
import json 
from datetime import datetime 
from app.admin.routes import routes
import pickle 
import numpy as np 
import re  # Added for regex operations

local_server = True
model = pickle.load(open('/c/Users/EMMA/prediction/disease/modal2.pkl', 'rb'))


app = Flask(__name__)

app.register_blueprint(routes, url_prefix='')

from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv('DATABASE_URL')
if db_url and db_url.startswith('postgresql://'):
    db_url = db_url.replace('postgresql://', 'postgresql+psycopg2://')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')
    
db = SQLAlchemy(app)

# payment module code   
from instamojo_wrapper import Instamojo

API_KEY = "test_1ad79f83a33b5de2516eaacd2a8"
AUTH_TOKEN = "test_9786a808d209aa8cc8df8a3664c"

api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

# Models
class Hdpuser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(120), unique=False, nullable=False)
    LastName = db.Column(db.String(120), unique=False, nullable=False)
    Email = db.Column(db.String(120), unique=False, nullable=False)  # Changed from 20 to 120
    Ph_no = db.Column(db.String(20), unique=False, nullable=False)  # Changed from Integer to String
    Profession = db.Column(db.String(12), unique=False, nullable=False)
    Username = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

class Doclog(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Corrected from primery_key
    FirstName = db.Column(db.String(120), unique=False, nullable=False)  # Corrected from Firstname
    LastName = db.Column(db.String(120), unique=False, nullable=False)  # Corrected from Lastname
    Ph_no = db.Column(db.String(20), unique=False, nullable=False)  # Changed from Integer to String
    Profession = db.Column(db.String(12), unique=False, nullable=False)
    Username = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(120), unique=False, nullable=False)  # Corrected from db.string
    Password = db.Column(db.String(120), unique=False, nullable=False)  # Corrected from db.string

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(120), unique=False, nullable=False)  # Corrected from db.Coumn

class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Age = db.Column(db.Integer, unique=False, nullable=False)
    sex = db.Column(db.Integer, unique=False, nullable=False)
    Cp = db.Column(db.Integer, unique=False, nullable=False)
    Trestbps = db.Column(db.Integer, unique=False, nullable=False)
    Chol = db.Column(db.Integer, unique=False, nullable=False)
    fbs = db.Column(db.Integer, unique=False, nullable=False)
    Restecg = db.Column(db.Integer, unique=False, nullable=False)
    Thalach = db.Column(db.Integer, unique=False, nullable=False)
    Exang = db.Column(db.Integer, unique=False, nullable=False)
    Oldpeak = db.Column(db.Integer, unique=False, nullable=False)  # Corrected from Olpeak
    Slope = db.Column(db.Integer, unique=False, nullable=False)
    Thal = db.Column(db.Integer, unique=False, nullable=False)
    Target = db.Column(db.Integer, unique=False, nullable=False)

app.secret_key = 'recordsaremeanttobroken'

@app.before_request 
def load_users():
    if 'user' in session:
        g.user = session['user']
    else:
        g.user = None 

@app.route('/')
@app.route('/admlogin', methods=['GET', 'POST'])
def admlogin():
    if request.method == 'POST':
        uname = request.form['username']
        passd = request.form['password']
        user1 = Admin.query.filter_by(Username=uname).first()
        pass1 = Admin.query.filter_by(Password=passd).first()
        
        if user1 and pass1: 
            session['user'] = uname
            return redirect('/dash')
        else:
            flash("Invalid Credentials")
    return render_template('admlogin.html')

@app.route('/register', methods=['GET', 'POST']) 
def register():
    msg = ''
    if request.method == 'POST':
        firstname1 = request.form['firstname']
        lastname1 = request.form['lastname']
        email1 = request.form['email']
        Ph_no1 = request.form['phone']
        pro1 = request.form['Pro']
        username1 = request.form['uname']
        password1 = request.form['password']
        
        email = Hdpuser.query.filter_by(Email=email1).first()
        phonenumber = Hdpuser.query.filter_by(Ph_no=Ph_no1).first()
        uname = Hdpuser.query.filter_by(Username=username1).first()
        if email: 
            flash('Email address already exists')
        elif phonenumber:
            flash('Phone number already exists')
        elif uname:
            flash('Username already taken')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email1):
            flash('Invalid email address input !')
        else:
            entry = Hdpuser(FirstName=firstname1, LastName=lastname1, Email=email1, Ph_no=Ph_no1, Profession=pro1, Username=username1, password=password1)
            db.session.add(entry)
            db.session.commit()
            flash("Added Successfully")
    return render_template('patregis.html')

@app.route('/doctorlogin', methods=['GET', 'POST'])
def doclogin(): 
    msg = ""
    
    if request.method == 'POST':
        uname = request.form['username']
        passd = request.form['password']
        user1 = Doclog.query.filter_by(Username=uname).first()  # Corrected from Doclogs
        if user1 and passd == user1.password:
            session['user'] = uname 
            return render_template('docindex.html', user1=user1)
        else:
            msg = "Wrong Credentials !"
    return render_template('doclogin.html', msg=msg)

@app.route('/dash')
def dash(): 
    d = Dataset.query.all()
    co = Hdpuser.query.all()
    co2 = Doclog.query.all()
    count = len(co)
    count1 = len(co)
    count2 = len(co2)
    c22 = count2 // 2
    return render_template('dash.html', d=d, count=count, count1=count1, count2=count2, c22=c22)

@app.route('/patientlogin', methods=['GET', 'POST'])
def patlog():
    msg = ""
    if request.method == 'POST':
        uname = request.form['username']
        passd = request.form['password']
        user1 = Hdpuser.query.filter_by(Username=uname).first()
        if user1 and passd == user1.password:
            session['user'] = uname 
            return render_template('profilepatient.html', user1=user1)
        else:
            msg = "Wrong Credentials !"
    return render_template('patogin.html', msg=msg)

@app.route('/docregis', methods=['GET', 'POST'])
def docregis(): 
    msg = ''
    if request.method == 'POST': 
        firstname2 = request.form['firstname']
        lastname2 = request.form['lastname']  # Corrected from lastname
        email2 = request.form['email']        # Corrected from emal
        Ph_no2 = request.form['phone']
        pro2 = request.form['Pro']
        username2 = request.form['uname']
        password2 = request.form['password']
        
        email = Doclog.query.filter_by(Email=email2).first()
        phonenumber = Doclog.query.filter_by(Ph_no=Ph_no2).first()
        uname = Doclog.query.filter_by(Username=username2).first()
        if email: 
            flash('Email address already exists')
        elif phonenumber:
            flash('Phone number already exists')
        elif uname: 
            flash('Username already taken')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email2):
            flash('Invalid email address input !')
        else: 
            entry = Doclog(FirstName=firstname2, LastName=lastname2, Email=email2, Ph_no=Ph_no2, Profession=pro2, Username=username2, password=password2)
            db.session.add(entry)
            db.session.commit()
            flash("Added Successfully")
    return render_template('docregis.html')

@app.route('/pattable', methods=['GET', 'POST'])
def adminview():
    c = Hdpuser.query.all()
    return render_template('pattable.html', c=c) 

@app.route('/doctable', methods=['GET', 'POST'])
def admindoc(): 
    c = Doclog.query.all()
    return render_template('doctable.html',c=c)

@app.route('/emailcount', methods=['GET'])
def emailcount(): 
    c = Emails.query.all()
    print(c)
    return render_template('emailscount.html', c=c)

@app.route('/heartcheck', methods=['GET', 'POST'])
def heartcheck(): 
    return render_template("heartcheck.html")

@app.route('/predict', methods=['POST'])
def predict(): 
    if request.method == 'POST':
        model = pickle.load(open('/c/Users/EMMA/prediction/disease/modal2.pkl', 'rb'))
        int_features = [int(x) for x in request.form.values()]  # Corrected from value()
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = round(prediction[0],2)
        if output == 1:
            o = "Bad News ! \n There is a chance that you have a heart disease"
            return render_template('heartcheck.html', prediction_text='Heart status: {}'.format(o))
        else:
            o = "Good News !\n There is no chance that you have a heart disease ! :)"
            return render_template('heartcheck.html', prediction_text='Heart status: {}'.format(o))
    return redirect('/heartcheck') 

@app.route('/docpredict', methods=['POST'])
def docpredict():
    if request.method == 'POST':
        model = pickle.load(open('/c/Users/EMMA/prediction/disease/modal2.pkl', 'rb'))
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = round(prediction[0],2)
        if output == 1:
            o = "Bad News ! \n There is a chance that you have a heart disease"
            return render_template('heartcheck.html', prediction_text='Heart status: {}'.format(o))
        else:
            o = "Good News ! \n There is no chance that you have a heart disease ! :)"
            return render_template('heartcheck.html', prediction_text='Heart status: {}'.format(o))
    return redirect('/heartcheck')

# CRUD Operations

@app.route('/pattable', methods=['GET', 'POST']) 
def viewadmin():
    c = Hdpuser.query.all()
    return render_template("pattable.html", c=c)

@app.route('/adminup', methods=['GET', 'POST'])
def adminup():
    if request.method == 'POST':
        c = Hdpuser.query.get(request.form.get('id'))
        if c:
            c.FirstName = request.form['name']
            c.LastName = request.form['name2']
            c.Email = request.form['email']
            c.Ph_no = request.form['phone']
            c.Username = request.form['usern']
            c.password = request.form['pass']
            db.session.commit()
            flash("Patient detail Updated Successfully")
        return redirect(url_for('adminview'))

@app.route('/admindocup', methods=['GET', 'POST'])
def admindocup():
    if request.method == 'POST':
        c = Doclog.query.get(request.form.get('id'))
        if c:
            c.FirstName = request.form['name']
            c.LastName = request.form['name2']
            c.Ph_no = request.form['phone']
            c.Username = request.form['usern']
            c.password = request.form['pass']
            db.session.commit()
            flash("Doctor Details Updated Successfully")
        return redirect(url_for('admindoc'))

@app.route('/admindel/<int:id>/', methods=['GET', 'POST'])  # Added type hint for id
def admindel(id):
    c = Hdpuser.query.get(id)
    if c:
        db.session.delete(c)
        db.session.commit()
        flash("Patient Deleted Successfully")
    return redirect(url_for('adminview'))

@app.route('/admindeldoc/<int:id>/', methods=['GET', 'POST'])  # Corrected route syntax
def admindeldoc(id):
    c = Doclog.query.get(id)
    if c:
        db.session.delete(c)
        db.session.commit()
        flash("Doctor Deleted Successfully")
    return redirect(url_for('admindoc'))

# Doctor Dashboard

@app.route('/viewdatatable')
def viewdatable():
    ds = Dataset.query.all()
    c = Doclog.query.filter_by(Username=g.user).first()
    return render_template('datatable.html', ds=ds, c=c)

@app.route('/docindex')
def docindex():
    curr = Doclog.query.filter_by(Username=g.user).first()
    return render_template('docindex.html', user1=curr)

@app.route('/viewpatient')
def viewpatient():
    patient = Hdpuser.query.all()
    c = Doclog.query.filter_by(Username=g.user).first()
    return render_template('viewpatient.html', patient=patient, c=c)

@app.route('/userprofile')
def userprofile():
    c = Doclog.query.filter_by(Username=g.user).first()
    return render_template('userprofile.html', c=c)

@app.route('/docupdata', methods=['GET', 'POST'])
def docupdate():
    if request.method == 'POST':
        d = Doclog.query.filter_by(Username=g.user).first()
        if d:
            d.FirstName = request.form['name1']
            d.LastName = request.form['name2']
            d.Email = request.form['email']
            d.Ph_no = request.form['phone']
            d.Profession = request.form['pro']
            db.session.commit()
            flash("Doctor Details Updated Successfully")
        return redirect(url_for('userprofile'))

@app.route('/profilepat')
def profilepat():
    c = Hdpuser.query.filter_by(Username=g.user).first()
    return render_template('profilepatient.html', user1=c)

@app.route('/checkheart', methods=['GET', 'POST'])
def checkheart():
    return render_template('paymenthome.html')

# Payment Module
@app.route('/payment', methods=['GET', 'POST'])
def payhome():
    return render_template('paysuccess.html')

@app.route('/success')
def success():
    return render_template('paysuccess.html')

@app.route('/pay', methods=['POST', 'GET'])
def pay():
    if request.method == 'POST':
        name = request.form.get('name')
        purpose = request.form.get('purpose')
        email = request.form.get('email')
        amount = request.form.get('amount')
        
        response = api.payment_request_create(
            amount=amount,
            purpose=purpose,
            buyer_name=name,
            send_email=True,
            email=email, 
            redirect_url="http://localhost:5000/success"
        )
        
        return redirect(response['payment_request']['longurl'])
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
