import math
print('Введите интересующую вас операцию: \n1 - Сложение \n2 - Вычитание \n3 - Умножение \n4 - Деление \n5 - Возведение в степень \n6 - Логарифм \n7 - Округление в большую или меньшую сторону до N знака после запятой')
x = (input('Введите цифру операции \n>>> '))
if x == '1':
    a = int(input("Давай, вводи первое число: "))
    b = int(input("Давай, вводи второе число: "))
    print(f'{a}+{b}={a+b}')
elif  x == '2':
    a = int(input("Давай, вводи первое число: "))
    b = int(input("Давай, вводи второе число: "))
    print(f'{a}-{b}={a-b}')
elif x == '3':
    a = int(input("Давай, вводи первое число: "))
    b = int(input("Давай, вводи второе число: "))
    print(f'{a}*{b}={a*b}')
elif x == '4':
    a = int(input("Давай, вводи числитель: "))
    b = int(input("Давай, вводи знаменатель: "))
    if b == 0:
        print("На ноль делить бессмысленно")
    else:
        print(f'{a}/{b}={a/b}')
elif x == '5':
    a = int(input("Давай, вводи первое число: "))
    b = int(input("Давай, вводи степень, в которую надо возводить: "))
    print(a, '^', b, '=', a**b)
elif x == '6':
    a = int(input("Давай, вводи основание логарифма: "))
    b = int(input("Давай, вводи второе число: "))
    print(math.log(b, a))
elif x == '7':
    zad = int(input('Вводи задание: округление до большего - 1 / округление до меньшего - 2 \n >>> '))
    x = float(input('Вводи число \n >>> '))
    dig = int(input('Вводи колчество знаков после запятой \n >>> '))
    def ocr(zad, x, dig):
        if zad == 1:
            otv = (math.ceil(x*(10**dig)))/(10**dig)
        else:
            otv = (math.floor(x*(10**dig)))/(10**dig)
        return otv
    print(ocr(zad, x, dig))
else:
    print('Такой операции в списке нет')
