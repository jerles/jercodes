#Joel Erles A01630546

import math

def sroot(x):
    a= x/2
    b= a+1
    while(a!=b):
        c=x/a
        b=a
        a=(a+c)/2
    return a

def hypotenuse(x1,y1,x2,y2):
    x=(x2-x1)
    y=(y2-y1)
    a=(x*x)+(y*y)
    b=math.sqrt(a)
    return b

num1=int(input("Give me a number: "))
num2=int(input("Give me another number: "))
num3=int(input("Give me another number: "))
num4=int(input("Give me another number: "))
hypo=hypotenuse(num1,num2,num3,num4)
print("The distance between the points is:",hypo)
