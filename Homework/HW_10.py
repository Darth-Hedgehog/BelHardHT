import json
from typing import Optional
from pydantic import BaseModel


class UserSelect(BaseModel):
    id: int
    name :str


class User(UserSelect):
    age: int
    interests: Optional[list] = None #не обязательное поле может быть null,
    salary: float


def user(id):
    users = {
        'id': int(id),
        'name': input('Input name: '),
        'age': int(input('Input AGE: ')),
        'interests': list(input('Enter interests separated by a space: ').split()),
        'salary': float(input('Input salary: '))
        }
    return users

def add_object():
    with open('users.json', 'w+') as file:
        num = int(input('how match object do you want to add?: '))
        for i in range(num):
            if i == 0:
                file.write('[')
            json.dump(user(i), file, indent=4)
            if i<num-1:
                file.write(',\n')
            elif i == num-1:
                file.write(']')
            print()


def give_all_object():
    with open('users.json', 'r+') as file:
        data = json.load(file)
        for d in data:
            valid_user = User(**d)
            print(valid_user)


def give_some_object():
    with open('users.json', 'r+') as file:
        some_object = input('Who do you want to see?(input name): ')
        data = json.load(file)
        for d in data:
            if d['name'] == some_object:
                valid_user = User(**d)
                return valid_user


def give_all_id_name_object():
    with open('users.json', 'r+') as file:
        data = json.load(file)
        user_list = list()
        for d in data:
            user_list.append(UserSelect(**d))
        return user_list



#add_object()
# give_all_object()
print(*give_all_id_name_object(), sep='\n')
print(give_some_object())

