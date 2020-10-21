birthdays = {'Bob': '18 nov', 'Sveta': '8 oct', 'Kristina': '13 june'}

while True:
    print('Enter a name: (blanc to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name], ' is the birthday of ', name)
    else:
        print('I don\'t have information of ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthdays database updated!')
