phrase = input("Введите слово или фразу: ")
result = ''
if phrase == '':
    print('Введена пустая строка')
vowels = ['a', 'e' ,'i', 'o', 'u', 'y']
words = phrase.split(' ')
for word in words:
    new_word = ''
    for j in range(6):
        if vowels[j] == word[0]:
            new_word = word + 'ау'
        else: 
            for k in range(len(word)):
                if word[k] == vowels[j]:
                    new_word = word[word.find(vowels[j]):] + word[:word.find(vowels[j])] + 'ау'
    result = result + ' ' + new_word      
print(result)

