#1. simple triangle 
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()  

#2. right angle triangle
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()   

#3. Inverted triangle
for i in range(1, 6):
    for j in range(1, 6-i+1): #formula N=6, N-i+1
        print("*", end="")
    print()   

#4. square pattern 
for i in range(1, 6):
    for j in range(9):
        print("*", end="")
    print()   

#5. Right-alligned triangle
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")    
    print() #right side triangle = spaces decreases, stars increase

#6. Pyramid pattern 
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()        

