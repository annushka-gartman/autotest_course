class PersonInfo:
    def __init__(self, fio: str, age: int, *unit):
        self.fio = fio
        self.age = age
        self.unit = unit

    def short_name(self):
        surname = f'{self.fio[self.fio.find(" ") +1 :]} {list(self.fio)[0]}.'
        return surname

    def path_deps(self):
        path = " --> ".join(self.unit)
        return path

    def new_salary(self):
        letters_dict = {}
        for work in self.unit:
            for letter in work:
                if letter in letters_dict:
                    letters_dict[letter] += 1
                else:
                    letters_dict[letter] = 1
        most_common = dict(sorted(letters_dict.items(), key=lambda item: item[1])[-3:])
        salary = 1337 * self.age * sum(most_common.values())
        return salary


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], '{} = {}'.format(d(), test_data[i])
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')