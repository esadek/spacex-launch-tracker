from flask import Flask, render_template, request
from requests import get
from json import loads

application = Flask(__name__)

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


@application.route('/')
@application.route('/home')
def home():
    next_launch = get('https://api.spacexdata.com/v4/launches/next')
    latest_launch = get('https://api.spacexdata.com/v4/launches/latest')
    data = {
        'next launch': loads(next_launch.text),
        'latest launch': loads(latest_launch.text),
        'rockets': rockets,
        'launchpads': launchpads
    }
    return render_template('index.html', data=data)


@application.route('/upcoming')
def upcoming():
    upcoming_launches = get('https://api.spacexdata.com/v4/launches/upcoming')
    data = {
        'upcoming launches': loads(upcoming_launches.text),
        'rockets': rockets,
        'launchpads': launchpads
    }
    return render_template('upcoming.html', data=data)


@application.route('/past')
def past():
    past_launches = get('https://api.spacexdata.com/v4/launches/past')
    data = {
        'past launches': loads(past_launches.text)[::-1],
        'rockets': rockets,
        'launchpads': launchpads
    }
    return render_template('past.html', data=data)


@application.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    application.run()
