# def add(x,y=8):
#     print(x + y)

# add(x=5, y=5)

default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)

add(5)