def isPrime(n):
  import math
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True

def Goldbach(num):
  """Goldbach's conjecture states that every even number after 2 is a sum of two prime numbers
  The function finds out the pairs of prime numbers whose sum is the even number provided inside the parameter"""
  
  pl = [] # List to store the prime numbers upto the number num
  for i in range(3,num):
    if isPrime(i):
      pl.append(i)
  gbl = [] # List to store the Goldbach's tuples
  for i in pl:
    if (num-i) in pl:
      if ((min(i,(num-i)),max(i,(num-i)))) not in gbl:
        gbl.append((min(i,num-i),max(i,num-i)))
  return gbl

n = int(input())
print(sorted(Goldbach(n)))

