from flask import Flask
from flask import render_template

app = Flask(__name__)

# main routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')