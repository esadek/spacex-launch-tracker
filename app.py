from flask import Flask, render_template, request
from requests import get
from json import loads

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', home_active='active')

@app.route('/launches')
def launches():
    r = get('https://api.spacexdata.com/v4/launches/past')
    past_launches = loads(r.text)[::-1]
    return render_template('launches.html', launches_active='active', past_launches=past_launches)

@app.route('/about')
def about():
    return render_template('about.html', about_active='active')

if __name__ == '__main__':
    app.run(debug=True)