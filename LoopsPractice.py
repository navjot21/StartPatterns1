"""# Write a program to print first 10 natural number
print("First 10 natural numbers are: ")
for i in range(1, 11):
    print(i)

# Write a program to print first 10 even numbers
print("First 10 even numbers are here: ")
for i in range(2, 22, 2):
    print(i)

# Write a program to print first 10 odd numbers
print("First 10 odd numbers are here: ")
for i in range(1, 21, 2):
    print(i)

# Write a program to print first 10 even numbers in reverse order.
print("First 10 even numbers in reverse are here: ")
for i in range(20, 0, -2):
    print(i)

# Write a program to print table of a number accepted from user.
n = int(input("Enter the number you want the table for: "))
for i in range(1, 11):
    c = n * i
    print(n, '*', i, '=', c)

# Write a program to display product of the digits of a number accepted from the user
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = a * b
print(c)

# Write a program to find the factorial of a number.
n = int(input("Enter the number for factorial: "))
p = 1
while n > 0:
    p = p * n
    n = n - 1
print(p)

# Write a program to find the sum of the digits of a number accepted from user
a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = a + b
print("the sum of two number is: ", c)
"""
# Write a program to check whether a number is prime or not.
n = int(input("Enter the number to find it is prime or not: "))
for i in range(2, n):
    if n % i == 0:
        print("this is not  prime number")
        break
else:
    print("this is a prime number")