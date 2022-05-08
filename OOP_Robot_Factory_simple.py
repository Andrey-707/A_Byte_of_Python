# Основы ООП. Robot Factory.
from colorama import init, Fore, Back, Style


init()

print(Fore.MAGENTA)
print("Program start")

print(Fore.YELLOW)
class Robot:
    '''Представляет робота с именем.'''
    population = 0 # переменная класса, содержит количество роботов

    def __init__(self, name):
        '''Инициализация данных.'''
        self.name = name
        print("(Инициализация {0})".format(self.name))

        Robot.population += 1 # при создании, робот добавляется (прибавляется) к переменной 'population'


    def __del__(self):
        '''Уничтожение.'''
        print("{0} уничтожается!".format(self.name))

        Robot.population -= 1 # при уничтожении, робот убирается (вычитается) из переменной 'population'

        if Robot.population == 0:
            print("{0} был последним.".format(self.name))
        else:
            print("Осталось работающих роботов {0:d}.".format( \
                Robot.population))


    def sayHi(self):
        '''Приветствие робота.

        Да, они это могут.'''
        print("Приветствую! Мои хозяева называют меня {0}.".format(self.name))


    def howMany():
        '''Выводит численность роботов.'''
        print("Сейчас роботов {0:d}.".format(Robot.population))

    howMany = staticmethod(howMany) # присваиваем функции howMany staticmethod без использования декоратора @


droid1 = Robot("R2-D2")
droid1.sayHi()
Robot.howMany()

droid2 = Robot("C-3PO")
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2

Robot.howMany()

# Вывод на печать текста строки документации для класса
print(Fore.WHITE)
print("\nВывод на печать текста строки документации для класса {0}:".format(str(Robot.__name__)))
print(Fore.YELLOW)
print(Robot.__doc__)

# Вывод на печать текста строки документации для методов класса
print(Fore.WHITE)
print("\nВывод на печать текста строки документации для методов класса {0}:".format(str(Robot.__name__)))
print(Fore.YELLOW)
print(Robot.sayHi.__doc__)
print(Robot.__del__.__doc__)
print(Robot.howMany.__doc__)


print(Fore.MAGENTA)
print("Program finish")

input()
