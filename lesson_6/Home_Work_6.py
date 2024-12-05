def yes_or_no(num_list):
    cash_set = set()
    for i in num_list:
        if i in cash_set:
            print("YES")
        else:
            print('NO')
            cash_set.add(i)

some_num_list = [int(i) for i in input('Введите целые числа через пробел: ').split() ]

yes_or_no(some_num_list)


def count_char(STR_VAL):
    cache_dict = dict()
    for i in STR_VAL:
        if i in cache_dict:
            cache_dict[i] += 1
        else:
            cache_dict[i] = 1
    return cache_dict

print(count_char(input('\n\ninput your phraze: ').lower()), '\n\n')



def bread(func):
    print('</----------\\>')
    def wrapped():
        func()
        print('<\\___________/>')
        print('\n\n')
    return wrapped

def tomato(func):
    print('***помидоры***')
    def wrapped():
        func()
    return wrapped

def salad(func):
    print('~~~Салат~~~')
    def wrapped():
        func()
    return wrapped

def cheese(func):
    print('^^^СЫР^^^')
    def wrapped():
        func()
    return wrapped

def onion(func):
    print('-----ЛУК-----')
    def wrapped():
        func()
    return wrapped

@tomato
@onion
@bread
def beef():
    print('###говядина###')

beef()


@salad
@cheese
@bread
def chicken():
    print('|||КУРА|||')

chicken()
