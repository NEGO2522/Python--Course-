# Recursion occurs when a function caless itself to solve a problem.

''' 0 1 1 2 3 5 8 13 and so 
on that are called 
as fibonacci sequece values.
fib(0) = 0
fib(1) = 1
fib(2) = fib(1) + fib(1) = 2
fib(3) = fib(1) + fib(2) = 3
fib(1) = fib(2) + fib(3) = 5
fib(n) = fib(n-2) + fib(n-1)  for n = 0 and n = 1 this formula not Work.
fib(5) = fib(3) + fib(5) = 8
'''

def  fib(n):
     # Base case of recursion.
     if(n==0 or n ==1):
          return n
     return fib(n-2) + fib(n-1);

result = fib(4)
print(result)

# Without recursion the hardest way to solve the problem.
fib(2) + fib(3)
fib(1)+fib(1) + fib(3)
1+1 + fib(1)+fib(2)      # To calculate fib 4 value 
1+1+1+fib(1)+fib(1)
1+1+1+1+1 
