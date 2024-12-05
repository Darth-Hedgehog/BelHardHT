
def check_login(login: str):
    counter = [0, 0, 0, 0]
    for i in login:
        if i.isdigit():
            counter[0] += 1
        elif i.isupper():
            counter[1] += 1
        elif i.islower():
            counter[2] += 1
        elif i == '_':
            counter[3] += 1
        else:
            return f'NO here is a symbol: {i}'

    for i in counter:
        if i == 0:
            return 'NO'
    return 'YES'

print(check_login(input('Input your password: ')))

def check_phone(phone):
    only_digit = phone[8:11]+phone[12:14]+phone[15:]
    operator_code = ['(29)', '(33)', '(44)', '(25)']

    if (len(phone) == 17 and phone[:4] == '+375' and only_digit.isdigit() and
            phone[4:8] in operator_code) and phone[11] == phone[14] == '-':
        return 'Good number format'
    else:
        return 'Number format error'

print(check_phone(input('Введите номер телефона в формате +375(__)___-__-__: ')))
# +375(33)666-66-66
