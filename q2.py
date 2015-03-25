def find_threes(x):
    sum=0
    for a in x:
        if(a%3==0):
            sum=sum+a
            print(a,"is divisible by 3")
    return sum

print("This program returns the sum of the numbers in a list that are divisible by 3")
print("I'll ask for 8 numbers")
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
final=find_threes(list1)
print(final,"is the sum of all the numbers in the list that are divisible by 3")
