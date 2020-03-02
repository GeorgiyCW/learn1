with open('referat.txt', 'r', encoding='utf-8') as newfile:
     text = newfile.read()
     print(len(text))
     leaters = text.split()
     print(len(leaters))

with open('referat2.txt', 'w', encoding='utf-8') as newfile:
     newfile.write(text.replace('.', '!'))
