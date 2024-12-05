while True:
    num = input('Введите количество гостей: ')
    if num.isdigit() or (num[0] in '-' and num[1:].isdigit()): # проверка на ввод числа даже отрицательного
        num = int(num)
        break
    else:
        print("Введено не число, попробуйте заново")

if num < 20:
    print("Дом")
elif 20 <= num <= 50:
    print("Кафе")
else:
    print("Ресторан")

