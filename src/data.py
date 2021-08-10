from requests import get

NEXT_LAUNCH_URL = 'https://api.spacexdata.com/v4/launches/next'
LATEST_LAUNCH_URL = 'https://api.spacexdata.com/v4/launches/latest'
UPCOMING_LAUNCHES_URL = 'https://api.spacexdata.com/v4/launches/upcoming'
PAST_LAUNCHES_URL = 'https://api.spacexdata.com/v4/launches/past'

ROCKET_IDS = {
    '5e9d0d95eda69973a809d1ec': 'Falcon 9',
    '5e9d0d95eda69955f709d1eb': 'Falcon 1',
    '5e9d0d95eda69974db09d1ed': 'Falcon Heavy',
    '5e9d0d96eda699382d09d1ee': 'Starship'
}
LAUNCHPAD_IDS = {
    '5e9e4501f5090910d4566f83': 'VAFB SLC 3W',
    '5e9e4501f509094ba4566f84': 'CCSFS SLC 40',
    '5e9e4502f5090927f8566f85': 'STLS',
    '5e9e4502f5090995de566f86': 'Kwajalein Atoll',
    '5e9e4502f509092b78566f87': 'VAFB SLC 4E',
    '5e9e4502f509094188566f88': 'KSC LC 39A'
}


def replace_launch_ids(launch_data: dict) -> dict:
    """Return a dict with rocket and launchpad ids replaced by names.

    Parameters
    ----------
    launch_data : dict
        Launch data with rocket and launchpad ids.

    Returns
    -------
    revised_launch_launch : dict
        Launch data with rocket and launchpad names.
    """
    revised_launch_data = launch_data.copy()
    revised_launch_data['rocket'] = ROCKET_IDS[launch_data['rocket']]
    revised_launch_data['launchpad'] = LAUNCHPAD_IDS[launch_data['launchpad']]
    return revised_launch_data


def get_next_launch() -> dict:
    """Return a dict containing data about the next SpaceX launch.

    Returns
    -------
    dict
        Data about the next SpaceX launch.
    """
    return replace_launch_ids(get(NEXT_LAUNCH_URL).json())


def get_latest_launch() -> dict:
    """Return a dict containing data about the latest SpaceX launch.

    Returns
    -------
    dict
        Data about the latest SpaceX launch.
    """
    return replace_launch_ids(get(LATEST_LAUNCH_URL).json())


def get_upcoming_launches() -> list:
    """Return a list of dicts containing data about upcoming SpaceX launches.

    Returns
    -------
    launches : list
        Data about upcoming SpaceX launches.
    """
    launches = []
    for launch in get(UPCOMING_LAUNCHES_URL).json():
        launches.append(replace_launch_ids(launch))
    return launches


def get_past_launches() -> list:
    """Return a list of dicts containing data about past SpaceX launches.

    Returns
    -------
    launches : list
        Data about past SpaceX launches.
    """
    launches = []
    for launch in get(PAST_LAUNCHES_URL).json():
        launches.append(replace_launch_ids(launch))
    return launches
