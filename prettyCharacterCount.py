import pprint


message = 'It was a bright cold day in april and the clocks the striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
