def triangles(x):
    for a in range(1,x+1):
        for b in range(a):
            print("T",end="")
        print()
    for a in range(1,x):
        for b in range(x-a):
            print("T",end="")
        print()

print("This program creates a triangle from a size given by the user")
size=int(input("Give me your triangle size: "))
tri=triangles(size)
