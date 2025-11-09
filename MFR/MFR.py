from functools import reduce

#1
def cube(x):
    return x ** 3

numbers = []
for i in range(5):
    numbers.append(i)

cubes = list(map(cube, numbers))
print(1, cubes)


#2
def is_even(x):
    return x % 5 == 0

numbers = []
for i in range(11):
    numbers.append(i)

even_numbers = list(filter(is_even, numbers))
print(2, even_numbers)


#3
def the_product_of_numbers(x, y):
    return x * y

def odd_numbers(x):
    return x % 2 != 0

numbers = []
for i in range(11):
    numbers.append(i)

filterr_numbers = list(filter(odd_numbers, numbers))
print(3, filterr_numbers)
reducee_numbers = reduce(the_product_of_numbers, filterr_numbers)
print(3, reducee_numbers)