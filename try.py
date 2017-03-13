def Is_prime(n):
    out = list()
    num= input("please enter number:")
    for num in range(1, n+1):
        Is_prime = True
        for factor in range(2, num):
            if (num % factor == 0):
                Is_prime = False


        if Is_prime==True:
        	print "%d is a prime number" %number
        else:

            print "%d is not a prime number" %number
        
        if Is_prime:
            out.append(num)
    return out



 