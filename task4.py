def scrabble(word):
    """
    Function to count the number of points received per word
    :param word: Line with word
    :return points: Number of points per word
    """
    letter = dict([('авеёинорст', 1), ('дклмпу', 2), ('бгья', 3), ('йы', 4),
                   ('жзхцч', 5), ('фшэю', 8), ('щ', 10), ('ъ', 15)])
    list_points = [key for i in word for value, key in letter.items() if i in value]
    points = sum(list_points)
    return points

data = ["курс", 'авеинорстё', 'дклмпеу', 'бгья', 'йы', 'жзхцч', 'фшэю', 'щъ', "карабасбарабас", "околоводопроводного",
        "еженедельное", 'эхоэнцефалограф', 'человеконенавистничество', 'делопроизводительница']

test_data = [6, 10, 13, 12, 8, 25, 32, 25, 21, 26, 20, 54, 34, 36]

for i, d in enumerate(data):
    assert scrabble(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')