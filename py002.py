#Program to check if number is prime or not
#program in Python to check whether the input number is prime or not. 
#A number is said to be prime if it is only divisible by 1 and itself.

#number=3
number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")