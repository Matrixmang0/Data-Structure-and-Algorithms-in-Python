def quickSort(list):

  n = len(list)

  if n<=1 :
    return list

  L = []
  U = []

  pivot = list[0]

  for i in range(1,n):
    if list[i]<pivot :
      L.append(list[i])
    else :
      U.append(list[i])

  return quickSort(L)+[pivot]+quickSort(U)

l = [4,5,4,12,756,3,75,13,654,35,13,76,45]

print(quickSort(l))