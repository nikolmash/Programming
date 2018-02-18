import random

def get_words_dict():
    d = {}
    with open('words.csv') as f:
        for line in f:
            line = line.strip()
            word, hint = line.split(';')
            d[word] = hint 
    return d

def guess_word(dict):
    dict = get_words_dict()
    words = list(dict.keys())
    word = random.choice(words)
    return word

def guess_hint(dict):
    dict = get_words_dict()
    right_word = guess_word(dict)
    hint = d[right_word]
    return hint
    
    
def guessing(right_word):
    dict = get_words_dict()
    right_word = guess_word(dict)
    right_hint = dict[right_word]
    i = 3
    while i != 0:
        print('Подсказка для загаданного слова: ', right_hint, ' ...')
        print('Осталось попыток: ', i)
        user_word = input('Введите Ваше предположение: ')
        if user_word == '':
            print('Введена пустая строка')
            break
        else:
            if user_word == right_word:
                print('Вы угадали')
                break
            else:
                print('Неверно')
                i = i-1
        if i == 0:
            print('Вы не угадали слово')


dict = get_words_dict()
right_word = guess_word(dict)
guessing(right_word)
    

    







                
                

