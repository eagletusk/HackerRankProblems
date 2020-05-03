# def freqQuery(queries):
#   class Found(Exception): pass
#   stack=[]
#   end = len(queries)
#   i = 0
#   dictionary = {}
  
#   while i < end:
#     if queries[i][0] == 1:
#       if queries[i][1] in dictionary:
#         dictionary[queries[i][1]] += 1
#       else:
#         dictionary[queries[i][1]] =1
   
#     elif queries[i][0] == 2:
#       if queries[i][1] in dictionary:
#         dictionary[queries[i][1]] -= 1
        
#     else:
#     # queries[i][0] == 3:
#     # print(dictionary)
#       try:
#         for k,l in dictionary.items():
#           if l == queries[i][1]:
#             raise Found 
      
#       except Found:
#         ditionary = {} 
#         stack.append(1)
#       else:
#         stack.append(0)
    
#     i+= 1
#   return stack



from collections import defaultdict

def freqQuery(queries):
    results = []
    lookup = {}
    histogram = defaultdict(set)
    for command, value in queries:
        freq = lookup.get(value, 0)
        print(lookup,list(histogram))
        if command == 1:
            lookup[value] = freq + 1
            print(dict(histogram),value)
            histogram[freq].discard(value)
            print('mid ',dict(histogram))
            histogram[freq + 1].add(value)
            print('end ',dict(histogram))
        elif command == 2:
            lookup[value] = max(0, freq - 1)
            histogram[freq].discard(value)
            histogram[freq - 1].add(value)
        elif command == 3:
            results.append(1 if histogram[value] else 0)
    return results


print(freqQuery([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]))