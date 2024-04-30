# # Lambda

# k = lambda a, b : a+b

# print(k(5, 10))

def cube(x):
    return x**3

def filter_func(x):
    if x%2 == 0:
        return x

l = [1,2,4,5,6,3]

newl = list(map(cube, l))
print(newl)

latestl = list(filter(lambda x: x%2==1, l))
print(latestl)
