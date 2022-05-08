# Основы ООП. Robot Factory.
from random import uniform
from time import sleep
from rich import print
from rich.prompt import Confirm
from progress.bar import IncrementalBar


print("[bold magenta]Programm start[/]")

class Robot:
    '''Представляет робота и его серию.'''
    population = 0 # переменная класса, содержащая количество роботов

    def __init__(self, name):
        '''Инициализация данных.'''
        self.name = name
        print("(Инициализация [bold cyan]{0}[/])".format(self.name))

        Robot.population += 1 # при создании, робот добавляется (прибавляется) к переменной 'population'


    def __del__(self):
        '''Уничтожение.'''
        print("\n[bold cyan]{0}[/] уничтожается!".format(self.name))

        Robot.population -= 1 # при уничтожении, робот убирается (вычитается) из переменной 'population'

        if Robot.population == 0:
            print("[bold cyan]{0}[/] был последним [bold cyan]функционирующим роботом[/].".format(self.name))
        else:
            print("В остатке " +
                str(Robot.choose_plural(Robot.population, (
                    "[bold cyan]функционирующий робот[/]",
                    "[bold cyan]функционирующих робота[/]",
                    "[bold cyan]функционирующих роботов[/]"))
                ) + ".")


    def sayHi(self):
        '''Приветствие робота.

        Да, они это могут.'''
        print("Приветствую! Мои создатели назвали меня [bold cyan]{0}[/].".format(self.name))


    @staticmethod
    def howMany():
        '''Выводит численность роботов.'''
        print("\nСейчас у нас " +
            str(Robot.choose_plural(Robot.population, ("робот", "робота", "роботов")))
            + ".\n")

    # howMany = staticmethod(howMany) # присваиваем функции howMany staticmethod без использования декоратора @


    def choose_plural(amount, variants):
        '''Выбор формы существительного.'''    
        if amount % 10 == 1 and amount % 100 != 11:
            variant = 0
        elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
            variant = 1
        else:
            variant = 2
        return "{} {}".format(amount, variants[variant])


    def do_work():
        '''Выполнение работы.'''        
        my_list = range(10)
        bar = IncrementalBar("Processing...", max=len(my_list))

        for i in my_list:
            bar.next()
            sleep(uniform(0.1, 1)) # random.uniform(a, b) дает случайное число с плавающей запятой в диапазоне [a, b]

        bar.finish()


Robot.howMany()

Robot1 = Robot("T-800")
Robot1.sayHi()
Robot.howMany()

Robot2 = Robot("T-900")
Robot2.sayHi()
Robot.howMany()

Robot3 = Robot("T-1000")
Robot3.sayHi()
Robot.howMany()

Robot4 = Robot("T-X")
Robot4.sayHi()
Robot.howMany()

print("Роботы выполняют свою работу.\n")
Robot.do_work()

print("\n[white]Роботы завершили свою работу. Давайте уничтожим их.[/]")

Confirm.ask("\nЗапустить процедуру уничтожения?")
del Robot1
Confirm.ask("\nЗапустить процедуру уничтожения?")
del Robot2
Confirm.ask("\nЗапустить процедуру уничтожения?")
del Robot3
Confirm.ask("\nЗапустить процедуру уничтожения?")
del Robot4

Robot.howMany()

print("[bold magenta]Programm finish[/]")

input()