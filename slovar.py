import csv

my_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('my.csv', 'w', encoding='UTF-8') as my_file:
    fields_list = ['name','age','job']
    writer = csv.DictWriter(my_file, fields_list, delimiter = '\t')
    writer.writeheader()
    for my in my_list:
        writer.writerow(my)
