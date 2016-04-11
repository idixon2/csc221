import unittest
from lab8 import (
    count_letters,
    reverse_string,
    is_palindrome,
    match_ends,
    front_x,
    sort_last,
)

class TestLab8(unittest.TestCase):
    def test_count_letters(self):
        self.assertEqual(count_letters('pizza', 'z'), 2)
    def test_reverse_string(self):
        self.assertTrue(reverse_string('hello') == "olleh")
        self.asssertEqual(reverse_string('abba'), 'abba')
    def test_is_palindrome(self):
        self.assertFalse(is_palindrome('hello'))
    def test_match_ends(self):
        self.assertEqual(
            match_ends(['hello', 'xoox', 'beeb', 'blab', 'a', 'asdf']),
            3
        )
    def test_front_x(self):
        self.assertEqual(
            front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
                ['xanadu','xyz', 'aardvark', 'apple', 'mix'],
        )
    def test_sort_last(self):
        self.assertEqual(sort_last([(1, 7), (2,3)]), [(2,30), (1, 7)])

if __name__ == '__main__':
    unittest.main()