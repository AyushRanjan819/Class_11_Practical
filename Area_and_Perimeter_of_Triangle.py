#To Find Area and Perimeter of Triangle
print("Program to Find Area and Perimeter of Triangle".center(100,'='))
L1 = float(input("Give length 1 of tringle :- "))
L2 = float(input("Give length 2 of tringle :- "))
L3 = float(input("Give length 3 of tringle :- "))
p = L1 + L2 + L3
print("Perimeter of triangle is ", p)
s = p / 2
Ar = (s*(s-L1)*(s-L2)*(s-L3))**(1/2)
print("Area of triangle is ", round(Ar,2))
