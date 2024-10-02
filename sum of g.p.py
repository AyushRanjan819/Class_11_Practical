#to find the sum of series G.P
print("Program To Find Sum Of G.P Series ".center(100,'='))
n = int(input("enter value of 'n' :- "))
x = float(input("give the value of x :- "))
s = 1*(1-(x)**(n+1))/(1-x)
print("Sum of given G.P is ",round(s,2))
