'''student={"Ajay":12,"Rita":34}
print(student)
#student.add["Reenu"]=12
student["Reenu"]=12
print (student)
#student ["Ajay"]
#add one dictionar to another
student.get("name")

student.keys()
#iterate value of dictionay
'''
studentinfo={ "101":{
    "name":"anil","email":"anil@add.com",
    "marks":{"sem1":100,"sem2":200,"sem3":200
    }},
               "102":{
                   "name": "Ramu", "email": "ramu@add.com",
                   "marks": {"sem1": 10, "sem2": 20, "sem3": 30
               }}
}

for roll_no,details in studentinfo.items():
    sum=0
    print(details)
    for m,n in details.items():
            if (m=="marks"):
                for i,j in n.items():
                    sum=sum+j
print ("rollno " + str(sum))
'''
print(studentinfo)
print (studentinfo["101"])
print (studentinfo["102"])
a= (studentinfo.get("101"))

'''

'''
print (studentinfo.values())
newdict=studentinfo.values()

print (newdict)

print (studentinfo.keys())
for x,y in studentinfo.values():
    print (x)
    print (y)
'''



'''print (studentinfo.keys())
e= studentinfo.get("marks")
print (e)
sum=e.get("sem1")+e.get("sem2")+e.get(sem3)
print (sum)
for'''