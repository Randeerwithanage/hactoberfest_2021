
#marks counter ------>


class Student:
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
         
    def accept(self):
        Name=str(input())
        Rollno=int(input())
        marks1=int(input())
        marks2=int(input())
        ob = Student(Name, Rollno, marks1, marks2 )
        lst.append(ob)
  
       #count
    def display(self, ob):
            print("Name   : ", ob.name)
            print("RollNo : ", ob.rollno)
            print("Marks1 : ", ob.m1)
            print("Marks2 : ", ob.m2)
            print("\n")    
         
    def search(self, rn):
        for i in range(len(lst)):
            if(lst[i].rollno == rn):
                return i       
  
                                      
    def delete(self, rn):
        i = individual.search(rn)  
        del lst[i]
  
       
    def update(self, rn, No):
        i = individual.search(rn)
        roll = No
        lst[i].rollno = roll;
         

lst =[]
individual = Student('', 0, 0, 0)
  


individual.accept()
individual.accept()
individual.accept()

     #print statements---->>>>>>.    


print("\nList of Students\n")
for i in range(len(lst)):    
    individual.display(lst[i])
             

print("\nStudent Found: ")
s = individual.search(2)
individual.display(lst[s])
         

individual.delete(2)
print("List after deletion")
for i in range(len(lst)):    
    individual.display(lst[i])
             

individual.update(3, 2)
print("List after updation")
for i in range(len(lst)):    
    individual.display(lst[i])
             

