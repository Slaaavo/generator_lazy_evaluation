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
    while True:
        for l in list:
            yield l


# Uloha 5:
def factorial():
    fact, x = 1, 1
    while True:
        yield fact
        fact *= x + 1
        x += 1


# Uloha 6:
def digits(n, base):
    yield n % base
    n //= base
    while n > 0:
        yield n % base
        n //= base


# Uloha 7:
def factorial_digit_sum(N):
    return reduce(add, digits(next(islice(factorial(), N - 1, N)), 10))


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
    # return next(islice(primes_memory(), n - 1, n))
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

    start = start[0] * 3600 + start[1] * 60 + start[2]
    end = stop[0] * 3600 + stop[1] * 60 + stop[2]
    step = step[0] * 3600 + step[1] * 60 + step[2]
    while start < end:
        temp = start
        hours = temp // 3600
        temp %= 3600
        minutes = temp // 60
        seconds = temp % 60
        yield (hours, minutes, seconds)
        start += step

# Uloha 20:
def k_permutations(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for ss in k_permutations(items, n-1):
                if (not items[i] in ss):
                    yield [items[i]]+ss


