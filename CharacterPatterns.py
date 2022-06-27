# this the program to print the characters in the program
# to make a character patterns we need to use the ASCII code
# A(65)-Z(90) , a(97)-z(122), 0(48)-9(57)

n = int(input("Enter the number of rows: "))

# Increment triangle program for character pattern only A
print("Right angle triangle for character pattern A")
for i in range(n):
    for j in range(i + 1):
        print(chr(65), end=' ')
    print()

# Reverse right angle triangle program for character pattern only A
print("Reverse right angle triangle program for character pattern only A")
for i in range(n):
    for j in range(i,n):
        print(chr(65), end=' ')
    print()

# Right right angle triangle program for character pattern only A
print("Right right angle triangle program for character pattern only A")
for i in range(n):
    for j in range(i,n):
        print(" ", end=' ')
    for j in range(i+1):
        print(chr(65), end=' ')
    print()

# Reverse Right right angle triangle program for character pattern only A
print("Reverse Right right angle triangle program for character pattern only A")
for i in range(n):
    for j in range(i + 1):
        print(" ", end=' ')
    for j in range(i, n):
        print(chr(65), end=' ')
    print()

# Triangle program for character pattern only A
print("Triangle program for character pattern only A")
for i in range(n):
    for j in range(i,n):
        print(" ", end=' ')
    for j in range(i+1):
        print(chr(65), end=' ')
    for j in range(i):
        print(chr(65), end=' ')
    print()


# Reverse Triangle program for character pattern only A
print("Reverse Triangle program for character pattern only A")
for i in range(n):
    for j in range(i + 1 ):
        print(" ", end=' ')
    for j in range(i, n):
        print(chr(65), end=' ')
    for j in range(i, n-1):
        print(chr(65), end=' ')
    print()

# right angle triangle and right-right angle triangle
print("right angle and right-right angle triangle")
for i in range(n):
    for j in range(i+1):
        print(chr(65), end=' ')
    for j in range(i,n):
        print(" ", end=' ')
    for j in range(i,n-1):
        print(" ", end=' ')
    for j in range(i+1):
        print(chr(65), end=' ')
    print()


# reverse right angle triangle and right-right angle triangle
print("Reverse right angle and right-right angle triangle")
for i in range(n):
    for j in range(i,n):
        print(chr(65), end=' ')
    for j in range(i + 1):
        print(" ", end=' ')
    for j in range(i + 1):
        print(" ", end=' ')
    for j in range(i,n):
        print(chr(65), end=' ')
    print()

# Increment triangle program for character pattern from starting A consecutively each character in one ROw
print("Increment triangle program for character pattern from starting A consecutively each character in one ROw")
p = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(p), end=' ')
    p+=1
    print()

# Increment triangle program for character pattern from A
print("Increment triangle program for character pattern from A")
p = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(p), end=' ')
        p+=1
    print()


# On right angle triangle and then reverse right angle triangle form the row where right ends
print("On right angle triangle and then reverse right angle triangle form the row where right ends")
n = int(input("Enter the number of Rows: "))
for i in range(5):
    for j in range(i + 1):
        print("*", end=' ')
    print()
for i in range(5, 10):
    for j in range(i + 1):
        print(" ", end=' ')
    for j in range(i, n):
        print("*", end=' ')

    print()
    
"""for i in range(5):
    for j in range(i + 1):
        print("*", end=' ')
    print()
for i in range(5, 11):
    for j in range(5, 11):
        print(" ", end=' ')
    for j in range(i, n):
        print("*", end=' ')
    print()"""