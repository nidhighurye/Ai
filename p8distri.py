a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))
c=int(input("Enter 3rd Number : "))

#for multiplication
p=a*(b+c)
print("LHS = ",p)
q=(a*b)+(a*c)
print("RHS = ",q)

if(p==q):
    print("LHS = RHS, Distributive Law, a*(b+c)=(a*b)+(a*c) is proved")
else:
    print("LHS != RHS")
