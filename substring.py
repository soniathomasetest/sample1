msg="Hello World"
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
#operations on arrays
nums=[12,23,34,56,67,78,23]
print (len(nums))
print (nums[0])
print (nums[0:7])
print (nums[0:len(nums)])  #dynamically calculates length of array
print (nums[-7:4])
#to add elements to list
nums.append(33) #no need of assignment. string is immutable. but numeric list is mutable
print (nums)
#to insert in between
nums.insert(1,100)
print (nums)
#to extend to the list
nums.extend({200,300,400}) #it can be anything. It can be lsit or set or a tuple
print (nums)
nums.append(1)
print (nums)
# to remove value 100
nums.remove(100)
print (nums)
#to delete nth element
del nums[1]
print (nums)
#clear complete list
nums.clear()
print (nums)
#to delete the list. It will not further exist in the memory
del nums #clears the nums list from memeory. It can also be used to clear anything
print (nums)
