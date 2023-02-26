class Triangle:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
    def Is_valid(self):
        if ((self.x+self.y)>self.z) and ((self.y+self.z)>self.x) and ((self.x+self.z)>self.y) :
            return "Valid"
        else :
            return "Invalid"
    def Side_Classification(self):
        if self.Is_valid()=="Valid":
            if self.x==self.y==self.z :
                return ("Equilateral")
            elif (self.x==self.y) or (self.y==self.z) or (self.x==self.z):
                return ("Isosceles")
            else :
                return ("Scalene")
        else:
            return "Invalid"
    def Angle_Classification(self):
        if self.Is_valid()=="Valid":
            s1 = min(self.x,self.y,self.z)
            s3 = max(self.x,self.y,self.z)
            s2 = (self.x + self.y + self.z) - (s1 + s3)
            s1 = s1*s1
            s2 = s2*s2
            s3 = s3*s3
            
            if (s1+s2)>s3:
                return ("Acute")
            elif (s1+s2)==s3:
                return ("Right")
            else:
                return ("Obtuse")
        else :
            return "Invalid"
    def Area(self):
        
        if self.Is_valid()=="Valid":
            import math
            s = (self.x+self.y+self.z)/2
            area = math.sqrt(s*(s-self.x)*(s-self.y)*(s-self.z))
            return area
            
        else :
            return ("Invalid")
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())