# Time Complexity
# It is a branch of CS where we are going to quantify the no. of operations the amount of time it has taken to run an algorithm.
# No. of operations it takes to quantify an operation.

# Whenever we are describing an algorithm always consider the worst case scenario.

# While quantifying we use a mathematical notation - Big O, describes a limiting function

# - Constant time complexity
#   Usually defined by O(1), the code takes same no. of operation to perform, regardless of the input.

# - Linear time complexity
#   Denoted by O(n), the code increases no. of operations in accordance with the input.

# - Logarithmic time complexity
#   Denoted by O(log(n)), the code reduces over each operational step
# Binary Search(merge-sort)
A = [1, 2, 3, 4, 5, 7, 9]

def binary(a, n):
    low = 0
    high = len(a) - 1 # to match the index
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if a[mid] < n:
            low = mid + 1

        elif a[mid] > n:
            high = mid - 1

        else:
            return mid

    return ("no number present")

print(binary(A, 9))


# - Exponential time complexity
#   Denoted by O(2^n), the code doubles no. of operation in accordance with the input.
# Fibonacci Series(Solve for a list)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(6))


# Memory Management
# Python takes care of allocation & deallocation of memory automatically, based on the reference count.
# Euclid Algorithm - Find the GCD, matrix multiplication, eigen values & eigen vectors
def gcd(a, b):

    while b != 0:
        a, b = b, a  % b
    return a

print(gcd(18, 12))
