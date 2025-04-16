# Create a list containig the table of 39.
# We can make list like this the code is below but this is very long method 
# a = 39 
# table= [] 
# for i in range(1,11):
#     table.append(39*i)
# To do the same thing in short cut 
table = [5*i for i in range(1,11)]
print(table)   

# Print the 5 number from 1 to 5
num = [i for i in range(1,6)]
print(num)


# Write a for loop to print only the marks that are greater than 50.
marks = [45,67,89,32,90]
numb = [i for i in marks if i>50 ]
print(numb)