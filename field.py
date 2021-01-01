import numpy as np


class Field:
    def __init__(self, screen, part_size, default_part_val=1000):
        self.part_size = part_size
        self._x_size = screen.get_rect().width // part_size
        self._y_size = screen.get_rect().height // part_size
        self._sectors = np.array([[default_part_val for i in range(self._x_size + 1)]
                                  for j in range(self._y_size + 1)])

    def get_value(self, rol, col):
        return self._sectors[rol][col]

    def set_value(self, rol, col, value):
        self._sectors[rol][col] = value

    def get_value_from_cords(self, x, y):
        return self._sectors[int(y // self.part_size)][int(x // self.part_size)]

    def set_value_from_cords(self, x, y, value):
        self._sectors[int(y // self.part_size)][int(x // self.part_size)] = value

    def get_field(self):
        return self._sectors
