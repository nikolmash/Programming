import re

def get_text(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
        text = text.lower()
    return text

def forms_of_verb(text):
    forms1 = re.findall('загрузи[а-я]+',text)
    forms2 = re.findall('загруж[е][а-я]+й',text)
    forms3 = re.findall('загруж[у][а-я]*', text)
    result = forms1 + forms2 + forms3
    return result
    
filename = input('Введите название файла: ')
if filename == '':
        print('Введена пустая строка')
else:
    text = get_text(filename)
    forms = forms_of_verb(text)
    forms = list(set(forms))
    for i in forms:
        print(i)
    
