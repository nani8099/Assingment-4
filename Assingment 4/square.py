#Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]

l=[4,5,2,9]
def square(x):
    return x*x
print(list(map(square,l)))

# [OR]

lst1 = [4,5,2,9]
data = list(map(lambda x:x**2,lst1))
print(data)


# OUTPUTS FOR BOTH PROGRAMS:

# [16, 25, 4, 81]








