##Print and Add two numbers
num1 = 15
num2 =16
sum = num1+num2
print("Sum of two numbers {0}  and {1} is {2}".format(num1,num2,sum))
##Adding two number provided by user input
# number1 = input("1st no")
# number2 = input("2nd no")
# sum=float(number1)+float(number2)
# print("Sum of two numbers {0}  and {1} is {2}".format(number1,number2,sum))

##Factorial n! = n * (n-1) * (n-2) ...*1
def factorial(n):
    return 1 if(n==1 or n==0) else n * factorial(n-1)
num=5
print("Factorial of ", num ,"is",factorial(num))

##maximum of two nos
def maximum(a,b):
    if a > b:
        return a
    else:
        return b
print("maximum no is" ,maximum(2,4))
##max functions
maximum1= max(2,8)
print("max function" ,maximum1)

## SimpleInterest
def simpleInterst(p,t,r):
    print("Principal",p)
    print("time period is ",t)
    print("Rate Of Interese",r)
    si=(p*t*r)/100
    print("The Simple Interest is ",si)
    return si

##Compound Interest A = P(1 + R/100) t Compound Interest = A – P
def compoundInterest(princple,rate,time):
    amount=princple * pow((1+rate/100),time)
    CI=amount-princple
    print("Compound Interest is ", round(CI))

## Check if the number is armstrong number or Not
def isAmstrongNo(num):
    order=len(str(num))
    sum=0
    original=num
    while num > 0:
        digit = num % 10
        sum+=digit ** order
        num=num//10
        print(sum)
        if sum==original:
            return True
            return False

##Find all the Prime numbers
def prime(x,y):
    prime_list=[]
    for i in range(x,y):
        if i==1 or i==0:
            continue
        else:
            for j in range(2,int(i+2)+1):
              if i % j == 0:
                break
              else:
                prime_list.append(i)
              return prime_list


if __name__ == '__main__':
    print("Start")
    simpleInterst(4798000,20,float(6.4))
    compoundInterest(500000,10.22,5)
    print(isAmstrongNo(153))
    prime_no=prime(1,100)
    print(prime_no)
    print("End")



