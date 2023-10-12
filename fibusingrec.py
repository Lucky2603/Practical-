def fib(num):
	if(num<=1):
		return num
	else:	
		return(fib(num-1)+fib(num-2))
		
a=int(input("enter the number of terms:- "))

for x in range(a):
    print(fib(x))
