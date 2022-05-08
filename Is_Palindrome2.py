from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.WHITE)
print("Program start")

print(Fore.YELLOW)

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Введите текст: ")
something = something.lower()

if (is_palindrome(something)):
    print(Fore.GREEN)
    print("Полиндром")
else:
    print(Fore.RED)
    print("Нет, это не палиндром")

print(Fore.WHITE)
print("Program finish")

input()
