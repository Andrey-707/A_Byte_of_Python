from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.WHITE)
print("Program start")

print(Fore.YELLOW)
string1 = "Топот"
string1 = string1.lower()
# print(string1)
string2 = string1[::-1]
# print(string2)

if string2 == string1:
	print(Fore.GREEN)
	print("Полиндром")
else:
	print(Fore.RED)
	print("Нет, это не палиндром")

print(Fore.WHITE)
print("Program finish")

input()
