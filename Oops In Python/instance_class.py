class Employee:
    company = "NextGenOva" # this is class attribute 

    def __init__(self,salary,name,bond,compamy):
        self.salary = salary
        self.name = name 
        self.bond = bond 
        self.company = compamy

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = Employee(34000,"John Dick",2,"Tesla")
print(e1.company) # Will always print instance attribute  whenever present 
print(Employee.company) # This will always print the class attribute.

# Object IntroSpection 
print(dir(e1))