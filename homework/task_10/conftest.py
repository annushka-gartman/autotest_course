import pytest
import time
import datetime


@pytest.fixture(scope='class', autouse=True)
def function_call_time_fixture():
    print('Время начала выполнения тестов: {}\n'.format(datetime.datetime.now().strftime("%d.%m %H:%M:%S")))
    yield
    print('\nВремя окончания выполнения тестов: {}'.format(datetime.datetime.now().strftime("%d.%m %H:%M:%S")))


@pytest.fixture()
def function_execution_time_fixture():
    start_time_test = time.time()
    yield
    end_time_test = time.time()
    print('\nВремя выполнения теста: {}'.format(end_time_test - start_time_test))
