from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

import os
import time
# backup файлов делать ТОЛЬКО ЧЕРЕЗ КОМАНДНУЮ СТРОКУ (cmd) !!!

print(Fore.WHITE)
print("Program start")

print(Fore.YELLOW)
# 1. Файлы и каталоги, КОТОРЫЙ НЕОБХОДИМО СКОПИРОВАТЬ, собираются в список.
source = ['"C:\\Users\\Андрей\\Documents\\Simple Sticky Notes"']
# Для имён, содержащих пробелы, необходимо использовать двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\\Backup_files\\Other_files' # КУДА НЕОБХОДИМО СКОПИРОВАТЬ.

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
# Если создать сейчас, то %Y%m%d%H%M%S - 20210816155621 - гггг,мм,дд,чч,мм,сс
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
	print('Резервная копия успешно создана в', target)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')

print(Fore.WHITE)
print("Program finish")

input()
