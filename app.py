from flask import Flask, render_template, request
from requests import get
from json import loads

app = Flask(__name__)

active = 'active'
rockets = {
    '5e9d0d95eda69955f709d1eb': 'Falcon 1',
    '5e9d0d95eda69973a809d1ec': 'Falcon 9',
    '5e9d0d95eda69974db09d1ed': 'Falcon Heavy',
    '5e9d0d96eda699382d09d1ee': 'Starship'
}
launchpads = {
    '5e9e4501f5090910d4566f83': 'VAFB SLC 3W',
    '5e9e4501f509094ba4566f84': 'CCSFS SLC 40',
    '5e9e4502f5090927f8566f85': 'STLS',
    '5e9e4502f5090995de566f86': 'Kwajalein Atoll',
    '5e9e4502f509092b78566f87': 'VAFB SLC 4E',
    '5e9e4502f509094188566f88': 'KSC LC 39A'
}

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', home_active=active)

@app.route('/past')
def launches():
    r = get('https://api.spacexdata.com/v4/launches/past')
    past_launches = loads(r.text)[::-1]
    return render_template(
        'past.html',
        past_active=active,
        past_launches=past_launches,
        rockets=rockets,
        launchpads=launchpads
    )

@app.route('/about')
def about():
    return render_template('about.html', about_active=active)

if __name__ == '__main__':
    app.run(debug=True)