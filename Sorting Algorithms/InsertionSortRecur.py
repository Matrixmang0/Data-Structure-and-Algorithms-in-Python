def Insert(L,el):

  n = len(L)

  if n==0:
    return ([el])
  elif L[-1] <= el :
    return (L+[el])
  else :
    return (Insert(L[:-1],el)+L[-1:])

def ISort(L):

  n = len(L)

  if n<=1 :
    return L
  L = Insert(ISort(L[:-1]),L[-1])
  return L

Li = [54,65634,23,76,38,79,17,8,178]

print(ISort(Li))