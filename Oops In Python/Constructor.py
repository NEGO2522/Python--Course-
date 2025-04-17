class Employee:
    company = "NEGO"

    def __init__(self, salary, name, bond): # This is an constructor 
        self.salary = salary # Create an Object Attribute of salary 
        self.name = name 
        self.bond = bond
     
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the Founder is {self.name}. Profit of NEGO is {self.salary}.The Owner Company Bond is for {self.bond}")
    
e1 = Employee(200,"Kshitij Jain","Life Long")
e2 = Employee( 500000,"Manish Kumar", "5Year")
e3= Employee(10000,"Aayush Bhardwaj", "10 Year")
print(e1.get_salary())
print(e2.get_salary())