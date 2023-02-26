import math

def factors(n):
  fl = []   # factors list
  for i in range(1,n+1):
    if n%i==0:
      fl.append(i)
  return fl


def isPrime1(num):   # Method 1
  if (factors(num)==[0,num]):
    return True
  return False


def isPrime2(num):
  val = True    # Assume the number is prime
  for i in range(2,num):
    if num%i==0 :
      val = False
  return val

def isPrimeEfficient(num):   # Still more efficient way to check prime
  for i in range(2,int(math.sqrt(num))+1):
    if num%i==0:
      return False
  return True

def primesUpto(num):
  pl = []     # Primes List
  for i in range(2,num+1):
    if isPrime2(i):
      pl.append(i)
  return pl

def firstNPrimes(count):
  fnpl = []     # First n primes list
  num = 2
  while(len(fnpl)<=count):
    if isPrime1(num) :
      fnpl.append(num)
  return fnpl

def primeDiffs(num):
  '''This functions computes the difference between the adjacent prime numbers and keep a count on the differnces computed upto the number provided as the parameter'''
  pd = {}
  lastPrime = 2
  for i in range(3,num+1):
    if isPrimeEfficient(i):
      diff = i - lastPrime
      lastPrime = i
      if diff in pd.keys():
        pd[diff] += 1
      else:
        pd[diff] = 1
  return pd


print(isPrimeEfficient(121))