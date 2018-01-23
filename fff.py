vowels = ['a', 'e' ,'i', 'o', 'u', 'y']
word = input("")
for j in range(6):
    if word.find(vowels[j]) != -1:
        print(word.find(vowels[j]))
        

