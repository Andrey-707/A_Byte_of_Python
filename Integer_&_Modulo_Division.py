from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

print(Fore.WHITE)
print("Program start")

print(Fore.YELLOW)

# Деление числа по модулю (%).
print('Деление числа по модулю\n')
a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = float(a) % float(b)
#c = int(a) % int(b)
print(str(a)+ ' % ' + str(b) + ' = ' + str(c))

input()

# Целочисленное деление (//).
print('Целочисленное деление\n')
a = input('Введите первое число: ')
b = input('Введите второе число: ')
#c = float(a) // float(b)
c = int(a) // int(b)
print(str(a)+ ' // ' + str(b) + ' = ' + str(c))

print(Fore.WHITE)
print("Program finish")

input()