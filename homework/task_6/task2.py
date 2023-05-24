def global_function():
    msg = 1

    def local_function():
        nonlocal msg
        msg = 2
        return msg

    local_function()
    return msg


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')