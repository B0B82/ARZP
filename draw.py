import copy

grid = [['.', '.', '.', '.', '.', '.', ],
        ['.', 'o', 'o', '.', '.', '.', ],
        ['o', 'o', 'o', 'o', '.', '.', ],
        ['o', 'o', 'o', 'o', 'o', '.', ],
        ['.', 'o', 'o', 'o', 'o', 'o', ],
        ['o', 'o', 'o', 'o', 'o', '.', ],
        ['o', 'o', 'o', 'o', '.', '.', ],
        ['.', 'o', 'o', '.', '.', '.', ],
        ['.', '.', '.', '.', '.', '.', ], ]

grid_copy = copy.deepcopy(grid)
# print(len(grid_copy))
k = 0
while True:
    for i in grid_copy:
        print(i[k], end='')
    print('')
    k += 1
    if k == len(grid_copy):
        break


