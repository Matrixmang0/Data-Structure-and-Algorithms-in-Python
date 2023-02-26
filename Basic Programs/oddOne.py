def oddOne(List):
  """This function returns that type of the data that is least used in the List"""
  # Typically the input list would contain one element that is of another type than all other elements in the list
  type1_n = 0
  type2_n = 0
  for i in range(len(List)):
    type1 = type(List[0])
    if type(List[i])==type1:
      type1_n += 1
    else :
      type2_n += 1
      type2 = type(List[i])
  
  if (type1_n>type2_n):
    return(type2.__name__)
  else:
    return(type1.__name__)


print(oddOne(eval(input().strip())))