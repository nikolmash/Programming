word = input("Введите слово: ")
new_word = ''
if word == '':
    print('Введена пустая строка')
vowels = ['a', 'e' ,'i', 'o', 'u', 'y']
for i in range(6):
    if vowels[i] == word[0]:
        new_word = word + 'ау'
        #перебрали все гласные
if new_word == '':
    for j in range(6):
        for k in range(len(word)):
            if word[k] == vowels[j]:
                new_word = word[word.find(vowels[j]):] + word[:word.find(vowels[j])] + 'ау'
                break
print(new_word)

