def calculateGmean(a , b):
   mean = (a*b)/(a+b)
   print(mean)
   
def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")
   

a = 10
b = 20

isGreater(a,b)
calculateGmean(a , b)
print("The mean of a and b is:",calculateGmean)
print(isGreater)

c = 2
d = 4

isGreater(c,d)
calculateGmean( c , d)
print("The mean of c and d is:" , calculateGmean)
print(isGreater)
    