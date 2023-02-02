import json
import os

from blaseball_mike.utils import csv_format, get_gameday_start_time
from os.path import join, basename, dirname
from urllib.request import urlopen

# Define dirnames and url snippets
processed_dir = 'processed'
data_dir = 'raw'

url_head = "https://api2.sibr.dev/chronicler/v0/entities?"
kind_player = "kind=player&at="
kind_team = "kind=team&at="

current_dir = dirname(__file__)

processed_dir = join(current_dir, processed_dir)
data_dir = join(current_dir, data_dir)


def download_data(start_season=1, end_season=-1):
    """Downloads stats from chronicler and saves it to the system

    Keyword arguments:
        start_season: season to begin pulling stats from.
        end_season: season to end pulling stats from. Setting to -1 defaults
        to the most recent season.
    """

    if end_season != -1 and start_season > end_season:
        raise ValueError("End season cannot be less than starting season")

    print("Downloading Data")

