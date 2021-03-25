import mymodule
from mymodule import check_float_number
import geo_lib
from geo_lib import Figure


class FigureResult(Figure):
    
    def __init__(self, *args):
        self.fig_class = args[0]
        self.a = args[1]
        if len(args) == 4:
            self.b = args[2]
        if len(args) == 5:
            self.b = args[2]
            self.c = args[3]
        self.oper = args[-1]


def operation():
    while True:
        x = input('Что ищем?\n1. Периметр\n2. Площадь\n')
        if not x.isdigit():
            print('Ошибка. Попробуйте снова.')
            continue
        else:
            x = int(x)
        if x == 1:
            return 1
        elif x == 2:
            return 2
        else:
            print('Ошибка. Попробуйте снова.')
            continue


SELECTOR = {
    1: FigureResult.circle,
    2: FigureResult.square,
    3: FigureResult.rectangle,
    4: FigureResult.triangle,
    5: FigureResult.ball,
    6: FigureResult.sphere,
    7: FigureResult.cube,
    8: FigureResult.cuboid,
    9: FigureResult.triangular_pyramid,
    10: FigureResult.quadrangular_pyramid
    }


def main():
    while True:
        p1 = ''
        p2 = ''
        p3 = ''
        oper = ''
        fig_class = (input('''
                    Программа по вычислению: 
                    Периметра, площади и объема.
                    Примеры фигур:
                    Плоские:
                    1. Круг
                    2. Квадрат
                    3. Прямоугольник
                    4. Треугольник
                    Объемные:
                    5. Шар
                    6. Сфера
                    7. Куб
                    8. Прямоугольный параллелепипед
                    9. Правильная треугольная пирамида
                    10. Правильная Четырехугольная пирамида
                    Укажите Вашу фигуру:'''))
        if fig_class.isdigit():
            fig_class = int(fig_class)
        else:
            print('Недопустимое значение.')
            continue
        if fig_class < 1 or fig_class > 10:
            print('Фигуры с таким индексом нет в БД.')
            continue
        if fig_class == 1 or fig_class == 5 or fig_class == 6:
            p1 = input('Введите радиус:')
        if fig_class == 2 or fig_class == 7:
            p1 = input('Введите длину стороны:')
        if fig_class == 3:
            p1 = input('Введите длину 1 стороны:')
            p2 = input('Введите длину 2 стороны:')
        if fig_class == 4:
            oper = operation()
            if oper == 1:
                p1 = input('Введите длину 1 стороны:')
                p2 = input('Введите длину 2 стороны:')
                p3 = input('Введите длину 3 стороны:')
            elif oper == 2:
                p1 = input('Введите длину стороны:')
                p2 = input('Введите высоту:')
        if fig_class == 8:
            p1 = input('Введите длину 1 стороны:')
            p2 = input('Введите длину 2 стороны:')
            p3 = input('Введите высоту:')
        if fig_class == 9 or fig_class == 10:
            p1 = input('Введите длину стороны основания:')
            p2 = input('Введите высоту:')
        p1 = check_float_number(p1)
        if type(p1) != float:
            print(p1)
            continue
        if not p2 and not p3:
            SELECTOR.get(fig_class)(FigureResult(fig_class, p1, oper))
        if p2 and not p3:
            p2 = check_float_number(p2)
            if type(p2) != float:
                print(p2)
                continue
            SELECTOR.get(fig_class)(FigureResult(fig_class, p1, p2, oper))
        if p2 and p3:
            p2 = check_float_number(p2)
            if type(p2) != float:
                print(p2)
                continue
            p3 = check_float_number(p3)
            if type(p3) != float:
                print(p3)
                continue
            SELECTOR.get(fig_class)(FigureResult(fig_class, p1, p2, p3, oper))
        con = input('Продолжить (y/n)?')
        if con == 'y':
            continue
        else:
            break


main()
