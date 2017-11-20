with open("text.txt", encoding="utf-8") as f:
    kol = 0
    count = 0
    flag = 0
    kolich = 0
    for line in f:
        kol += 1
        for i in range(len(line)):
            if line[i] != ' ' and flag == 0:
                count += 1
                flag = 1
            else:
                if line[i] == ' ':
                    flag = 0
            if count>5:
                kolich += 1
    x = int(kolich/kol*100) 
    print(x)
         
    
        
            
        
    
