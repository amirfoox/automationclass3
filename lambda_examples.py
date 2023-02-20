# x = lambda n: n+n
#
# print(x(2), x(3), x(11))

print((lambda n: n+n)(120))


def increase(n):
    """
    Use to construct different increase functions
    :param n: The number of times to increase
    :return: a lambda function
    """
    return lambda x: x*n


double = increase(2)
triple = increase(3)
tenfold = increase(10)

print((double(11)), triple(11), tenfold(11))


power = lambda x, y: x ** y
print(power(2, 10))

# --------------- map, filter, reduce
print(list(map(double, [1, 2, 3, 4])))
# instead do a lambda:
print(list(map(lambda x: x+x, list(range(1, 100)))))

print(list(map(lambda x: 4*x, "abcdefghijklmnop")))


print(list(filter(lambda x: x < 5, list(range(-100, 100)))))


def is_prime(n):
    for i in range(2, n):
        if n % 1 == 0:
            return False
    return True


print("Here are the first prime numbers")
print(list(filter(is_prime, list(range(2, 1000)))))


# reduce



