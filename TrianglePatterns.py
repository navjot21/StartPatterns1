# print different types of Triangle patterns
n = int(input("Enter the number of Rows: "))

# left right angle triangle
print("Left Right angle triangle: ")
print(" ")
for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    print()

# reverse left right angle triangle
print("Reverse right angle triangle: ")
print(" ")
for i in range(n):
    for j in range(i, n):
        print("*", end=' ')
    print()

# right right angle triangle
print("Right Right angle triangle: ")
print(" ")
for i in range(n):
    for j in range(i,n-1):
        print(" ", end=' ')
    for j in range(i+1):
        print("*", end=' ')
    print()

# reverse right right angle triangle
print("Reverse Right Right angle triangle: ")
print(" ")
for i in range(n):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()

# Two right angle triangles
print("Two right angle triangle: ")
print(" ")
for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    for j in range(i, n-1):
        print(" ", end=' ')
    for j in range(i+1):
        print("*", end=' ')
    print()


# one right angle triangle and one reverse right angle triangle
print("One right angle and reverse right angle triangle: ")
print(" ")
for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    for j in range(i,n-1):
        print(" ", end=' ')
    for j in range(i, n):
        print("*", end=' ')
    print()
# Simple triangle
print("Simple triangle: ")
print(" ")
for i in range(n):
    for j in range(i, n-1):
        print(" ", end=' ')
    for j in range(0, i+1):
        print("*", end=' ')
    for j in range(i):
        print("*", end=' ')
    print()

# reverse simple triangle
print("reverse simple triangle")

for i in range(n):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i, n-1):
        print("*", end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()
# Diamond triangle
print(" Diamond triangle: ")
print(" ")
for i in range(n-1):
    for j in range(i, n-1):
        print(" ", end=' ')
    for j in range(0, i+1):
        print("*", end=' ')
    for j in range(i):
        print("*", end=' ')
    print()
for i in range(n):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i, n-1):
        print("*", end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()


# reverse diamond means pascal triangle
print("sandglass triangle")
print(" ")
for i in range(n-1):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i, n-1):
        print("*", end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()
for i in range(n):
    for j in range(i, n-1):
        print(" ", end=' ')
    for j in range(0, i+1):
        print("*", end=' ')
    for j in range(i):
        print("*", end=' ')
    print()

# left pascal triangle
print("Left Pascal triangle: ")
print(" ")
for i in range(n-1):
    for j in range(i+1):
        print("*", end=' ')
    print()
for i in range(n):
    for j in range(i, n):
        print("*", end=' ')
    print()

# right pascal triangle
print("right Pascal triangle: ")
print(" ")
for i in range(n-1):
    for j in range(i+1):
        print("*", end=' ')
    print()
for i in range(n):
    for j in range(i, n):
        print("*", end=' ')
    print()

# left pascal triangle
print("Left pascal triangle: ")
print(" ")

for i in range(n-1):
    for j in range(i,n-1):
        print(" ", end=' ')
    for j in range(i+1):
        print("*", end=' ')
    print()
for i in range(n):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()

# butterfly triangle
print("butterfly triangle: ")
print(" ")
for i in range(n-1):
    for j in range(i+1):
        print("*", end=' ')
    print()
for i in range(n):
    for j in range(i, n):
        print("*", end=' ')
    print()
for i in range(n-1):
    for j in range(i,n-1):
        print(" ", end=' ')
    for j in range(i+1):
        print("*", end=' ')
    print()
for i in range(n):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()
for i in range(n):
    for j in range(i, n):
        print("*", end=' ')
        for j in range(i):
         print(" ", end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()
