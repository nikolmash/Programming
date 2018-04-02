import re

def get_text(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
    return text

def get_animal(text):
    name = re.search('<h1.*?>(.*?)</h1>', text)
    name = name.group(1)
    return name
    
    
def get_order(text):
    ord = re.search('Отряд.*?title=.*?>(.*?)</a>', text)
    ord = ord.group(1)
    return ord

    

filename = input('Введите название файла: ')
with open('text.txt', 'w', encoding="utf-8") as f:
    while filename != '':
        text = get_text(filename)
        name_of_animal = get_animal(text)
        order_of_animal = get_order(text)
        result = name_of_animal + ': ' + order_of_animal
        f.write(result)
        f.write('\n')
        filename = input('Введите еще одно название файла: ')

print('Введена пустая строка, работа программы завершена') 
    
