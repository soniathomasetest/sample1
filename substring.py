msg="Hello World"
if "World" in msg :
    print("substring is present")
else:
    print("substring is absent")
    
print (msg[0:6])
print (len(msg))
print (msg[-1:-5])
msg=msg+"!!!"
newmsg=msg
print (msg);
print (newmsg)
# + is to concatenate
# to replace a substring
msg=msg.replace("World","India")
print (msg)
# to print as many times you want
print (msg*3)
# to trim the white spaces on the left and right of the string
print (msg.strip())
#to convert to upper left trim and right trim
print (msg.upper().strip())
print (msg.upper().rstrip())
print (msg.upper().lstrip())
#given one string names, split based on ,
names="Kumar,anoop,james , ravi"
data=names.split(",")
print (data)
print (data[2])
print (id(data))
print (id(data[1]))
print (id(data[2]))
##reverse operation of split is join
msg="!".join(["Hello","how","are","you"])
print (msg)


