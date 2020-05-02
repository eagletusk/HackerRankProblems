def twoStrings(s1, s2):
    if(len(s1) > len(s2)):
        for i in s2:
            if i in s1:
                return "YES"
        return "NO"    
    else:
        for i in s1:
            if i in s2:
                return "YES"
        return "NO" 
        