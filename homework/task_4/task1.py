type_triangle = [
    "Равносторонний",
    "Равнобедренный",
    "Обычный",
    "Не треугольник"
]

def which_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (c + b > a):
        if (a == b) and (b == c):
            return type_triangle[0]
        elif (a != b) and (a != c) and (b != c):
            return type_triangle[2]
        else:
            return type_triangle[1]
    else:
        return type_triangle[3]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник"
]

data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3)
]

for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')