def GCD_Without_List(m,n):
  for i in range(1,min(m,n)+1):
    if (m%i)==0 and (n%i)==0:
      mrcf = i       # most recent common factor
  return mrcf


print(GCD_Without_List(212,10))

# Both the GCD with list and GCD without list takes proportionally same time as min(m,n) to execute