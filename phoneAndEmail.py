# ! python3
#
# phoneAndEmail.py - находит все номера и емайлы в буфере обмена

import pyperclip, re
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?              # территориальный код
#     (\s|-|\.)?                      # разделитель
#     (\d{3})                         # первые три цифры
#     (\s|-|\.)                       # разделитель
#     (\d{4})                         # последние 4 цифры
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?  # добавочный номер
#     )''', re.VERBOSE)
phoneRegex = re.compile(r'((\+)?\b(8|38)?(0[\d]{2}))([\d-]{5,8})([\d]{2})')  # для украинских мобильных телефонов
# TODO: создать регулярное выражение для почты
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# TODO: найти соответствия в тексте, содержащемся в буфере обмена
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups(1), groups(3), groups(5)])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# TODO: скопировать результаты в буфер обмена
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопированно в буфер обмена')
    print('\n'.join(matches))
else:
    print('Телефон и емайл не обнаружены')
