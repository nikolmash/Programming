def readtext(filename):
    with open (filename, encoding = "utf-8") as f:
        text = f.read()
    text = text.lower()
    symbols_to_remove = ',.:;!?"-()'
    for s in symbols_to_remove:
        text = text.replace(s,'')
    words = text.split()
    return words

def omni_filter1(words):
    omniwords = []
    for word in words:
        if word[0:4] == 'omni':
            omniwords.append(word)
    return omniwords

def omni_filter2(words):
    without_omni_words = []
    for word in words:
        if word[0:4] == 'omni':
            without_omni_words.append(word[4:])
    return without_omni_words

def search_omni(words):
    omni_freq = {}
    for word in omniwords:
            if word in omni_freq:
                omni_freq[word] += 1
            else:
                omni_freq[word] = 1
    return omni_freq

def search_without_omni(words):
    without_omni_freq = {}
    for word in without_omni_words:
            if word in without_omni_freq:
                without_omni_freq[word] += 1
            else:
                without_omni_freq[word] = 1
    return without_omni_freq

filename = input('Введите название файла: ')
if filename == '':
        print('Введена пустая строка')
else:
    words = readtext(filename)
    omniwords = omni_filter1(words)
    without_omni_words = omni_filter2(words)
    freq1 = search_omni(omniwords)
    freq2 = search_without_omni(without_omni_words)
    print(freq1, freq2)

                
        
    
               
