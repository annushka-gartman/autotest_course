number = 1
string = 'Hello'

def global_changes():
    """
    The function changes global variables and returns a new value
    :return: modified number and string
    """
    global number, string
    number = 5
    string = 'Hello, dear friend'
    return number, string

global_changes()

assert number == 5, 'Переменная number должна иметь значение 5'
assert string == 'Hello, dear friend', 'Переменная string должна иметь значение Hello, dear friend'
assert global_changes() == (5, 'Hello, dear friend')

print('Все ок')