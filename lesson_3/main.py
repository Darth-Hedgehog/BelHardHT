firstname, lastname, age = input("input firstname: "), input("input lastname: "), int(input("input age: "))

print(f'Привет, меня зовут {firstname} {lastname}, мне {age} лет')

some_str = input("введите строку: ")
print(some_str[2], some_str[-2], some_str[:5], some_str[:-2], sep="\n")

some_str = "Hello, world!"

print(some_str.replace('world', firstname))
