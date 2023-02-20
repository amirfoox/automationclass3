# create our own functions

# use pass instead of print hello to return an empty function

def our_function():
    """
    This is my first function. It just prints 'hello'
    :return: None
    """
    print("hello!!!")


def our_function2(name):
    """
    This is my second function, it prints hello {name}
    :arg name: the name of the person to greet
    :return: None
    """
    print(f"Hello {name}!")


our_function()
help(our_function)  # prints the docstring of the function

help(our_function2)

our_function2("Amir")


def our_function3(a, b, c):
    """
    Adds a, b, c and prints the result
    :param a: first value
    :param b: second value
    :param c: third value
    :return: None
    """
    result = a + b +c
    print(f"the result of adding: {a}, {b}, {c} is {result}")


our_function3(1, 2, 3)


def our_function4(a, b, c):
    """
    Adds a, b, c and prints the result
    :param a: first value
    :param b: second value
    :param c: third value
    :return: the result of a+b+c
    """
    result = a + b + c
    return result

# examples of uses with function4

print(our_function4(4, 6, 8))
print(2 * our_function4(4, 6, 8))
print(0.5 * our_function4(4, 6, 8))

result = our_function4(10, 20, 30)
result2 = our_function4(20,30, 15)
print(f"I can use this {result> result2}")

result = (our_function4(b=10, c=20, a=10))  # the order of the parameters doesn't matter
print(result)

def our_function5(a=10, b=20, c=1):
    """
    Adds a, b, c and prints the result
    :param a: first value
    :param b: second value
    :param c: third value
    :return: the result of a+b+c
    """
    result = (a + b) * c
    print(result)


print(our_function5())
print(our_function5(c=100))
print(our_function5(a=1000, c=0))
print(our_function5(22, c=30))  # ok
# print(our_function5(b=22, 30)) # not ok (Positional argument after keyword argument)


def f() -> int:
    """
    return 10 times the value of global variable a
    :return: int
    """
    a = 1
    return "xxxxx"


print(f())
print(f"a = {a}")

