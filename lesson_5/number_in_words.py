# объявление функции
def number_to_kop(num):
    zero_to_nineteen = ['ноль', 'одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
                        'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
                        'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = [0,1,'двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
    if 0 <= num <= 19:
        return zero_to_nineteen[num]
    elif 20 <= num < 100:
        if num % 10 == 0:
            return tens[num // 10]
        word = tens[num//10] + ' ' + zero_to_nineteen[num%10]
        return word


def number_to_rub(num):
    zero_to_nineteen = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
                        'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
                        'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = [0,1,'двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
    hundredths = [0, 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    if 0 <= num <= 19:
        return zero_to_nineteen[num]
    elif 20 <= num < 100:
        if num % 10 == 0:
            return tens[num // 10]
        word = tens[num//10] + ' ' + zero_to_nineteen[num%10]
        return word
    if 100 <= num < 1000:
        if 0 <= num % 100 <= 19:
            return hundredths[num // 100] + ' ' + zero_to_nineteen[num]
        elif 20 <= num % 100 < 100:
            if num % 10 == 0:
                return hundredths[num // 100] + ' ' + tens[num // 10 % 10]
            word = hundredths[num // 100] + ' ' + tens[num // 10 % 10] + ' ' + zero_to_nineteen[num % 10]
            return word


def input_int(a):
    while True:
        num = input(f'Введите количество {a}: ')
        if num.isdigit(): # проверка на ввод числа даже отрицательного
            return int(num)
        else:
            print("Введено не число, попробуйте заново")

# считываем данные
rub = input_int("рублей")
kop = input_int("копеек")

rub += kop // 100 # переводим копейки в рубли
kop = kop % 100 # остаток от копеек после перевода в рубли

rub_words = number_to_rub(rub) # вызываем функцию для ввода в рубли
kop_words = number_to_kop(kop) # вызов функции для копеек

if rub_words[-1] in 'н':
    r = 'рубль'
elif rub_words[-1] in 'аие':
    r = 'рубля'
elif rub_words[-1] in 'ькто':
    r = 'рублей'

if kop_words[-1] in 'еи':
    k = 'копейки'
elif kop_words[-1] in 'а':
    k = 'копейка'
elif kop_words[-1] in 'ькто':
    k = 'копеек'


print(f'{rub_words} {r},  {kop_words} {k}')