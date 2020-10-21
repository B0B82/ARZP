tableData = [['apples', 'oranges', 'cherries', 'banana', 'lemon'],
             ['Alice', 'Bob', 'Alex', 'Dan'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    tmp = []
    max_len = 0
    for i in table:
        size = 0
        for k in i:
            if size < len(k):
                size = len(k)
        tmp.append(size)
    for i in table:
        if max_len < len(i):
            max_len = len(i)
    for i in range(max_len):
        for k in table:
            try:
                print(k[i].rjust(tmp[table.index(k)] + 1), end='')
            except IndexError:
                print('-'.rjust(tmp[table.index(k)] + 1), end='')
        print('')


printTable(tableData)
