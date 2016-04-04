from functools import reduce
from operator import add


# Uloha 1:
def square_generator(numbers):
    for number in numbers:
        yield number**2


# Uloha 2:
def square_map(numbers):
    return map(lambda x: x**2, numbers)


# Uloha 3:
def square_comprehension(numbers):
    return (x**2 for x in numbers)


# Uloha 4:
def cycle(list):
    index = 0
    length = len(list)
    while True:
        yield list[index % length]
        index += 1


# Uloha 5:
def factorial():
    value = 1
    number = 1
    while True:
        yield value
        number += 1
        value = value * number


# Uloha 6:
def digits(n, base):
    yield n % base
    n //= base
    while n > 0:
        yield n % base
        n //= base


# Uloha 7:
def factorial_digit_sum(N):
    number = 0
    factorial_generator = factorial()
    for _ in range(N):
        number = next(factorial_generator)
    return reduce(add, digits(number, 10))


# Uloha 8:
def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step


# Uloha 9:
def my_range_negative(start, stop, step=1):
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


# Uloha 10:
def items(dictionary):
    for key in dictionary:
        yield (key, dictionary[key])


# Uloha 11:
def pseudorandom(modulus, multiplier, increment, seed):
    previous_value = seed
    while True:
        previous_value = (multiplier * previous_value + increment) % modulus
        yield previous_value


# Uloha 12:
def sample(items):
    random_generator = pseudorandom(2**31, 1103515245, 12345, 1)
    length = len(items)
    while True:
        yield items[next(random_generator) % length]


# Uloha 13:
def sample_no_rep(items):
    random_generator = pseudorandom(2**31, 1103515245, 12345, 1)
    length = len(items)
    while length > 0:
        index = next(random_generator) % length
        yield items[index]
        items = items[:index] + items[index+1:]
        length -= 1


# Uloha 14:
def primes():
    count = 2
    while True:
        for x in range(2, count):
            if count % x == 0:
                break
        else:
            yield count
        count += 1


# Uloha 15:
def primes_memory():
    count = 2
    prime_list = []
    while True:
        for x in prime_list:
            if count % x == 0:
                break
        else:
            prime_list.append(count)
            yield count
        count += 1


# Uloha 16:
def nth_prime(n):
    prime = 0
    primes_generator = primes_memory()
    for _ in range(n):
        prime = next(primes_generator)
    return prime


# Uloha 17:
def pairs(list1, list2):
    iterators = iter(list1), iter(list2)
    stop_obj = object()
    while True:
        result = []
        for iterator in iterators:
            new_value = next(iterator, stop_obj)
            if new_value is stop_obj:
                return
            result.append(new_value)
        yield tuple(result)


# Uloha 18:
def groups(*lists):
    iterators = [iter(list) for list in lists]
    stop_obj = object()
    while True:
        result = []
        for iterator in iterators:
            new_value = next(iterator, stop_obj)
            if new_value is stop_obj:
                return
            result.append(new_value)
        yield tuple(result)


# Uloha 19:
def trange(start, stop, step):
    """
    trange(stop) -> time as a 3-tuple (hours, minutes, seconds)
    trange(start, stop[, step]) -> time tuple

    start: time tuple (hours, minutes, seconds)
    stop: time tuple
    step: time tuple

    returns a sequence of time tuples from start to stop incremented by step
    """

    current = list(start)
    while current < list(stop):
        yield tuple(current)
        seconds = step[2] + current[2]
        min_borrow = 0
        hours_borrow = 0
        if seconds < 60:
            current[2] = seconds
        else:
            current[2] = seconds - 60
            min_borrow = 1
        minutes = step[1] + current[1] + min_borrow
        if minutes < 60:
            current[1] = minutes
        else:
            current[1] = minutes - 60
            hours_borrow = 1
        hours = step[0] + current[0] + hours_borrow
        if hours < 24:
            current[0] = hours
        else:
            current[0] = hours -24

# Uloha 20:
def k_permutations(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for ss in k_permutations(items, n-1):
                if (not items[i] in ss):
                    yield [items[i]]+ss


