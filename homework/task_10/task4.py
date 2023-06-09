import time


class TestClass:

    def test_summ(self):
        list_number = list(range(1, 10000000))
        assert sum(list_number) == 49999995000000

    def test_sleep(self):
        time.sleep(3)

    def test_unique(self, function_execution_time_fixture):
        time.sleep(1.111)
