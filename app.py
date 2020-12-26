from flask import Flask, render_template, request
from requests import get
from json import loads

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/launches')
def launches():
    r = get('https://api.spacexdata.com/v4/launches/past')
    past_launches = loads(r.text)[::-1]
    return render_template('launches.html', past_launches=past_launches)

@app.route('/about')
def about():
    return render_template('about.html')