a=2
b=0.5
c=a+b
print(c)
name= 'Привет, Георгий'
print(name)
v=int(input("Ведите число от 1 до 10:"))
v= v+10
print(f'={v}!')


def get_summ(one, two, delimiter='&'):
     format_str = '{} {} {}!'.format(one, delimiter, two).upper()
     x = get_summ("Learn", "python")
print(x)

#города

dict = {"city": "Дмитров", "temperature": "11"}
print(dict.get("city"))

dict_upd = {"temperature": "6"}
dict.update(dict_upd)
print(dict)

print(dict.get("country"))
print(dict.get("country", "Russia"))

dict_upd_2 = {"date": "27.05.2019"}
dict.update(dict_upd_2)
print(dict)
print(len(dict))




user_info = {'first_name':'Georgit', 'last_name':'Cheburashkin'}

print(user_info['first_name'])
