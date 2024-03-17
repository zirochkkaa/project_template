# input.py

import pandas as pd

def input_from_console():
    return input("Будь ласка, введіть текст: ")

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def read_from_file_pandas(filename):
    return pd.read_csv(filename)
