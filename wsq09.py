#Joel Erles

def factorial(x):
    a=x
    b=x
    for i in range(x-1):
        a=a*(b-1)
        b=b-1
    return a

print("Factorial Calculator")
print("This program displays the factorial of a number")
again="y"
while(again=="y"):
    while True:
        try:
            num=int(input("Give me a positive integer: "))
            break
        except ValueError:
            print("This is not an integer, try again.")
    while(num<0):
        try:
            num=int(input("This is not a positive integer, try again: "))
        except ValueError:
            print("This is not an integer, try again.")
    if(num==0):
        print("0! = 1")
    else:
        fac=factorial(num)
        prnt="{}! = {}".format(num,fac)
        print(prnt)
    again=input("Would you like to try another number? y/n: ")
    while(again!="y" and again!="n"):
        again=input("Incorrect option, choose -> y/n: ")
