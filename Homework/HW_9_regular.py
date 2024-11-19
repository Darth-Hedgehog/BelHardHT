import re


def good_password(password):
    template_pass = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[_])[A-Za-z0-9_]{5,21}$'
    if re.fullmatch(template_pass, password) is not None:
        return 'Good password'
    else:
        return 'Bad password'

print(good_password(input('Input your password: ')))


def check_phone(phone_number):
    template_number = '^(\+375\((25|33|44|29)\)\d{3}\-\d{2}\-\d{2})'
    if re.fullmatch(template_number, phone_number) is not None:
        return 'Good number'
    else:
        return 'Bad number'

print(check_phone(input('Введите номер телефона в формате +375(__)___-__-__: ')))

