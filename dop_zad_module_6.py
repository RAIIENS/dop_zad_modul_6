# Дополнительное практическое задание по модулю: "Наследование классов."
#
# Начнём реализацию классов Figure, Circle, Triangle и Cube, соответствующих нашему заданию.
# Многие атрибуты и методы должны будут инкапсулированны и для них должны будут написаны
# интерфейсы взаимодействия (методы) - геттеры и сеттеры.
# Импортируем математику:
import math
# Создаём класс Figure,который содержит общие для всех фигур атрибуты и методы. Он будет
# являться родительским классом для Circle, Triangle и Cube.
class Figure:
# Из ТЗ имеем, что атрибуты класса Figure: sides_count = 0
# Записываем атрибут класса Figure
    sides_count = 0
# Инициализация объекта Figure
    def __init__(self, color=(0, 0, 0), *sides):
# Проверяем корректность сторон и цвета, если всё некорректно, устанавливаем значение по умолчанию
# Атрибут(инкапсулированный): __sides(список сторон (целые числа))
# Если проверка __is_valid_sides прошла успешно стороны преобразуются в список list(sides)
# и присваиваются атрибуту self.__sides.
# Иначе, атрибуту self.__sides присваивается список, состоящий из self.sides_count элементов,
# каждый из которых равен 1.
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
# Атрибут(инкапсулированный): __color(список цветов в формате RGB)
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
# Атрибут(публичный): filled(закрашенный, bool)
        self.filled = self.__is_filled()  # Устанавливает значение атрибута filled.

# Метод для получения цвета
    def get_color(self):
# Метод get_color, возвращает список RGB цветов.
        return self.__color

# Внутренний метод для проверки корректности цвета
    def __is_valid_color(self, r, g, b):
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность
# переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа
# в диапазоне от 0 до 255 (включительно).
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

# Метод для установки нового цвета
    def set_color(self, r, g, b):
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color
# на соответствующие значения, предварительно проверив их на корректность.
# Если введены некорректные данные, то цвет остаётся прежним.
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = self.__is_filled()

    def __is_filled(self):
# Проверяет, установлен ли цвет фигуры в значение, отличное от (0, 0, 0).
        return self.__color != [0, 0, 0]

# Внутренний метод для проверки корректности сторон
    def __is_valid_sides(self, *sides):
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True
# если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False -
# во всех остальных случаях.
# Метод __is_valid_sides проверяет, что все стороны являются положительными целыми числами
# и их количество len(sides) совпадает с sides_count.
        return all(isinstance(s, int) and s > 0 for s in sides) and len(sides) == self.sides_count

# Метод для получения сторон
    def get_sides(self):
# Метод get_sides возвращает значение атрибута __sides.
        return self.__sides

# Метод для получения периметра (суммы сторон)
    def __len__(self):
# Метод __len__ возвращает периметр фигуры.
        return sum(self.__sides)

# Метод для установки новых сторон
    def set_sides(self, *new_sides):
# Метод set_sides(self, *new_sides) принимает новые стороны, если их количество не равно sides_count,
# то не изменяет, в противном случае - меняет.
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


# Класс Circle (Круг), наследуемый от Figure
class Circle(Figure):
# Атрибут класса Circle: sides_count = 1
    sides_count = 1  # Длина окружности.

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
# Если количество сторон не соответствует ожиданиям, устанавливаем значение по умолчанию
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(1)
# Расчет радиуса: Радиус = Длина_окружности / (2 * 3,14)
# Атрибут __radius, рассчитывается исходя из длины окружности (одной единственной стороны).
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_radius(self):
        return self.__radius

# Метод для вычисления площади круга: Площадь_круга = 3,14 * Радиус ^ 2
    def get_square(self):
# Метод get_square возвращает площадь круга (можно рассчитать как через длину,
# так и через радиус).
        return math.pi * (self.__radius ** 2)


# Класс Triangle (треугольник), наследуемый от Figure
class Triangle(Figure):
# Атрибут класса Triangle: sides_count = 3
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
# Если количество сторон не соответствует ожиданиям, устанавливаем значение по умолчанию
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))
# Расчет высоты
# Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника).
        self.__height = self.__calculate_height()

# Метод для получения высоты треугольника
    def get_height(self):
        return self.__height

# Внутренний метод для вычисления высоты треугольника по формуле Герона.
    def __calculate_height(self):
# Стороны треугольника
        first, second, third = self.get_sides()
# print("first, second, third", first, second, third)
# Полупериметр: half_of_perimeter
        half_of_per = sum([first, second, third]) / 2
# Площадь треугольника
        area = math.sqrt(half_of_per * (half_of_per - first) * (half_of_per - second) * (half_of_per - third))
#  Метод __calculate_height возвращает высоту треугольника:
#  Высота = 2 * Площадь_треугольника / Основание
        return 2 * area / first

# Метод для вычисления площади треугольника: Площадь_треугольника = 0,5 * Основание * Высота
    def get_square(self):
# Метод get_square возвращает площадь треугольника.
        first, _, _ = self.get_sides()
        return 0.5 * first * self.__height


# Класс Cube (Куб), наследуемый от Figure
class Cube(Figure):
# Атрибут класса Cube: sides_count = 12
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)
# Если количество сторон не соответствует ожиданиям, устанавливаем значение по умолчанию
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))

# Метод для вычисления объема куба
    def get_volume(self):
        side_length = self.get_sides()[0]
# Метод get_volume, возвращает объём куба.
        return side_length ** 3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # Вывод: [55, 66, 77]

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # Вывод: [222, 35, 130]

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # Вывод: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # Вывод: [15]

# Проверка периметра (длины окружности)
print(len(circle1))  # Вывод: 15

# Проверка объёма куба
print(cube1.get_volume())  # Вывод: 216


# ДОПОЛНИТЕЛЬНО:
# Дополнительные,(свои) проверки работы методов объектов каждого класса в отдельности:

print(circle1.get_sides())
circle1.set_sides(10)
print(circle1.get_sides())
print(len(circle1))
print(circle1.get_square())
print("circle1.get_radius()", circle1.get_radius())
circle1.set_color(128, 64, 32)
print("128, 64, 32", circle1.get_color())

triangle1 = Triangle((200, 200, 100), 4, 5, 3)
print(triangle1.get_sides())
print(len(triangle1))
print(triangle1.get_height())
print("triangle1.get_square", triangle1.get_square())
triangle1.set_sides(3, 4, 5)
print(triangle1.get_sides())
triangle1.set_color(128, 64, 32)
print("128, 64, 32", triangle1.get_color())

cube2 = Cube((254, 254, 254), 13)
print(cube2.get_sides())
print(len(cube2))
print("get_volume", cube2.get_volume())
cube2.set_sides(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
print(cube2.get_sides())
cube2.set_color(16, 32, 64)
print("16, 32, 64", cube2.get_color())

print(Figure.mro())
print(Circle.mro())
print(Triangle.mro())
print(Cube.mro())