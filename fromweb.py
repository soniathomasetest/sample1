# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2,5,6,1]
print (randomList)

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)
