# Class is a blueprint or a template. Eg:- Form for an Exam That contains name, age , Father's name , Mother's name ect.
# Object : Specific Instance create form the template(class) Eg. Form which contain the data of John Doe.  This specefic Object is an instance of a class.

# Creating a class called Employee.
class Employee:
    company = "NEGO"
    def get_salary(self): # Self is important here because self is a way to reference the object of the class which is being created.
        return 34000
# Creating a Object for Class Employee.
e = Employee()
print(e.get_salary())
e2 = Employee()
print(e2.get_salary())
print(e2.company)



# Create a Class called Student 
class Student:
    school = "Bright Future School"
    def get_grade(self):
        return "A+"
 # Create a object for class Student 
teacher = Student()
print(teacher.get_grade()) 
print(teacher.school)



# Create a class called Car 
class car:
    brand = "Tesla"
    def get_speed(self):
        return 150;
# Create a Object for class car 
founder = car()
print(founder.get_speed())


