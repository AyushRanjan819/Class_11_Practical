#To Check String is Palidrom or not
print("Program to check string is palidrom or not".center(100,'='))
a=input('enter a string:-')
for i in range(len(a)//2):
    if a[i]!=a[-i-1]:
        print('print string is not palindrome')
        break
else:
    print('print string is palindrome')
