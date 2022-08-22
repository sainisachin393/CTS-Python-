num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
for number in range (num1+1, num2):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
