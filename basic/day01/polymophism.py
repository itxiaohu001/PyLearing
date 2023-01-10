class Pet(object):
    def __init__(self, nickname):
        self._nickname = nickname

    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂')]
    for p in pets:
        p.make_voice()


if __name__ == '__main__':
    main()
