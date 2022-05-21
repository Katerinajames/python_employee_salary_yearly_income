class Employee:
 def __init__(self,first,last,monthlysalary):
       self.first=first
       self.last=last
       
       if monthlysalary>400 and monthlysalary<=500:
            self.monthlysalary=monthlysalary
       else:
           raise ValueError("Monthly salary must be between 400 and 500 euros")
 
 def yearlysalary(self):
     return  self.monthlysalary*12
  

print("----------------------------------")

e=Employee("Kat","Papa",401)

print ("Our employee's monthly salary is",e.monthlysalary,"euros")
print("Our employee's yearly income is",e.yearlysalary(),"euros")

