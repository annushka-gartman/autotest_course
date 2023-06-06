import datetime
import time


def func_log(file_log='log.txt'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_log, 'a', encoding='utf-8') as log_file:
                res = func(*args, **kwargs)
                data_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
                log_file.write('{} вызвана {}\n'.format(func.__name__, data_time))
            return res
        return wrapper
    return decorator


@func_log()
def func1():
    time.sleep(5)


@func_log(file_log='func2.txt')
def func2():
    time.sleep(5)


func1()
func2()
func1()
func1()