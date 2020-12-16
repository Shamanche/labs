FILENAME = 'output.txt'

def p(n, x):
    if n == 0:
        return float(1) # P0 = 1
    elif n == 1:
        return x # P1 = x
    else:
        return (((2 * n)-1)*x * p(n-1, x)-(n-1) *  p(n-2, x))/n

try:
    n = int(input('Введите целое число N: '))
    x = float(input('Введите вещественное число X:'))
except ValueError:
    print ('Ошибка ввода данных')
    exit(0) # завершение программы

result = []
for i in range(n + 1):
    result.append(str(p(i,x)))

with open(FILENAME, 'w') as f:
    raw = ' '.join(result)
    f.write(raw)
    print('Файл {} создан.'.format(FILENAME))





