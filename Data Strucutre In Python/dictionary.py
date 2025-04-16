# Dicitonary are key-value pairs in python.

marks = {
    "Kshitij": 51,
    "Aayush" : 59,
    "Karan" : 60,
    "Manish": 75
};
print(marks) # Print all the values in the form of key value pairs where key are Kshitij,Aayush,Manish,Karam and values are 51,59,60,75
print(type(marks))

family_age = {
    "Kshitj":18,
    "Sakshi": 21,
    "Rekha Jain": 15,
    "Manoj Kumar Jain" : 19,
    "Madan Lal Patodi": 17
}
print(family_age)

# to accessing a value in dictionary 
print(family_age["Manoj Kumar Jain"]) # 19
print(marks["Manish"]) # 75
# To modify a value in dictionary 
marks["Karan"] = 93 # Updating value
print(marks)
# To make a new key value pair in family_age 
family_age["Shruti Jain"] = "22"
print(family_age)