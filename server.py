from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def one():
    return render_template('index.html')

@app.route('/<string:pagename>')
def index(pagename):
    return render_template(pagename)

def database_func(data):
    with open(r'C:\Users\syeds\Desktop\python_ztm\web\database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n {email},{subject},{message}')
        

def write_to_csv(data):
    with open(r'C:\Users\syeds\Desktop\python_ztm\web\databasee.csv',mode='a',newline='') as database2:                           
        fieldnames = ['email','subject','message']
        writer = csv.DictWriter(database2, fieldnames=fieldnames)
        writer.writeheader() 
        writer.writerow({'email':data['email'], 'subject':data['subject'],'message':data['message']})               

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
   if request.method=='POST':
       data= request.form.to_dict()
       write_to_csv(data)
       return redirect('/thankyou.html') 

  
