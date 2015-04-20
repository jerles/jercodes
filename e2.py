def triangle(x):
	for a in range(x+1):
		for b in range(a):
			print("T",end="")
		print()
	for a in range(1,x):
		for b in range(x-a):
			print("T",end="")
		print()
	
   
size=int(input("Give me the size of the triangle: "))
tri=triangle(size)
