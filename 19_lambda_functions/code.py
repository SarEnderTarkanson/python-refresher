# add = lambda x, y: x + y

# print(add(5,7))

# x = (lambda x, y: x + y)(5, 7)

# print(x)

def double(x):
    return x * 2

sequence = [1, 3, 5, 7]
# doubled =  [x * 2 for x in sequence]

# print(doubled)

doubled = list(map(double, sequence))

print(doubled)

