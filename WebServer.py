from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
print(__name__)


@app.route('/') 
def home():
    return render_template('index.html') 

@app.route('/<string:page_name>')
def page(page_name = None):
    return render_template(page_name)

# @app.route('/works.html') 
# def works():
#     return render_template('works.html') 

# @app.route('/about.html') 
# def about():
#     return render_template('about.html') 

# @app.route('/contact.html') 
# def contact():
#     return render_template('contact.html') 

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     return 'form submitted hoooorraayyyyyy!!'

def writeinfile(data):
    with open('database.txt', mode='a') as database: #mode='a' means append in the file cause the file already exists similarly could have wrote 'wb' or 'rb' to rwrite or read modes
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def writetocsv(data):
    with open('database.csv',newline='', mode='a') as database2: #mode='a' means append in the file cause the file already exists similarly could have wrote 'wb' or 'rb' to rwrite or read modes
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
   if request.method == 'POST':
       data = request.form.to_dict()
       writeinfile(data)
       writetocsv(data)
       return redirect('/thankyou.html')
   else:
       return 'something went wrong. Try again'
   
