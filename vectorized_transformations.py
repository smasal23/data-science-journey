# lambda function
def add_1(a,b):
    return a + b
print(add_1(1, 2))

# Example(x,y are called as arguments)
add_2 = lambda x, y: x + y
print(add_2(3, 4))
print(add_2('shub', 'ham'))
print(add_2(1, 2) - 9)

# Example
mul_1 = lambda x: x * x
print(mul_1(7))

# Example
some = lambda x: "even" if x % 2 == 0 else "odd"
print(some(7))


# Map, Filter & Reduce

# Map(n to n function)
# Example 1
A = ['Shubham', 'Shubha', 'Shubh', 'Shub', 'Shu']
print(list(map(str.upper, A)))

# Example 2
B = [1,2,3,4,5]
def sqr(a): # Usecase 1
    return a * a
print(list(map(sqr, B)))
print(list(map(lambda x: x * x, B))) # Usecase 2


# Filter
# Example 1
C = ['Ronaldo', 'Beckham', 'Bale', 'Messi']
def remove(x):
    return 'a' in x
print(list(filter(remove, C)))

# Example 2
D = [1,2,3,4,5,6]
def  even(y):
    return y % 2 == 0
print(list(filter(even, D)))


# Reduce
# Example 1
E = [1,2,3,4,5,6]
from functools import reduce
print(reduce(lambda x,y: x + y, E))

# Combination of Map, Filter, Reduce
# USECASE 1
prices = [560, 480, 790, 220, 690]
def add_tax(prices): # Increase by 10%
    return prices * 1.10
taxed_price  = list(map(add_tax, prices))
print(taxed_price)

def expensive(prices): # Remove prices below 250
    return prices > 250
expensive_items = list(filter(expensive, taxed_price))
print(expensive_items)

def total(a, b):  # Total of the remaining prices
    return a + b
total_price = reduce(total, expensive_items)
print(total_price)

# USECASE 2
print(reduce(lambda a, b: a + b, filter(lambda x: x > 250, map(lambda y: y * 1.10, prices)))) # understand this later

# Iterators
D = [1,2,3,4,5,6]
nums = iter(D)
print(nums)
print(next(nums))
print(next(nums))