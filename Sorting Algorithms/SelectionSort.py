def SelectionSort(L):

  n = len(L)

  if n<=0 :
    return L
  else :
    for i in range(n):
      minpos = i
      for j in range(i+1,n):
        if L[j]<L[minpos]:
          minpos = j
      (L[i],L[minpos]) = (L[minpos],L[i])
    return L

list = [54,7,234,67,2,86,852,17,2]

print(SelectionSort(list))