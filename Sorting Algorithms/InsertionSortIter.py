# This is the iterative version of the insertion sort algorithm

def InsertionSort(L):
  
  n = len(L)

  if n<=1 :
    return L
  else :
    for i in range(n):
      j = i
      while (j>0 and L[j]<L[j-1]):
        (L[j],L[j-1]) = (L[j-1],L[j])
        j = j-1
    return L


list = [5,67,23,564,23,1238,78,234,6]

print(InsertionSort(list))