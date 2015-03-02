print("Sum of Numbers")
print("This program calculates the sum of a range of numbers")
num= int(input("Give me a number: "))
num2= int(input("Give me other number: "))
total = 0
for i in range(num,num2+1):
    total += i
print(total)
