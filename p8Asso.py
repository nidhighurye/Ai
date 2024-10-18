a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))
c=int(input("Enter 3rd Number : "))

#for addition
x=a+(b+c)
print("LHS = ",x)
y=(a+b)+c
print("RHS = ",y)

if(x==y):
    print("LHS = RHS, Associative Law, a+(b+c)=(a+b)+c is proved")
else:
    print("LHS != RHS")

print("\n")

#for multiplication
p=a*(b*c)
print("LHS = ",p)
q=(a*b)*c
print("LHS = ",q)

if(p==q):
    print("LHS = RHS, Associative Law a*(b*c)=(a*b)*c is proved")
else:
    print("LHS != RHS")