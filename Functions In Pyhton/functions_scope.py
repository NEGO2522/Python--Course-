# Local Varaible and Global Variable 
x = 10 # Global Varaible 
def my_func():
    x = 5  # Local Varaible 
    print(x) # Output: 5

my_func()
print(x)

# Using the global Keyword
x = 10 # Global Variable 

def modify_global():
    global x 
    x = 5 # Modifes the global x 

modify_global()
print(x) # Output : 5


def sum (a,b):
    print("Hey, I'm summing")
    global z # Modilfy Global z
    z = 0 
    c = a+b
    return c 
z =3
print(sum(3,12))
print(z)