# ! python3
#
# bulletPointAdapter.py - добавляет макеты википедии в начало каждой сточки текста из буфера обмена

import pyperclip

text = pyperclip.paste()


# TODO: разделить строки и добаввит звездочки
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
