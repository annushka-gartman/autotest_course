import math


class Segment:
    def __init__(self, x1y1, x2y2):
        self.x1y1 = x1y1
        self.x2y2 = x2y2

    def length(self):
        segment_length = math.sqrt(
            math.pow((self.x2y2[1] - self.x1y1[1]), 2) + math.pow((self.x2y2[0] - self.x1y1[0]), 2))
        return round(segment_length, 2)

    def x_axis_intersection(self):
        if (self.x1y1[1] * self.x2y2[1] < 0) or (self.x1y1[1] * self.x2y2[1] < 0):
            return True
        else:
            return False

    def y_axis_intersection(self):
        if (self.x1y1[0] * self.x2y2[0] < 0) or (self.x1y1[0] * self.x2y2[0] < 0):
            return
        else:
            return False


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]

test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
