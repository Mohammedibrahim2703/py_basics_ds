##Fibonacci sequence

def recursive_fab(n):
    if n<=1:
        return n
    else:
        return (recursive_fab(n-1) + recursive_fab(n-2))

def recursive_fab1(n_term):
    #erm=10
    if n_term <=0:
        print("Invalid")
    else:
        print("Fabinaaci")
        for i in range(n_term):
            print(recursive_fab(i))


print(recursive_fab1(10))

def functions(n):
    if (n>0):
        print("woo,", n)
        functions(n-1)
        print("Between call,", n)
        functions(n-1)
        print("After call,", n)
       # functions(n-1)
print(functions(3))

## Factorial
def myfact(n):
    if n==1:
        return n
    else:
        return n * myfact(n-1)
print(myfact(4))

##Fibnanocci
def myfib(n):
    if n <=1:
        return n
    else :
        return (myfib(n-1)+myfib(n-2))
cnt=10
if cnt <0 :
    print("Invalid Input")
else:
    sum=0
    for i in range(cnt):
      print(myfib(i),end=" ")
      sum+=myfib(i)
      last_val=myfib(i)

print( " \n sum :-",sum)
print(" \n  last value",last_val)