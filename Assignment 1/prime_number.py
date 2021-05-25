M = int(input("Enter starting number: ")) 
N = int(input("Enter last number")) 
result=[]
for num in range(M, N+1):
	if num > 1:  
	   for i in range(2,num):  
	       if (num % i) == 0:
	       		break
	   else:
	   		result.append(num)
print(result)
