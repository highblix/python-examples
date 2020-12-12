#program to print multiplication table


# loop will repeat itself as long as
# num < 10 remains true
n=0
while n<20:
    n=n+1
    num=1
    while num <= 10     :
        #print(2, " x ", num, " = ", 2*num )
        print(" {:3}  x  {:3}  = {:3}".format(n,num,num*n))
        #incrementing the value of num
        num = num + 1
    print("-------------------------")
    print("")