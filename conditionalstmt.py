a=int(input('enter the first number'))
b=int(input('enter the first number'))
result=0
if (a>=b):
    result=a+b
else:
    result=a-b
print(result)
#statement re written as
result= a+b if a>=b else a-b
print(result)