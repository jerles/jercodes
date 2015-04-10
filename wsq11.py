def inverse(x):
    x=str(x)
    x=x[::-1]
    x=int(x)
    return x

numbers=[]
lychrel=[]
a=0
b=0
c=0
print("YoSoy196")
print("This program calculates the natural palindromes, the non-Lychrel and the Lychrel candidates of a range of numbers")
num1=int(input("Give the lower bound of numbers to consider: "))
num2=int(input("Give the upper bound of numbers to consider: "))
print ("The results for the range",num1,"to",num2,"are: ")
for i in range(num2-num1+1):
    numbers.append(num1)
    num1=num1+1
for i in numbers:
    x=inverse(i)
    if i==x:
        a=a+1
    else:
        y=i+x
        x1=inverse(y)
        for j in range(30):
            if y==x1:
                c=c+1
                break
            else:
                y=y+x1
                x1=inverse(y)
                if j==29:
                    b=b+1
                    lychrel.append(i)
if b!=0:
    print ("LYCHRELS FOUND:")
    print (lychrel)
print("Palindromes:",a)
print("Non-Lycherels:",c)
print("Lycherels:",b)
