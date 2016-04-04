import exercises as e
from itertools import islice
import unittest

class GeneratorTests(unittest.TestCase):


    # Uloha 1:
    def test_square_generator(self):
        self.assertNotIsInstance(e.square_generator(range(7)), list)
        self.assertEqual(list(e.square_generator(range(7))), [0,1,4,9,16,25,36])


    # Uloha 2:
    def test_square_map(self):
        self.assertNotIsInstance(e.square_map(range(7)), list)
        self.assertEqual(list(e.square_map(range(7))), [0,1,4,9,16,25,36])


    # Uloha 3:
    def test_square_comprehension(self):
        self.assertNotIsInstance(e.square_comprehension(range(7)), list)
        self.assertEqual(list(e.square_comprehension(range(7))), [0,1,4,9,16,25,36])


    # Uloha 4:
    def test_cycle(self):
        self.assertEqual(list(islice(e.cycle([1,2,3]), 7)), [1,2,3,1,2,3,1])


    # Uloha 5:
    def test_factorial(self):
        self.assertEqual(list(islice(e.factorial(),6)), [1, 2, 6, 24, 120, 720])


    # Uloha 6:
    def test_digits(self):
        self.assertEqual(list(e.digits(123450, 10)), [0, 5, 4, 3, 2, 1])
        self.assertEqual(list(e.digits(0, 10)), [0])
        self.assertEqual(list(e.digits(8, 2)), [0, 0, 0, 1])


    # Uloha 7:
    def test_factorial_digit_sum(self):
        self.assertEqual(e.factorial_digit_sum(10), 27)
        self.assertEqual(e.factorial_digit_sum(101), 639)


    # Uloha 8:
    def test_my_range(self):
        self.assertEqual(list(e.my_range(0,10)), list(range(0, 10)))
        self.assertEqual(list(e.my_range(0, 10, 2)), list(range(0, 10, 2)))
        self.assertEqual(list(e.my_range(0, 10, 3)), list(range(0, 10, 3)))


    # Uloha 9:
    def test_my_range_negative(self):
        self.assertEqual(list(e.my_range_negative(0,10)), list(range(0, 10)))
        self.assertEqual(list(e.my_range_negative(0, 10, 2)), list(range(0, 10, 2)))
        self.assertEqual(list(e.my_range_negative(0, 10, 3)), list(range(0, 10, 3)))
        self.assertEqual(list(e.my_range_negative(10, 0, -1)), list(range(10, 0, -1)))
        self.assertEqual(list(e.my_range_negative(10, 0, -3)), list(range(10, 0, -3)))


    # Uloha 10:
    def test_items(self):
        dictionary = {'a':1, 'b':2, 'c':3, 'd':4}
        self.assertEqual(list(e.items(dictionary)), list(dictionary.items()))


    # Uloha 11:
    def test_pseudorandom(self):
        self.assertEqual(list(islice(e.pseudorandom(9, 2, 0, 1), 6)), [2, 4, 8, 7, 5, 1])


    # Uloha 12:
    def test_sample(self):
        self.assertEqual(list(islice(e.sample(['a',1,2,3,4,5,6,7,8,9]), 20)), ['a', 5, 4, 1, 4, 9, 2, 5, 6, 7, 8, 1, 6, 1, 8, 1, 6, 9, 2, 9])


    # Uloha 13:
    def test_sample_no_rep(self):
        items = ['a',1,2,3,4,5,6,7,8,9]
        self.assertEqual(list(islice(e.sample_no_rep(items), 9)), ['a', 4, 6, 7, 8, 9, 1, 2, 3])
        self.assertEqual(items, ['a',1,2,3,4,5,6,7,8,9])
        self.assertEqual(list(islice(e.sample_no_rep(items), 20)), ['a', 4, 6, 7, 8, 9, 1, 2, 3, 5])


    # Uloha 14:
    def test_primes(self):
        self.assertEqual(list(islice(e.primes(), 5)), [2,3,5,7,11])


    # Uloha 15:
    def test_primes_memory(self):
        self.assertEqual(list(islice(e.primes_memory(), 5)), [2,3,5,7,11])


    # Uloha 16:
    def test_nth_prime(self):
        self.assertEqual(e.nth_prime(1), 2)
        self.assertEqual(e.nth_prime(100), 541)


    # Uloha 17:
    def test_pairs(self):
        self.assertEqual(list(e.pairs([1, 2, 3, 4], ['a', 'b', 'c', 'd'])), [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])


    # Uloha 18:
    def test_groups(self):
        self.assertEqual(list(e.groups([1, 2, 3, 4], ['a', 'b', 'c', 'd'], 'xyz')), [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')])


    # Uloha 19:
    def test_trange(self):
        self.assertEqual(list(e.trange((10, 10, 10), (13, 50, 15), (0, 15, 12))),
                         [(10, 10, 10),
                         (10, 25, 22),
                         (10, 40, 34),
                         (10, 55, 46),
                         (11, 10, 58),
                         (11, 26, 10),
                         (11, 41, 22),
                         (11, 56, 34),
                         (12, 11, 46),
                         (12, 26, 58),
                         (12, 42, 10),
                         (12, 57, 22),
                         (13, 12, 34),
                         (13, 27, 46),
                         (13, 42, 58)])


    # Uloha 20:
    def test_k_permutations(self):
        self.assertEqual(list(e.k_permutations(['a', 'b', 'c', 'd'], 3)),
                                                                    [['a', 'b', 'c'],
                                                                    ['a', 'b', 'd'],
                                                                    ['a', 'c', 'b'],
                                                                    ['a', 'c', 'd'],
                                                                    ['a', 'd', 'b'],
                                                                    ['a', 'd', 'c'],
                                                                    ['b', 'a', 'c'],
                                                                    ['b', 'a', 'd'],
                                                                    ['b', 'c', 'a'],
                                                                    ['b', 'c', 'd'],
                                                                    ['b', 'd', 'a'],
                                                                    ['b', 'd', 'c'],
                                                                    ['c', 'a', 'b'],
                                                                    ['c', 'a', 'd'],
                                                                    ['c', 'b', 'a'],
                                                                    ['c', 'b', 'd'],
                                                                    ['c', 'd', 'a'],
                                                                    ['c', 'd', 'b'],
                                                                    ['d', 'a', 'b'],
                                                                    ['d', 'a', 'c'],
                                                                    ['d', 'b', 'a'],
                                                                    ['d', 'b', 'c'],
                                                                    ['d', 'c', 'a'],
                                                                    ['d', 'c', 'b']])



if __name__ == '__main__':
    unittest.main()