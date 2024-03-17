import pandas as pd

def input_from_console():
    """
    Запитує текст у користувача через консоль.

    Returns:
        str: текст, введений користувачем.
    """
    return input("Будь ласка, введіть текст: ")

def read_from_file(filename):
    """
    Читає вміст файлу за допомогою вбудованих можливостей Python.

    Parameters:
        filename (str): шлях до файлу, який потрібно прочитати.

    Returns:
        str: вміст файлу у вигляді рядка.
    """
    with open(filename, 'r') as file:
        return file.read()

def read_from_file_pandas(filename):
    """
    Читає вміст файлу за допомогою бібліотеки pandas. Призначено для читання файлів CSV.

    Parameters:
        filename (str): шлях до файлу CSV, який потрібно прочитати.

    Returns:
        DataFrame: вміст файлу у вигляді pandas DataFrame.
    """
    return pd.read_csv(filename)
