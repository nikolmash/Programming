numh = input('Введите Ваш рост в см: ')
numw = input('Введите Ваш вес в кг: ')
if numh == '' or numw == 0:
    print('Невозможно определить индекс массы тела, введены одна или более пустых строк')
else:
    height = int(numh)
    weight = int(numw)
    imt = weight/(height*0.01*height*0.01)
    print('Ваш индекс массы тела: ', imt)
    if imt <= 16:
        print('Выраженный дефицит массы тела')
    elif imt > 16 and imt <= 18.5 :
        print('Недостаточная масса тела')
    elif imt > 18.5 and imt < 24.99:
        print('Норма')
    elif imt > 25 and imt <= 30:
        print('Избыточная масса тела')
    elif imt > 30 and imt < 35:
        print('Ожирение первой степени')
    elif imt > 35 and imt < 40:
        print('Ожирение второй степени')
    elif imt >= 40:
        print('Ожирение третьей степени')

             
