
names = ['Оля', 'Петя', 'Вася', 'Маша']

print(', '.join(names))


names = ['Оля', 'Петя', 'Вася', 'Маша']



is_male = {
  'Оля': False,  
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
    if name not in is_male:
        print(f'{name} is not in the dictionary')
    elif is_male[name]:
        print(f'{name} is male')
    else:
        print(f'{name} is female')


groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

groups_count = len(groups)
members_groups_count = [len(inner_group) for inner_group in groups]


print(f'There are {groups_count} groups.')
for group_volume in members_groups_count:
    print(f'There are {members_groups_count} students in group.')




groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

for i, inner_group in enumerate(groups):
    names = ', '.join(inner_group)
    print(f'Group {i+1} : {names}')
