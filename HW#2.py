Q1
def fancy_printing(n):

    
    a=[]
    for i in range(1,n+1):
        if(n%i==0):
            a.append(i)
            
    def result(n):
        b=[]
        t=0
        
        for i in range(0,n+1):
            b.append(i)
        for i in range(0,len(a)):
            
            while(t<len(b)-1):
                if(a[i]==b[t]):
                    b[t]="buzz!"
                    break
                t+=1
        i=0
        while(i<len(b)):

            print(b[i])
            i+=1
    return result

replace = fancy_printing (18)
replace(20)

Q2
def sum_num(n):
    if(n==0 or n==1 ):
        return n
    
    return n+(sum_num(n-2))

print(sum_num(5))
Q3

def cnt_primes(n):
    
    if(n==1):
        return 0
    for x in range(n-1,1,-1):
        if(n%x==0):
            return cnt_primes(n-1)
return 1+cnt_primes(n-1)


print(cnt_primes(6))
print(cnt_primes(10))

Q4
def square(x):
    return x*x
def triple(x):
    return 3*x
def identity(x):
    return x
def incr(x):
    return x+1
def foo(f, n):
    def result(t):
        
        for i in range(0,n):
            t=f(t)
    
        return t
    
    
    return result


add3 = foo (incr, 3)
print(add3(5))

add3 = foo (triple, 5)
print(add3(1))
print( foo(square,4)(5))

Q5

def op(a, b, c):
    result=a*b
        
        if(a==0 and b==0):
            return result+c
                
                return result+op(0,0,c)

print(op(2,4,3))

print(op(0,3,2))

Q6
def checking(x):
    if(x/10>9):
        
        if(x%10<(x/10)%10 and x%10 != (x//10)%10 ):
            
            return False
    if(x/10<10 and (x%10<x/10) and (x%10 != x//10)):
        return False
    if(x//10==0):
        return True
    
    return checking(x//10)
print(checking(2222))
print(checking(12346))
print(checking(123946))

Q7
def cal(n):
    
    if(n==0):
        return 0
    elif(n==1):
        return 1
    
    return n*cal(n-2)
print(cal(5))
print(cal(8))

Q8
def square(x):
    return x*x
def triple(x):
    return 3*x
def identity(x):
    return x
def increment(x):
    return x+1
def intscts(f, x):
    def compare(s):
        if(f(x)==s(x)):
            return True
        else:
            return False
    return compare
at_three = intscts (square, 3)
print(at_three(triple))
print(at_three(increment))
at_three = intscts (identity, 1)
print(at_three(square))

Q9
def A(n):
    if(n<=3):
        return n
    if(n>3):
        return A(n-1)+ 2*A(n-2)+ 3*(n-3)
    
    return A(n-1)+ 2*A(n-2)+ 3*(n-3)
print(A(4))
print(A(5))

Q10
def bnc_bck_frth(k):
    count=1
    switch=1
    for x in range(1,k):
        if(x%10==7 or x%7==0 or (x//10)%10==7):
            
            switch*=(-1)
        if(switch==(-1)):
            
            count-=1
        
        else:
            count+=1

                return count
print(bnc_bck_frth(100))

