marks = [21,23,3,4,78]
extra_marks = [67,87,56]
print(marks) # The original One 
# List method 
marks.append(63) # This will change the original list 
marks.pop() # Remove last element from the list 
marks.insert(1,7) # 7 will insert at index 1
marks.extend(extra_marks)  # append extra_marks at the end of the marks list.
extra_marks.reverse() 
extra_marks.sort()
print(extra_marks)
print(marks)

