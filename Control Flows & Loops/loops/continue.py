# for i in range(1, 20):
#     if i == 10:
#         continue  # Skip this iteration when i == 10
#     print(i)



# Write a program that prints all numbers from 1 to 20, but skip the numbers that are divisible by 3 using the continue statement.

for i in range(1,20):
    if i % 3 == 0:
        continue
    print(i)

print("End of this Program");