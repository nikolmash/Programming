import re

def get_text(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
    return text

def substitution(text):
    result = re.sub(r'Финл[яя́]нди(?=[яиею]й?)', 'Малайзи', text)
    return result
        
filename = input('Введите название файла: ')
if filename != '':
    text = get_text(filename)
    finaltext = substitution(text)
    with open('text.html', 'w', encoding="utf-8") as t:
        t.write(finaltext)
        print('Текст статьи изменен')
else:
    print('Введена пустая строка')
        


