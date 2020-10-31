def sumOfSeries(n): 
	s = 0
	for i in range(1, n+1): 
		s +=i*i*i 	
	return s
n = int(input("enter the number till which sum of cube has to be found : "))
print(sumOfSeries(n)) 
