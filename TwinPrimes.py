def isPrime(num):
  """The function to check whether a number is prime or not"""
  import math
  for i in range(2, int(math.sqrt(num))+1):
    if num%i==0:
      return False
  return True

def TwinPrimes(a,b):
  """The function to collect tuples of twin primes in a list within the range (a,b)
     Twin Primes are the pair of prime numbers which differ by 2"""
  TP = [] # list to store tuples of twin primes
  next_prime=-1
  for i in range(a,b+1):
    if isPrime(i) and next_prime==-1 :
      next_prime = i
    elif isPrime(i):
      pre_prime = next_prime
      next_prime = i
      if (next_prime-pre_prime)==2:
        TP.append((pre_prime,next_prime))
  return TP

num1 = int(input())
num2 = int(input())

print(sorted(TwinPrimes(num1,num2)))