# Dictionary methods in pyhton 
marks = {"Kshitij":51, "Manish":83, "Aayush": 92}
print(marks.keys()) # Print only key of marks dictionary.
print(marks.values()) # Print only value of marks dictionary
print(marks.items()) # Print particular key with value
# marks.clear() # Clear whole dictionary 
marks.pop("Kshitij")
print(marks)