import argparse
import logging
from datetime import datetime


class NegativeValueError(ValueError):
    pass


logging.basicConfig(filename='rectangle.log', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


class Rectangle:

    def __init__(self, width, height=None):
        logger.info(f'{datetime.now()}: Создается объект класса Rectangle c параметрами width={width} height={height}')
        if width <= 0:
            logger.error(f'{datetime.now()}: Вызвано исключение NegativeValueError для параметра width = {width}')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(f'{datetime.now()}: Вызвано исключение NegativeValueError для параметра height = {height}')
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        logger.info(f'{datetime.now()}: Запрос на получение значение параметра width. Результат width={self._width}')
        return self._width

    @width.setter
    def width(self, value):
        logger.info(f'{datetime.now()}: Изменение значения параметра width={self.width}')
        if value > 0:
            self._width = value
            logger.info(f'{datetime.now()}: Значение параметра width изменено на значение {value}')
        else:
            logger.error(f'{datetime.now()}: Вызвано исключение NegativeValueError при попытке изменить параметр '
                         f'width={self.width} на значение = {value}')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        logger.info(f'{datetime.now()}: Запрос на получение значение параметра height. Результат height={self._height}')
        return self._height

    @height.setter
    def height(self, value):
        logger.info(f'{datetime.now()}: Изменение значения параметра height={self.height}')
        if value > 0:
            self._height = value
            logger.info(f'{datetime.now()}: Значение параметра height изменено на значение {value}')
        else:
            logger.error(f'{datetime.now()}: Вызвано исключение NegativeValueError при попытке изменить параметр '
                         f'height={self.height} на значение = {value}')
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        logger.info(f'{datetime.now()}: Вычисление периметра прямоугольника. '
                    f'width={self._width} height={self._height}: Результат {2 * (self._width + self._height)}')
        return 2 * (self._width + self._height)

    def area(self):
        logger.info(f'{datetime.now()}: Операция вычисление площади прямоугольника. '
                    f'width={self._width} height={self._height}: Результат {self._width * self._height}')
        return self._width * self._height

    def __add__(self, other):
        logger.info(f'Операция сложения двух прямоугольников')
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        logger.info(f'Результат сложения прямоугольника Rectangle({self._width}, {self._height}) и '
                    f'прямоугольника Rectangle({other._width}, {other._height}): Rectangle({width}, {height})')
        return Rectangle(width, height)

    def __sub__(self, other):
        logger.info(f'Операция вычитания двух прямоугольников')
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        logger.info(f'Результат вычитания прямоугольника Rectangle({self._width}, {self._height}) и '
                    f'прямоугольника Rectangle({other._width}, {other._height}): Rectangle({width}, {height})')
        return Rectangle(width, height)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Class Rectangle')
    parser.add_argument('-width', metavar='width', type=int,
                        help='enter the width parameter for the rectangle')
    parser.add_argument('-height', metavar='height', type=int,
                        help='enter the height parameter for the rectangle', default=1)
    args = parser.parse_args()
    r1 = Rectangle(args.width, args.height)
    print(r1.perimeter())
