from flask import Flask,redirect, url_for,render_template,request
import os
from index import d_dtcn

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

# Defining the home page of our site
@app.route("/",methods=['GET', 'POST'])
def home():
        return render_template("index.html")

@app.route("/start", methods=['GET', 'POST'])       
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            d_dtcn()
            return render_template("index.html")
        if request.form.get('contact') == "contact":
            return render_template('contact.html')
    else:
        # pass # unknown
        return render_template("index.html")

@app.route('/contact.html', methods=['GET', 'POST'])
def cool_form():
        return render_template("contact.html")

if __name__ == "__main__":
    app.run()
    
