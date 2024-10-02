#To Find Roots Of Quadratic Equation
print("Program to find roots of a quadratic equation".center(100,'='))
a = float(input("give the value of 'a' :- "))
b = float(input("give the value of 'b' :- "))
c = float(input("give the value of 'c' :- "))

d = (b**2)-4*a*c
if d > 0:
    x = (-b + (d)**(1/2))/2*a
    y = (-b - (d)**(1/2))/2*a

    print("Root of this equation are" , round(x,2) , "and" , round(y,2))
else:
    print("No Real Roots Exist")
