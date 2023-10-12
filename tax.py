cost=int(input("enter bike cost"))
if(cost>100000):
	print(cost*15/100,"road tax")
elif(cost>50000 and cost<=100000):
		print(cost*10/100,"road tax")
else:
     print(cost*5/100,"road tax")
	

     

