# Loops - for & while
for i in range(10):
    print("HELLO SHUBHAM")

# Printing every element in a list
for i in A:
    print(i)

#Assignment 2
S = "shubham" # print only vowels
vowels = ['a', 'e', 'i', 'o', 'u']

for i in S:
    if i in vowels:
        print(i)

# While Loop
number = 0

while number < 5:
    print("Hi, I am Shubham")
    number = number + 1

#Assignment 1(Incomplete)!
J = [1,2,3,4,5,6] # print even and odd numbers
for i in J:
    if i % 2 == 0:
        print(i)


# Functions
A = 1
B = 2
C = A + B
print(C)

def add_1():
    A = 1
    B = 2
    C = A + B
    print(C)
add_1()

# Using Return Statement
def add_2():
    A = 1
    B = 3
    C = A + B
    return C
add_2()
print(add_2() + 3) # Requires a print command as within the function inherent print is not present.
print(add_2() - 3)

# Without giving hard-coded values of the variables
def add_3(A, B):
    C = A + B
    return C
print(add_3(96, 4))
print(add_3(9, 14))

# Giving a default parameter
def add_4(A, B = 10):
    C = A + B
    return C
print(add_4(90))
print(add_4(90, 90))


# Global & Local Variable
g = 1 # Global Variable
def add_5():
    h = 10
    g = 100 # Local Variable
    return h, g
print(add_5())
print(g)