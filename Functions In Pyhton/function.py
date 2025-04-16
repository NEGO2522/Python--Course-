# a = 2 
# b = 3 
# c = 4

# average = (a+b+c)/3
# print(average)

# a1 = 23
# b1 = 24
# c1 = 25
# average1 = (a1+b1+c1)/3
# print(average1)

# To do The same thing 100 time it will make our code so much long to do this in short we use function.

def average_num(a,b,c): # def is a keyword for making functions in python and the () brackets tell the parameter of this function like a,b,c are the parameter of function inside the paranthesis()
    average = (a+b+c) /3
    print(average);  # Till Yet we only define function nothing esle not calling a function so it not execute up till now. 
    return average  # Return the value so we can use it further in our program or to use the average later.

o1 = average_num(2,3,4); # Calling the function.
o2 = average_num(4,2,2)

print(o1)
print(o2)

