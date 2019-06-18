a="Hello"
b="Hello"
print ("id of variable a " + str(id(a)))
print ("id of variable b " + str(id(b)))
if a is b:       #is checks for id
    print("equal")
else:
    print("not equal")