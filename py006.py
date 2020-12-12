# Program to find entered string is vowel or not Consonant
# a e i o u  A E I O U
# taking user input
# ch = input("Enter a character: ")

# if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 # or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    # print(ch, "is a Vowel")
# else:
    # print(ch, "is a Consonant")
    







# #separe in the string
str = input("Enter a word ")
counter =0
for ch in str:
     counter = counter+1
     if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
     or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
         print(counter, "letter ", ch, "is a Vowel")
     else:
      print(counter, "letter ", ch, "is a Consonant")