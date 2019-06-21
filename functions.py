#iterate values in a set and find the sum. Uses function call which inturn has a tuple
def add (a=0,*b):
    sum=a
    i = 0
    while i<len(b):
        sum = sum + b[i]
        i=i+1
    return sum
def add1(a,*b,**c):
    sum=a+add(*b)
    for x,y in c.items():
        sum=sum+y
    return sum

j=add1(10,10,10,x=10,y=20)
print ("sum " + str(float(j)))
k=add(10,30,30)
print(k)

