def power(base,exp):
    if(exp==1):
        return base
    if(exp!=1):
        return (base*power(base,exp-1))




base1=2
exp1=3
print("vale is" , power(base1,exp1))
print("******")