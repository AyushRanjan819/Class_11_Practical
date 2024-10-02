# To Check Number Is Prime Or not
print("Program to find given number is prime or composite".center(100,'='))
num = int(input("Give Your Number :- "))
v = 0
if num > 1:
    for i in range(2,(num//2)+1):
        if num % i == 0:
            v = 1
    if v == 1:
        print("Given Number Is Composite Number")
    else:
        print("Given Number Is Prime Number")
else:
    print("Your Number Is Invalid")
