import statistics

def suma(x):
    a=sum(x)
    return a

def promedio(x):
    a=summ/10
    return a

def standev(x):
    a=statistics.stdev(x)
    return a


num1=int(input("Give me a number: "))
num2=int(input("Give me another number: "))
num3=int(input("Give me another number: "))
num4=int(input("Give me another number: "))
num5=int(input("Give me another number: "))
num6=int(input("Give me another number: "))
num7=int(input("Give me another number: "))
num8=int(input("Give me another number: "))
num9=int(input("Give me another number: "))
num10=int(input("Give me another number: "))
list1=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10];
print ("Your numbers are:",list1)
summ=suma(list1)
print ("Total sum:",summ)
prom=promedio(list1)
print ("Average:",prom)
stdev=standev(list1)
print ("Standard deviation:",stdev)
