# SpaceX Launch Tracker

[![Continuous Integration Status](https://img.shields.io/github/workflow/status/esadek/spacex-launch-tracker/Continuous%20Integration)](https://github.com/esadek/spacex-launch-tracker/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/esadek/spacex-launch-tracker)](https://github.com/esadek/spacex-launch-tracker/blob/main/LICENSE)

SpaceX Launch Tracker is an open source web application for exploring data about upcoming and past [SpaceX](https://www.spacex.com/) launches. It was created by [Emil Sadek](https://emilsadek.com) using [Flask](https://github.com/pallets/flask) and [Bootstrap](https://github.com/twbs/bootstrap), with data from [SpaceX-API](https://github.com/r-spacex/SpaceX-API).

[https://www.spacexlaunchtracker.com/](https://www.spacexlaunchtracker.com/)

## Installation

Clone repository and change directory:
```
$ git clone https://github.com/esadek/spacex-launch-tracker.git
$ cd spacex-launch-tracker
```
Create and activate virtual environment:
```
$ python3 -m venv env
$ source env/bin/activate
```
Install required packages:
```
$ pip install -r requirements.txt
```
Run app:
```
$ python src/app.py
```

## Testing
Run all tests with [pytest](https://docs.pytest.org/en/stable/):
```
$ pytest
```

## License

[MIT](https://github.com/esadek/spacex-launch-tracker/blob/main/LICENSE)