import os

file_list = []
punct = ['.',',','!','?',':',';','-','"','(',')', '—','/']
count = 0
for file in os.listdir():
    if os.path.isfile(file):
        base, ext = os.path.splitext(file)
        for x in punct:
            if x in base:
                count += 1
                if not file in file_list:
                    file_list.append(file) 
print('Файлов, названия которые содержат знаки препинания, найдено:', count) 
for x in file_list:
    print(x) 
