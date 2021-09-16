import pandas as pd
from skyfield.api import EarthSatellite, load, wgs84
from datetime import datetime


def get_data(url):
    # Collect TLE data from URL
    satellites = load.tle_file(url)
    print('Loaded', len(satellites), 'satellites')
    return satellites


def create_dataset(sat_name, url):
    # Creates a dataset stored in a csv file which includes the sat's name, lat, lon and elevation.

    satellites = get_data(url)

    # Set the time of the dataset e.g. ts.now() gives you the positioning data of the satellites now.
    ts = load.timescale()
    t = ts.now()

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    export_time = now.strftime("%d-%m-%Y")

    # Arrays to store cleaned data.
    name = []
    lat = []
    long = []
    el = []
    el_earth = []

    # Stores the Earths radius to allow the radius to be added to the elevation of the satellites
    earth_radius = 6378137

    # Use Skyfield to clean the TLE file and append the data to a column array.
    for sat in satellites:
        geometry = sat.at(t)
        subpoint = geometry.subpoint()
        latitude = subpoint.latitude.degrees
        longitude = subpoint.longitude.degrees
        elevation = subpoint.elevation.m

        name.append(sat.name)
        lat.append(latitude)
        long.append(longitude)
        el.append(elevation)
        el_earth.append(elevation + earth_radius)

    # Merge the cleaned columns into a dataframe
    sat_data = pd.DataFrame(
        {'Name': name, 'Latitude': lat, 'Longitude': long, 'Elevation': el, 'Earth Radius + Elevation': el_earth})

    # Write a csv file with the cleaned data.
    sat_data.to_csv(sat_name + " " + export_time + ".csv")

    print(sat_data)


# Dictionary of data set urls from Celestrak
sat_datasets = {
    "starlink": {
        "name": "Starlink",
        "url": 'https://celestrak.com/NORAD/elements/starlink.txt'
    },
    "geo_comms": {
        "name": "Geo Comms",
        "url": "https://celestrak.com/NORAD/elements/geo.txt"
    },
    "one_web": {
        "name": "OneWeb",
        "url": 'https://celestrak.com/NORAD/elements/oneweb.txt'
    },
    "galileo": {
        "name": "Galileo",
        "url": 'https://celestrak.com/NORAD/elements/galileo.txt'
    },
    "space_stations": {
        "name": "Space Stations",
        "url": 'https://celestrak.com/NORAD/elements/stations.txt'
    },
    "gps": {
        "name": "GPS",
        "url": 'https://celestrak.com/NORAD/elements/gps-ops.txt'
    },
    "active": {
        "name": "Active Satellites",
        "url": 'https://celestrak.com/NORAD/elements/active.txt'
    },
    "weather": {
        "name": "Weather",
        "url": 'https://celestrak.com/NORAD/elements/weather.txt'
    },
    "planet": {
        "name": "Planet Labs",
        "url": 'https://celestrak.com/NORAD/elements/planet.txt'
    },
    "glonass": {
        "name": "GLONASS Operational Satellites",
        "url": 'https://celestrak.com/NORAD/elements/glo-ops.txt'
    },
    "beidou": {
        "name": "Beidou",
        "url": 'https://celestrak.com/NORAD/elements/beidou.txt'
    },
    "geo-protected": {
        "name": "GEO Protected Zone",
        "url": '/Users/alexlong/Documents/Github/sat-map/data/geoprotectedzone.txt'
    },
    "fengyn-debris": {
        "name": "FENGYUN 1C Debris",
        "url": 'https://celestrak.com/NORAD/elements/1999-025.txt'
    },
    "iridium-debris": {
        "name": "IRIDIUM 33 Debris",
        "url": 'https://celestrak.com/NORAD/elements/iridium-33-debris.txt'
    },
    "cosmos-debris": {
        "name": "COSMOS 2251",
        "url": 'https://celestrak.com/NORAD/elements/cosmos-2251-debris.txt'
    }
}


# iridium-debris
name = sat_datasets.get("iridium-debris", {}).get("name")
url = sat_datasets.get("iridium-debris", {}).get("url")

create_dataset(name, url)


# fengyn-debris
name = sat_datasets.get("fengyn-debris", {}).get("name")
url = sat_datasets.get("fengyn-debris", {}).get("url")

create_dataset(name, url)


# cosmos-debris
name = sat_datasets.get("cosmos-debris", {}).get("name")
url = sat_datasets.get("cosmos-debris", {}).get("url")

create_dataset(name, url)


# %%
# geo-protected
name = sat_datasets.get("geo-protected", {}).get("name")
url = sat_datasets.get("geo-protected", {}).get("url")

create_dataset(name, url)


# beidou
name = sat_datasets.get("beidou", {}).get("name")
url = sat_datasets.get("beidou", {}).get("url")

create_dataset(name, url)


# glonass
name = sat_datasets.get("glonass", {}).get("name")
url = sat_datasets.get("glonass", {}).get("url")

create_dataset(name, url)


# planet
name = sat_datasets.get("planet", {}).get("name")
url = sat_datasets.get("planet", {}).get("url")

create_dataset(name, url)


# weather
name = sat_datasets.get("weather", {}).get("name")
url = sat_datasets.get("weather", {}).get("url")

create_dataset(name, url)


# active
name = sat_datasets.get("active", {}).get("name")
url = sat_datasets.get("active", {}).get("url")

create_dataset(name, url)


# Starlink
name = sat_datasets.get("starlink", {}).get("name")
url = sat_datasets.get("starlink", {}).get("url")

create_dataset(name, url)


# geo_comms
name = sat_datasets.get("geo_comms", {}).get("name")
url = sat_datasets.get("geo_comms", {}).get("url")

create_dataset(name, url)


# one_web
name = sat_datasets.get("one_web", {}).get("name")
url = sat_datasets.get("one_web", {}).get("url")

create_dataset(name, url)


# galileo
name = sat_datasets.get("galileo", {}).get("name")
url = sat_datasets.get("galileo", {}).get("url")

create_dataset(name, url)


# space_stations
name = sat_datasets.get("space_stations", {}).get("name")
url = sat_datasets.get("space_stations", {}).get("url")

create_dataset(name, url)


# gps
name = sat_datasets.get("gps", {}).get("name")
url = sat_datasets.get("gps", {}).get("url")

create_dataset(name, url)
