# Random Number


import random
#print(random.random()) #0 and 1


# Example
# Import the random module, and display a random number between 1 and 9:
#random.randrange(1, 9)
# randrange(beg, end, step) 


#print(random.randrange(0, 10))
#print(random.randrange(1, 10), random.randrange(1, 10), random.randrange(1, 10))
#print(random.randrange(0, 100,5))  #steps of 5


# #=====================
# #random.randint(a, b)

# a=0
# b=10
# print(random.randint(a, b))
# #Return a random integer N such that a <= N <= b.

# #=====================



# # using choice() to generate a random number from a  
# # given list of numbers. 
print ("A random number from list is : ",end="") 
print (random.choice([1, 4, 8, 10, 3])) 
  
# # using randrange() to generate in range from 20 
# # to 50. The last parameter 3 is step size to skip 
# # three numbers when selecting. 
# print ("A random number from range is : ",end="") 
# print (random.randrange(20, 50, 3)) 



# # 3. random() :- This number is used to generate a float random number less than 1 and greater or equal to 0.

# # 4. seed() :- This function maps a particular random number with the seed argument mentioned. All random numbers called after the seeded value returns the mapped number.




# # 5. shuffle() :- This function is used to shuffle the entire list to randomly arrange them.

# # 6. uniform(a, b) :- This function is used to generate a floating point random number 
# #between the numbers mentioned in its arguments. 
# #It takes two arguments, lower limit(included in generation) and upper limit(not included in generation).





# # Python code to demonstrate the working of 
# # ===============shuffle() and uniform() 
   
# # importing "random" for random operations 
# import random 
  
# # Initializing list  
# li = [1, 4, 5, 10, 2] 
  
# # Printing list before shuffling 
# print ("The list before shuffling is : ", end="") 
# for i in range(0, len(li)): 
    # print (li[i], end=" ") 
# print("\n") 
  

# # using shuffle() to shuffle the list 
# random.shuffle(li) 
  
# # Printing list after shuffling 
# print ("The list after shuffling is : ", end="") 
# for i in range(0, len(li)): 
    # print (li[i], end=" ") 
# print("\n") 
  
  
  
  
# # using uniform() to generate random floating number in range 
# # prints number between 5 and 10 
# print ("============random.uniform") 
# print ("The floating point number between 5 and 10 is : ",random.uniform(5,10))
# print ("The floating point number between 5 and 10 is : ",random.uniform(5,10))


# #==============================
# # Python code to demonstrate the working of 
# # random() and seed() 
   
# # importing "random" for random operations 
# import random 
  
# # using random() to generate a random number 
# # between 0 and 1 
# print ("A random number between 0 and 1 is : ", end="") 
# print (random.random()) 
  
# # using seed() to seed a random number 
# random.seed(5) 
  
# # printing mapped random number 
# print ("The mapped random number with 5 is : ", end="") 
# print (random.random()) 
  
# # using seed() to seed different random number 
# random.seed(7) 
  
# # printing mapped random number 
# print ("The mapped random number with 7 is : ", end="") 
# print (random.random()) 
  
# # using seed() to seed to 5 again 
# random.seed(5) 
  
# # printing mapped random number 
# print ("The mapped random number with 5 is : ",end="") 
# print (random.random()) 
  
# # using seed() to seed to 7 again  
# random.seed(7) 
  
# # printing mapped random number 
# print ("The mapped random number with 7 is : ",end="") 
# print (random.random()) 
