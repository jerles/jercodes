#Joel Erles A01630546

def fibonacci(x):
	if(x==0) or (x==1):
		return(x)
	if(x>1):
		return fibonacci(x-1)+fibonacci(x-2)

num=int(input("Give me a number: "))
fib=fibonacci(num)
print("The fibonacci of {} is {}".format(num,fib))
