from flask import Flask, render_template
from requests_cache import install_cache

from data import (get_next_launch, get_latest_launch, get_upcoming_launches,
                  get_past_launches)

CACHE_DURATION_SECONDS = 3600
install_cache(expire_after=CACHE_DURATION_SECONDS)

app = Flask(__name__)


@app.route('/')
def home() -> str:
    context = {
        'next_launch': get_next_launch(),
        'latest_launch': get_latest_launch()
    }
    return render_template('index.html', context=context)


@app.route('/upcoming')
def upcoming() -> str:
    context = {'upcoming_launches': get_upcoming_launches()}
    return render_template('upcoming.html', context=context)


@app.route('/past')
def past() -> str:
    context = {'past_launches': get_past_launches()[::-1]}
    return render_template('past.html', context=context)


@app.route('/about')
def about() -> str:
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
