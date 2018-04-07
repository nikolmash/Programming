import re

def read_file(filename):
    with open (filename, encoding="utf-8") as f:
        text = f.read()
    return text

def tag_search(text):
    text_in_tag = re.findall(r'<se>(.*?)</se>', text, re.DOTALL)
    textin = ''.join(text_in_tag)
    lines_in_tag = re.findall(r'(.*?)\n', textin)
    count = 0
    for line in lines_in_tag:
        count += 1
    return count

def create_dict(text):
    d = {}
    textlines = text.splitlines()
    for line in text:
        characteristics = re.findall(r'gr="(.*?)"', line)
        same_charact = text.find(characteristics)
        for x in same_charact:
            freq += 1
        d[characteristics] = freq
    return d 
        
        
    
filename = input('Введите название файла: ')
if filename == '':
        print('Введена пустая строка')
else:
    text = read_file(filename)
    amount = tag_search(text)
    dictionary = create_dict(text)
    with open('text.txt', 'w', encoding="utf-8") as f:
        f.write(str(amount))
        for key, value in dictionary.items():
            f.write(key, value)
