import random

def noun():
    gender = ['m','f','n']
    noun_gender = random.choice(gender)
    with open("nouns_m.txt", encoding="utf-8") as f:
        text = f.read()
        nouns_m = text.split(',')
    with open("nouns_f.txt", encoding="utf-8") as e:
        text = e.read()
        nouns_f = text.split(',')
    with open("nouns_n.txt", encoding="utf-8") as c:
        text = c.read()
        nouns_n = text.split(',')
    if noun_gender == 'm':
        result = 'der ' + random.choice(nouns_m)
        return result
    elif noun_gender == 'f':
        result = 'die ' + random.choice(nouns_f)
        return result
    elif noun_gender == 'n':
        result = 'das ' + random.choice(nouns_n)
        return result
    
def verb():
    with open("verbs.txt", encoding="utf-8") as d:
        text = d.read()
        verbs = text.split(',')
    #verbs = ['spielen','kaufen','küssen','lieben','schreiben','brauchen','kochen']
    result = random.choice(verbs)
    result = result[:-2] + 't'
    return result


def object():
    with open("adjectives.txt", encoding="utf-8") as k:
        text = k.read()
        adjectives = text.split(',')
    #adjectives = ['klein','alt','gesund', 'fantastisch','schön','rot','frisch']
    adjective = random.choice(adjectives)
    result = noun()
    if result[0:3] == 'der':
        result = result.replace('der', 'den')
        adjective = adjective + 'en'
    if  result[0:3] == 'die':
        adjective = adjective + 'e'
    if  result[0:3] == 'das':
        adjective = adjective + 'es'
    result = result.replace(' ',' . ')
    result = result.replace('.',adjective)
    return result
    

def affirmative():
    subj = noun()
    subj = subj.title()
    result = subj + ' ' +verb() + ' ' + object() + '.'
    return result

def question():
    check = random.randint(0, 1)
    with open("question_words.txt", encoding="utf-8") as q:
        text = q.read()
        question_words = text.split(',')
    #question_words = ['Wo', 'Warum', 'Wann','Wen','Wie']
    if check == 0:
        verb_in_sentence = verb()
        verb_in_sentence = verb_in_sentence.title()
        result = verb_in_sentence + ' ' + noun() + ' ' + object() + '?'
    if check == 1:
        quest_word = random.choice(question_words) 
        result = quest_word + ' ' + verb() + ' ' + noun() + ' ' + object() + '?'
    return result

def negative():
    subj = noun()
    subj = subj.title()
    result = subj + ' ' + verb() + ' ' + object() + ' nicht.'
    return result

def imperative():
    with open("pronouns.txt", encoding="utf-8") as p:
        text = p.read()
        pronouns = text.split(',')
    #pronouns = ['Sie','sie','du']
    person = random.choice(pronouns)
    if person == 'Sie':
        action = verb()[:-1]+'en'
        action = action.title()
        result = action + ' ' + person + ' ' + object() + '!'
    if person == 'sie':
        action = verb()
        action = action.title()
        result = action + ' ' + object() + '!'
    if person == 'du':
        action = verb()[:-1]
        action = action.title()
        result = action + ' ' + object() + '!'
    return result
        
def conditional():
    first_part = affirmative()[:-1]
    second_part = affirmative()
    article1 = first_part[0:3]
    article1 = article1.lower()
    first_part = first_part.replace(first_part[0:3],article1)
    article2 = second_part[0:3]
    article2 = article2.lower()
    second_part = second_part.replace(second_part[0:3],article2)
    result = 'Wenn ' + first_part + ', ' + second_part
    return result


a = affirmative()
b = question() 
c = negative()
d = imperative()
e = conditional()
order = [a,b,c,d,e]
random.shuffle(order)
for i in order:
    print(i)




