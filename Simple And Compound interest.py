# To Find Simple interest
print("Program to find Simple interest" .center(100,'='))
p = float(input("Give the Principal Amount :- "))
r = float(input("Tell the rate of interest per year :- "))
t = float(input("Tell the time period in year :- "))
si = (p*r*t)/100
print("Simple Interest is ", round(si,2),'\n\n\n')


# To Find Compound Intrest
print("Program to find Compound interest" .center(100,'='))
p = float(input("Give the Principal Amount :- "))
r = float(input("Tell the interest rate :- "))
n = float(input("tell the number of time interest compounds in a year :- "))
t = float(input("time period in year :- "))
ci = p*(1+(r/(n*100)))**(n*t)
print("Compund Interest is ", round(ci,2))
