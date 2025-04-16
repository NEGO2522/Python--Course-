# Strings methods in Python 
text = "hello world" # Strings are immutable in python.(Can Not change)
# s[0] = "R" # You cannot do this

s = len(text)  # This is len function
print(s)  

# changing case methods
print(text.upper(),);
print(text.lower()); 
print(text.capitalize());
print(text.title());

# Remove whitespace
text = " hello world "
print(text.strip()) 
print(text.lstrip()) 
print(text.rstrip())

# Finding and Replacing
text = "Python is fun" 
print(text.find("is")) # Ouptut : 7
print(text.replace("fun","awesome")) # Output: Python is awesome.

# Spliting and Joining 
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits) # Output: ['apple', 'banana','orange']

new_text = " - ".join(fruits)
print(new_text) # Output:- "apple -banana -orange"


text ="Python123" 
print(text.isalpha()) # Output:  False  # This tells that the value have only alaphabes in the srting no digits or whitespace in this string.
print(text.isdigit()) # Ouput: False # This tells that isdigit have only numeric value no character inside string
print(text.isalnum()) # Output: True # This tells that isalnu have both type of alphanumeric character in which alphabets and numeric digit both are there.
print(text.isspace()) # Output: False # This tell that isspace has only whitespace character or not.