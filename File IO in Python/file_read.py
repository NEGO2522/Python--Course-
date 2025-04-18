''' Two Types of File:-
1. Text File- .c,.py,.txt etc.
2. Binary File- .pdf,.mp4,.mp3,.jpg etc 
'''

# This will read the file called as file.txt.
f = open("file.txt", "r")  # By default r mode called as read mode in open function.
data = f.read()
print(data)
f.close()

