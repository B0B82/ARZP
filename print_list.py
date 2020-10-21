spam = ['apples', 'bananas', 'tofu', 'cats']
x = [1, 2, 3]

def printList(li):
    print('In your list: ', end='')
    for i in li:
        print(i, end='')

        if len(li) - 2 >= li.index(i):
            if len(li) - 2 == li.index(i):
                print(' and ', end='')
                continue
            print(', ', end='')




printList(spam)
print('')
printList(x)