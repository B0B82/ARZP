def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return 3*number + 1


print('Введите целое число!')
try:
    number1 = int(input())
    while True:
        number1 = collatz(number1)
        print('Число =', number1)
        if number1 == 1:
            break
except ValueError:
    print('Вы ввели не целое число!')




