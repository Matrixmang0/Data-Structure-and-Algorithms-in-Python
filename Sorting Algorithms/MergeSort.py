def merge(A,B):

  m = len(A)
  n = len(B)

  (C,i,j,k) = ([],0,0,0)

  while (k < (m+n)):

    if (m==i) :
      C.extend(B[j:])
      k = k + (n-j)
    elif (n==j):
      C.extend(A[i:])
      k = k + (m-i)
    elif (A[i] < B[j]):
      C.append(A[i])
      (i,k) = (i+1,k+1)
    else:
      C.append(B[j])
      (j,k) = (j+1,k+1)

  return C

def mergeSort(L):

  n = len(L)

  if n <= 1:
    return L

  l = mergeSort(L[:n//2])
  r = mergeSort(L[n//2:])

  newLi = merge(l,r)

  return newLi

li = [43,65,12,74,1,7,2,54,14,756,12,87,32]

print(mergeSort(li))