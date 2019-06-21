
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
#delete the nth element after storing in a variable
print ("popping nums(1)")
x=nums.pop(1)
print (x)
print (nums)
#clear complete list
nums.clear()
print (nums)
#to delete the list. It will not further exist in the memory
del nums #clears the nums list from memeory. It can also be used to clear anything
#print (nums)
nums=[1,4,2,7,9,10]
s=sorted (nums)
print ("nums original")
print (nums)
print ("sorted applied")
print (s)
nums.sort ()
print ("sort applied")
print (nums)
