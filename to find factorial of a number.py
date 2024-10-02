#To find factorial of a number
print("Program To Find Factorial Of A Number" .center(100,'='))
num = int(input("give number you want factorial :- "))
x = num
for i in range(1,num):
    num *= i
print("factorial of ",x ,"is ",num)
