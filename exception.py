#exception handling in python
l=[10,20,30,'a']
print (l)
print (type(l))
try:
    print(l[3] + 5)
    print (l)
    print(l[20])
except IndexError as e1:
    print (e1)
    print("oops!out of range")
except ZeroDivisionError as e2:
    print (e2)
    print("oops!you are trying to divide by 0")
#Exception is the super class
except Exception as e3:
    print (e3)
    print ("something wrong")
#finally clause gets executed whether there is an exoeption or not
finally:
    print(l)
print(l[1])
