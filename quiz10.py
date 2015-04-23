#QUESTION 1

def findThrees(x):
    sum=0
    for a in x:
        if(a%3==0):
            sum=sum+a
    return sum

print("I'll ask for 8 numbers then I'll get the sum of them")
num1=int(input("Give me the first number: "))
num2=int(input("Give me the second number: "))
num3=int(input("Give me the third number: "))
num4=int(input("Give me the fourth number: "))
num5=int(input("Give me the fifth number: "))
num6=int(input("Give me the sixth number: "))
num7=int(input("Give me the seventh number: "))
num8=int(input("Give me the eighth number: "))
list1=[num1,num2,num3,num4,num5,num6,num7,num8]
print(list1,", this is your list")
final=findThrees(list1)
print(final,"is the sum of all the numbers in the list that are divisible by 3")

#QUESTION 2

def dotProduct(x,y):
    ab=[]
    for i in range(0, len(x)):
        ab.append(x[i]*y[i])
    return sum(ab)

print()
print("I'll ask for 2 lists of 4 numbers, then I'll get the product of them and get the sum")
num1=int(input("Give me the first number of the first list: "))
num2=int(input("Give me the second number of the first list: "))
num3=int(input("Give me the third number of the first list: "))
num4=int(input("Give me the fourth number of the first list: "))
num5=int(input("Give me the first number of the second list: "))
num6=int(input("Give me the second number of the second list: "))
num7=int(input("Give me the third number of the second list: "))
num8=int(input("Give me the fourth number of the second list: "))
list1=[num1,num2,num3,num4]
list2=[num5,num6,num7,num8]
print(list1,", this is your first list")
print(list2,", this is your second list")
prod=dotProduct(list1,list2)
print("The result of the operation is:",prod)
