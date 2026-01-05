# *args

def add(*args):
    summ = 0
    for n in args:
        summ +=n
    return summ

def example_function(*args):
    print(type(args))  # Output: <class 'tuple'>
    print(args)

example_function(1, 2, 3)  # Output: (1, 2, 3)


# print(add(1,2,3,4,5))


# **kwargs -->

def calculate(n, **kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

def example_function(**kwargs):
    print(type(kwargs))  # Output: <class 'dict'>
    print(kwargs)

example_function(a=1, b=2, c=3)  # Output: {'a': 1, 'b': 2, 'c': 3}
