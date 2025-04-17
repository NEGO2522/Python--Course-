# For Addition
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum( self, p):
        return point((self.x+p.x), (self.y +p.y))
    def print_point(self):
        return f"X is {self.x} and Y is {self.y}"
    def __add__(self,p):
        return point((self.x+p.x), (self.y +p.y))
p1 = point(3,2)
p2 = point(6,3)

# p = p1.sum(p2) # Returning new point which is sum of p1 and p2
p = p1+p2 # We overloaded the + operator by writing __add__ function.
print(p.print_point())

# For subtraction 
class Point:
    def __init__(self, x, y):
        self.x = x;
        self.y = y; 
    def __sub__(self,p):
        return Point((self.x-p.x),(self.y-p.y));
    def print_point(self):
        return f"X is {self.x} and y is {self.y}";
p1 = Point(23,24);
p2 = Point(5,12);
p = p1-p2  # (18,12)
print(p.print_point())

# For multiplication 
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self,p):
        return point((self.x*p.x),(self.y*p.y))
    def print_point(self):
        return f"X is {self.x} and y is {self.y}"
    
p1 = point(21,12)
p2 = point(7,9)
p = p1*p2
print(p.print_point())

# For division 
class point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __truediv__(self,p):
        return point((self.x/p.x),(self.y/p.y))
    def print_point(self):
        return  f"X is {self.x} and Y is {self.y}"
p1 = point(12,28)
p2 = point(2,7)
p = p1/p2
print(p.print_point())