import os

start_path = '.'
count_of_dirs = 0
for root, dirs, files in os.walk(start_path):
    for x in dirs:
        list_of_ext =[]
        for file in os.listdir(x):
            base, ext = os.path.splitext(file)
            ext = ext.lower()
            list_of_ext.append(ext)
        if len(list_of_ext) != len(set(list_of_ext)):
            count_of_dirs += 1
                
print('Найдено папок с повторяющимися расширениями файлов: ' , count_of_dirs) 
            
            
            
