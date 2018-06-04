import re

def readtext():
    with open('text.txt', encoding ='utf-8') as f:
        text = f.read()
    text = text.replace('\n',' ')
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    symbols_to_remove = ',.:;!?"-()'
    cl_sentences = [x.replace(s,'') for s in symbols_to_remove for x in sentences]
    return cl_sentences 

def word_counter(sent):
    words_in_sentence = [x.split() for x in sent]
    a = 0
    for x in range(len(sent)):
        if len(words_in_sentence[x])>10:
            s = 0
            for word in words_in_sentence[x]:
                len_of_word = len(word)
                s += len_of_word
            result = s/len(words_in_sentence[x])
            print('Это предложение со словами длины' ,'{:03.1f}'.format(result))

        
    
            
            
    



text = readtext()
word_counter(text)     
        
