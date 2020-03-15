
s = input("Input:")
print(s[:-1:])



word = 'Архангельск'
print(word.count('а'))



word = 'Архангельск'
vowels = 0
for i in word:
    letter = i.lower()
    if letter == "а" or letter == "о" or\
       letter == "е" or letter == "у" or\
       letter == "ю" or letter == "э" or\
       letter == "ы" or letter == "ё" or\
       letter == "и" or letter == "я":
        vowels += 1
print(vowels)





sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))



sentence = 'Мы приехали в гости'
print('М','п', 'в', 'г')


sentence = 'Мы приехали в гости'
print(sentence.split())
