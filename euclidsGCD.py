def euclidsGCD(m,n):
  (a,b) = (max(m,n),min(m,n))
  if (a%b)==0 :
    return b
  else:
    return euclidsGCD(b,a%b)

print(euclidsGCD(3,9997))