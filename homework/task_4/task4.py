def multiplication_chain(num):
    count_multy = 0
    while num > 9:
        multi = 1
        while not num == 0:
            remainder = num % 10
            multi = multi * remainder
            num = num // 10
        num = multi
        count_multy += 1
    return count_multy

data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    3, 0, 2, 4, 1, 4
]

for i, d in enumerate(data):
    assert multiplication_chain(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
