from flask import Flask,render_template,request,redirect,flash,url_for
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data = request.form.to_dict()
        write_to_file(data)
        return render_template("thankyou.html")
    else:
        return "somethings wrong"
def write_to_file(data):
    with open("database.txt", "a") as database:
        name=data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {name},{email},{subject},{message}')
 
def write_to_csv(data):
    with open("database.csv", "a") as database2:
        name=data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimitter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email, subject, message])



