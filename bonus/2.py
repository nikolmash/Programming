number = input('Введите температуру в градусах Цельсия ')
if number == '':
    print('Введена пустая строка')
else:
    degrees_c = int(number)
    kelvin = degrees_c + 273.15
    degrees_f = 1.8*degrees_c + 32
    print('Температура в градусах Фаренгейта равна: ' , degrees_f)
    print('Температура в Кельвинах равна: ' , kelvin)
                  
