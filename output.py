def output_to_console(text):
    """
    Виводить текст у консоль.

    Parameters:
        text (str): текст, який потрібно вивести.
    """
    print(text)

def write_to_file(filename, text):
    """
    Записує текст до файлу за допомогою вбудованих можливостей Python.

    Parameters:
        filename (str): шлях до файлу, де потрібно зберегти текст.
        text (str): текст для запису у файл.
    """
    with open(filename, 'w') as file:
        file.write(text)
