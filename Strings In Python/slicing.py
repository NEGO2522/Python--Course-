name = "Kshitij55987957"
print(name[0:2]) # Goes from 0 to 2-1 i.e 0 to 1. output(Ks)

print(name[2:-1]) # output (hiti) same as [2:6]

# Step Parameter in slicing
print(name[0:15]) # Kshitij55987957
print(name[0:10:1]) # skip n-1 character here n is 1 which is step parameter # it skip 0 characters
print(name[0:10:2]) # It skip 1 character.
print(name[0:10:3]) # It skip 2 character.

print(name[:4]) # before 4 all character will be rpinted . Output :- Kshi. Same as [0:4]
print(name[1:]) # after one all character will be printed. Output :- shitij55987957 same as [1:15]