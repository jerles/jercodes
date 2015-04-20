#Joel Erles A01630546

def superpower(x,y):
    if y==0:
        return 1
    a=x
    for i in range(y-1):
        a*=x
    return a

num1=int(input("Give me a number: "))
num2=int(input("Give me another number: "))
power=superpower(num1,num2)
print('{}^{}={}'.format(num1,num2,power))
