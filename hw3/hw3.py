word = input('Введите слово: ')
for i in range(len(word)//2):
    word = word[1:-1]
    print(word)
