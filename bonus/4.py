phrase = input("Введите слово или фразу: ")
result = ''
if phrase == '':
    print('Введена пустая строка')
vowels = ['а', 'е' ,'ё', 'и', 'о', 'у' ,'ы' , 'э' , 'ю', 'я']
words = phrase.split(' ')
for word in words:
    x = 0
    new_word = ''
    for k in range(len(word)):
            for j in range(10):
                if word[k] == vowels[j]:
                    new_word = new_word + word[x:k+1] + 'с' + vowels[j]
                    x = k+1
    new_word = new_word + word[x:]
    result = result + ' ' + new_word      
print(result)

