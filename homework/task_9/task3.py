with open('test_file/task_3.txt') as task_3:
    list_price = task_3.read().split('\n')
    sum_price = 0
    list_sum_price = []
    for item in list_price:
        if item != '':
            sum_price = sum_price + int(item)
        else:
            list_sum_price.append(sum_price)
            sum_price = 0
list_sum_price.sort()
three_most_expensive_purchases = sum(list_sum_price[-3:])

assert three_most_expensive_purchases == 202346