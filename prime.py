def prime_numbers(num):
	import math
	output= []
	for num in range(2,num+1):
		if num ==2 or num ==3:
			output.append(num)
		if num % 2 != 0 and num % 3 !=0 and type(math.sqrt(num)==float):
			output.append(num)
	return output


print prime_numbers(100)