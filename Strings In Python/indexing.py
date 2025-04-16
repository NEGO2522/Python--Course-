# String Indexing in Python.

name = "Kshitij" 
# Possitive indexing
print(name[0]) # In programing Counting start from 0. therfore the output will be K.
print(name[1]) # s
print(name[2]) # h
print(name[3]) # i
print(name[4]) # t
print(name[5]) # i
print(name[6]) # j

# print(name[7]) # an error occur if we do this because last indexing is up to 6 character.
# Negitive indexing

#      -6-5-4-3-2-1
text = "Python"
#       0 1 2 3 4 5
print(text[-1]) # n (last character)
print(text[-2]) # o
print(text[-3]) # h
print(text[-4]) # t   # To convert it in possitive indices we simply do -4+6 it means the value of indices and the length of thtat word. And it Always work.
print(text[-5]) # y
print(text[-6]) # p
