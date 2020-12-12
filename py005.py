# Program for factorial of a number

# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 
# For example factorial of 4 is 4*3*2*1 which is 24.

#program to find the factorial of a number provided by the user.

# change the value for a different result
#num = 4

# To take input from the user
num = int(input("Enter a number: "))

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
       print(i,"  - ", factorial)
   print("The factorial of",num,"is",factorial)









# # Iterative Method

# # factorial of given number 
# def factorial(n): 
    # if n < 0: 
        # return 0
    # elif n == 0 or n == 1: 
        # return 1
    # else: 
        # fact = 1
        # while(n > 1): 
            # fact *= n 
            # n -= 1
        # return fact 
  
# # check  
# num = 5; 
# print("Factorial of",num,"is", factorial(num)) 











# # Recursive  Method


# # factorial of given number 
# def factorial(n): 
    # return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  
# # check 
# num = 5; 
# print("Factorial of",num,"is", factorial(num)) 

















# sdfsa dfsasdf
