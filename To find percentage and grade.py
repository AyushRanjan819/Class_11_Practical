# To find percentage and grade
print("Program To Find Percentage And Grade".center(100,'='))
name = input("Enter Your Name :- ")
Roll = input("Enter your Roll Number :- ")
sub1 = int(input("give your subject 1 marks :- "))
sub2 = int(input("give your subject 2 marks :- "))
sub3 = int(input("give your subject 3 marks :- "))
sub4 = int(input("give your subject 4 marks :- "))
sub5 = int(input("give your subject 5 marks :- "))
sum = sub1 + sub2 + sub3 + sub4 + sub5
print("Your Total Marks Is ", sum)
percent = sum/5
print("Your Total Percent Is ", round(percent,2))
if percent >= 90:
    print("You Get Grade A")
elif percent >= 75:
    print("You Get Grade B")
elif percent >= 50:
    print("You Get Grade C")
else:
    print("You Get Grade D")
