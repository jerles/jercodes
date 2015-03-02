print("Temperature")
print("This program converts Fahrenheit to Celsius")
fah= int(input("Enter a Fahrenheit temperature: "))
cels= 5*(fah-32)/9
conv= "{} Fahrenheit is: {} Celsius".format(fah,cels)
print(conv)
if(cels>=100):
    print("Water boils")
else:
    print("Water does not boil")
