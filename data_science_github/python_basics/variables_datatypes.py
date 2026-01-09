# Printing a Statement
print("HeLLo World")

print("'Hello World'")

print('"Hello World"')

print("Shubham's World")

# Creating a Variable
S = 23
print(S)

#Defining Datatypes
a = 10
b = ("Shubham")
c = 2.3
print(type(a))
print(type(b))
print(type(c))

#Code 1
A = 5
B = 85
C = A + B
print(C)

#Code 2
D, E = 5, 85
print(D+E)


# Global & Local Variable
g = 1 # Global Variable
def add_5():
    h = 10
    g = 100 # Local Variable
    return h, g
print(add_5())
print(g)