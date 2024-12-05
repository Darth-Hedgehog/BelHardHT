# Homework 4.1
list_1 = ['bo', 'chau', 'duo']
list_2 = ['fo', 'global', 'red hat']

list_1.append('cat')
list_2.append('alpaka')

print(list_1, list_2, '===============================',sep='\n')

list_1.insert(0, "first element")
list_2.insert(0, 'second list')

print(list_1, list_2, '===============================', sep='\n')

list_1.extend(list_2)
print(list_1)

#Homework 4.2
#===========================
zen_of_python = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

print("\nHOMEWORK 2:", "\n\nКоличество строк в Zen: ", zen_of_python.count('\n'), '\n=============================\n')

list_of_zen = zen_of_python.lower().split()

count_dict = {'is': list_of_zen.count('is'), 'and': list_of_zen.count('and'), 'or': list_of_zen.count('or')}

print(f'Подсчет вхождений: {count_dict}\n\n')
print(f'Замена в тексте "is" на "is not": \n{zen_of_python.replace("is", "is not")}')

