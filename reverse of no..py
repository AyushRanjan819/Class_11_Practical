# To reverse the number
print("Program to reverse number".center(100,'='))
num = int(input("Enter a number :- "))
reverse = 0
while num > 0:
    digit = num % 10       
    reverse = reverse * 10 + digit
    num = num // 10
print("The reverse of the number is:", reverse)
