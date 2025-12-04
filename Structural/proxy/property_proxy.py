class Property:
    def __init__(self, value, name=''):
        self._name = name
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self._value == value:
            return
        self._value = value
        print(f'{self._name} changed to {self._value}')


class Creature:
    def __init__(self):
        self._speed = Property(10, 'speed')

    @property
    def speed(self):
        return self._speed.value

    @speed.setter
    def speed(self, value):
        self._speed.value = value

if __name__ == '__main__':
    c = Creature()
    c.speed = 12
    c.speed += 3
    x = c.speed
    print(x)