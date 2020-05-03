def whatFlavors(cost, money):
  cost_dict = {}

  for i, icost in enumerate(cost):

    if money-icost in cost_dict:
      index1 =cost_dict[money-icost] +1
      index2 = i+1
      print(f'{index1} {index2}')
      return 
    else: 
      # takes care of the first element problem
      cost_dict[icost] = i



whatFlavors([1,2,3],3)