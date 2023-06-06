# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

import re

with open('test_file/task1_data.txt', encoding='utf-8') as task1_data:
    list_lines = task1_data.readlines()
    new_txt = ''
    for items in list_lines:
        new_txt += re.sub("[0-9]", "", items)

with open('test_file/task1_answer.txt', mode='w', encoding='utf-8') as result:
    result.write(new_txt)

with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном{},{}".format(answer, ethalon)
print('Всё ок')