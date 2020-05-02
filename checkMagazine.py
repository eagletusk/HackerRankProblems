def checkMagazine(magazine, note):
    words = {}
        

    for i in magazine:
        if i in words:
            words[i] += 1 
        else: 
            words[i] =1

    
    for j in note:
        if j not in words or words[j] == 0:
            print('No')
            return
        else:
            words[j] -=1

    print('Yes')