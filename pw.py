# ! Python 3
# pw.py Программа для незащищенного хранения паролей

PASSWORDS = {'email': 'dfDFFG5!dfgg))-_', 'blog': 'dfDFFG5!dfgg))-_eR'}


import sys, pyperclip

if len(sys.argv) < 2:
    print('Использование: pw.py (имя учетной записи) - копирование пароля учетной записи')
    sys.exit()
account = sys.argv[1]  # первый аргумент коммандной строки это имя учетной записи

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для ' + account + ' скопирован в буфер.')
else:
    print('Учетная запись ' + account + ' отсутствует в списке.')
