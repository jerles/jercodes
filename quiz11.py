#QUESTION 1

import statistics

def readNumbersFromFile(x):
    a=open(x, 'r')
    list=[]
    sum=0
    lin=0
    for line in a:
        sum=sum+int(line)
        list.append(int(line))
        lin = lin + 1
    av=sum/lin
    stdev=statistics.stdev(list)
    print("The sum of all the integers is:",sum)
    print("The number of integers (lines) is:",lin)
    print("The average is:",av)
    print("The standard deviation is:",stdev)

print()
print("QUESTION 1")
print("This program reads a text file with integers inside and does some operations")
readNumbersFromFile('random_numbers.txt')

#QUESTION 2

def check_banana(x):
    c=0
    a=open(x, 'r')
    for line in a:
        lin=line.lower()
        nana=lin.find("banana")
        while(nana!=-1):
            c=c+1
            nana=lin.find("banana",(nana+1))
    return c

print()
print("QUESTION 2")
print("This program finds how many times the word 'banana' appears in a text file")
bana=check_banana('bananas.txt')
print("The numbers of times that 'banana' appears in the file is {} times".format(bana))
