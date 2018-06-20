import os
import re

def file_recover():
    list_of_files = os.listdir('news')
    for file in list_of_files:
        filepath = os.path.join('news',file)
        with open(filepath, encoding='utf-8') as f:
            text = f.read()
            text = re.sub(r'</?title>','',text)
            text_without_tag = re.sub(r'<.*?>','',text)
            result = text_without_tag.replace('`','')
            new_name = os.path.splitext(file)[0]
            new_name = new_name + '.txt'
            with open(new_name,'w', encoding='cp1251') as t:
                t.write(result)

def name_find():
    list_of_files = os.listdir('news')
    names = {}
    for file in list_of_files:
        filepath = os.path.join('news',file)
        with open(filepath, encoding='utf-8') as f:
            text = f.read()
            text_without_title = re.sub(r'<title>.*?</title>','',text) #было сказано, что не надо считать собственные имена в заголовке
            names_in_this_text = re.findall('</ana>([A-Z]|[А-Я].*?)</w>',text_without_title)
            for name in names_in_this_text:
                if name in names:
                    names[name] += 1
                else:
                    names[name] = 1
    return names

def names_write_in_table(diction):
    diction = name_find()
    with open('result2.csv','w') as f:
        for key,value in diction.items():
            f.write(key)
            f.write('\t')
            f.write(str(value))
            f.write('\n')


def find_bigrams():
    list_of_files = os.listdir('news')
    bigram_with_topic = {}
    for file in list_of_files:
        filepath = os.path.join('news',file)
        with open(filepath, encoding='utf-8') as f:
            text = f.read()
            tags_bigram = re.findall(r'gr="NUM.*?\n.*?gr="S.*?gen.*?</w>', text)
            topic = re.findall(r'="(.*?)"\sname="topic"',text)
        for couple in tags_bigram:
            gram = re.findall(r'/ana>(.*?)</w>',couple)
            bigram =''
            for x in gram:
                bigram = bigram + ' '+ x
            bigram_with_topic[bigram] = topic
    return bigram_with_topic


        
  
                

file_recover() #это задание 1

required_names = name_find()
names_write_in_table(required_names) #это задание 2

bigrams = find_bigrams() #это найденные биграммы с соответствующими топиками в задании 3, с таблицей csv не успела


            
            
            
                               
