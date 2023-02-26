def GCD(m,n):
  cf = [] # List to store the comman factors
  for i in range(1,min(m,n)+1):
    if (m%i)==0 and (n%i)==0 :
      cf.append(i)
  return cf[-1]

print(GCD(75,10))