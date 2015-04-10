def euclid(x,y):
    if y==0:
        return x
    else:
        return euclid(y, x%y)

num1=int(input("Give me a positive integer: "))
num2=int(input("Give me another positive integer: "))
euc=euclid(num1,num2)
print("The greatest common divisor of {} and {} is {}".format(num1,num2,euc))
