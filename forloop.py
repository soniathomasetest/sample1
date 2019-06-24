marks=[11,22,33,44]
sum=0
for x in marks:
    print (x)
    sum=sum+x
print ("Total marks " + str(sum))
print (type(sum))
print ("avg marks " + str(sum/len (marks)))
'''len function gives length of list'''

#2nd program
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)