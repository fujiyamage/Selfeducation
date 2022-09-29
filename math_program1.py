#Программа  вычисляет:
#площадь круга;
#длину окружности;
#площадь прямоугольника;
#периметр прямоугольника.

import  circle
import  rectangle

#Константы для элементов с меню

AREA_CIRCLE = 1
CIRCUMFERENCE_CIRCLE = 2
AREA_RECTANGLE = 3
PERIMETR_RECTANGLE = 4
QUIT = 5

def main():
    choice = 0

    while choice != QUIT:
        display_menu()

        choice = int(input("Выберите пункт меню: "))
        if choice == AREA_CIRCLE:
            radius = float(input("Введите радиус окружности: "))
            print("Площадь круга равна", circle.area(radius),"см")
        elif choice == CIRCUMFERENCE_CIRCLE:
            radius = float(input("Введите радиус окружности: "))
            print("Длина круга равна", circle.circumference(radius), "см")
        elif choice == AREA_RECTANGLE:
            width = float(input("Введите ширину прямоугольника: "))
            length = float(input("Введите длину прямоугольника: "))
            print("Площадь прямоугольника равна", rectangle.area(width, length) , "см")
        elif choice == AREA_RECTANGLE:
            width = float(input("Введите ширину прямоугольника: "))
            length = float(input("Введите длину прямоугольника: "))
            print("Площадь прямоугольника равна", rectangle.perimetr(width, length) , "см")
        elif choice == QUIT:
            print("Завершение программы")
        else:
            print("Ошибка ввода. Выберите пункт из меню")

def display_menu():
    print("=" * 25)
    print("МЕНЮ")
    print("Площадь круга ||", AREA_CIRCLE)
    print("Длина круга ||", CIRCUMFERENCE_CIRCLE)
    print("Площадь прямоугольника ||", AREA_RECTANGLE)
    print("Периметр прямоугольника ||", PERIMETR_RECTANGLE)
    print("Выход ||", QUIT)
    print("=" * 25)

main()
