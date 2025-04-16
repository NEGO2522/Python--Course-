 # Positional  arguments.
def add (a,b):
    x = a+b;
    return x;

c = add(3,5); # here we call the function add() and the arguments of that fucntion is 3,5
print(c);

 # Default arguments
def add(a,b,plus=0):
    x = a +b + plus
    return x
c = add(3,5,2)
print(c)

 # Keyword arguments
def add(a,b):
    x = a+b
    return x

c1 = add(b=5, a=3)
print(c1)