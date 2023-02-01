import os

from os.path import join, basename, dirname

processed_dir = 'processed'
data_dir = 'raw'

current_dir = dirname(__file__)

processed_dir = join(current_dir, processed_dir)
data_dir = join(current_dir, data_dir)


def download_data():
    print("Downloading Data")

