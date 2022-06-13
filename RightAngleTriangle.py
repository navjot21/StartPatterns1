# Start patterns print using For LOOP and nested For Loop
#Right Angle Triangle

n = int(input("Enter the number of Rows: "))

for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    print()