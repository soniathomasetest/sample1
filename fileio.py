f=open("testfile.txt")
x=f.readlines()
print (x)
class Student:
    def __init__(self,name,total):
        self.name=name
        self.total=total

s=[]
for item in x:
    print (item)
    val=item.split(',')
    total=int(val[2])+int(val[3])+int(val[4])
    print ("total marks of " + val[1] + " is " + str(total))
    s.append(Student(val[1],total))    #writing to an array of objects
snew=sorted(s, key=lambda s: s.total,reverse=True)


f1=open("ranklist","w+")
j=1
for i in snew:
    f1.writelines(str(j) + " " + i.name+ " " + str(i.total)+ "\n")
    j=j+1

'''
print ((snew[0].name),snew[0].total)
print ((snew[1].name),snew[1].total)
print ((snew[2].name),snew[2].total)
print ((snew[3].name),snew[3].total)

'''
