# Collection - List, Dictionary, Tuple

# List
A = [23,'Shubham', 23.7,89.4,'Anuja',69.3]
print(A)

# Indexing
print(A[0])
print(A[1])
print(A[2])

# Negative Indexing
print(A[-1])
print(A[-2])

# Slicing(last value is (n-1))
print(A[0:3])
print(A[2:5])
print(A[:4])
print(A[:-1])

# Updating - Append, Insert, Delete
A[1] = 7
A[2] = 'Shubham'
print(A)

A.append("Mahadev")
print(A)

A.insert(2,'Kalpana')
print(A)

del A[1]
print(A)


# Dictionary(Key & Value)
B = {7:'Beckham', 10:'Messi', 11:'Bale'}
print(B)

#Indexing
print(B[11])

#Can't perform slicing as keys are not in chronological order

#Updating
B[7] = 'Ronaldo'
print(B)

B[8] = 'Kroos'
print(B)

B[9] = 10
print(B)

# Tuple(immutable)
C = (24, 'Sachin', 89.74, 'Virat', 69.3)
print(C)

D = list(C)
D[1] = 'Rohit'
print(D)

C = tuple(D)
print(C)


# Conditional Statements
#Example 1
E = 58
F = 96

if E < F:
    print("IF STATEMENT SATISFIED")

#Example 2
G = 96
H = 58

if G < H:
    print("IF STATEMENT SATISFIED")

print("IF STATEMENT SKIPPED")

#Example 3
Marks = 48

if Marks > 40:
    print("PASSED")
else:
    print("FAILED")

#Example 4
Marks = 38

if Marks > 40:
    print("PASSED")
else:
    print("FAILED")

#Example 5
Marks = 68

if Marks > 60:
    print("First Class")
elif Marks > 40:
    print("PASSED")
else:
    print("FAILED")

#Example 6
Marks = 88

if Marks > 80:
    print("First Class with Distinction")
elif Marks > 60:
    print("First Class")
elif Marks > 40:
    print("PASSED")
else:
    print("FAILED")

#Example 7(Nested if Condition)
Marks = 88
Subject = "English"

if Subject == "MATHS":
    if Marks > 80:
        print("First Class with Distinction")
    elif Marks > 60:
        print("First Class")
    elif Marks > 40:
        print("PASSED")
    else:
        print("FAILED")
else:
    print("Unidentified Subject")

# Example 8
I = 4

if I % 2 == 0:
    print("I is even")
else:
    print("I is odd")

# Example 9
I = 5

if I % 2 == 0:
    print("I is even")
else:
    print("I is odd")