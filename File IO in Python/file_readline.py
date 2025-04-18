f = open("another.txt","w")
f.write("Kshitij Is a Good Boy\n")
f.write("I am Second Line\n")
f.write("This is amazing\n")
f.write("Twinkle Twinkle Little Star\n")
f.close()


# Now we use an function called readlines fuction 
f = open("another.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()


# Now we use an function called readline function
f = open("another.txt")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1, type(line1))
# print(line2, type(line2))
# print(line3, type(line3))
# f.close()

# Do the same thing using while loop.
line = f.readline()
while (line!= ""):
    print(line)
    line = f.readline()
f.close()