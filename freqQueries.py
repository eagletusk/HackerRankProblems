def freqQuery(queries):
  class Found(Exception): pass
  stack=[]
  end = len(queries)
  i = 0
  dictionary = {}
  
  while i < end:
    if queries[i][0] == 1:
      if queries[i][1] in dictionary:
        dictionary[queries[i][1]] += 1
      else:
        dictionary[queries[i][1]] =1
   
    elif queries[i][0] == 2:
      if queries[i][1] in dictionary:
        dictionary[queries[i][1]] -= 1
        
    else:
    # queries[i][0] == 3:
    # print(dictionary)
      try:
        for k,l in dictionary.items():
          if l == queries[i][1]:
            raise Found 
      
      except Found:
        ditionary = {} 
        stack.append(1)
      else:
        stack.append(0)
    
    i+= 1
  return stack

print(freqQuery([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]))