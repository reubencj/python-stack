import unittest
import math

def reverse_list(ls):
    last_index = len(ls) - 1
    start_index = 0
    while start_index < len(ls)/2:
        ls[last_index], ls[start_index] = ls[start_index], ls[last_index]
        start_index += 1
        last_index -= 1
    return ls 

def is_palindrome(word):
    upper_word = word.upper()
    reversed_word = "".join(reverse_list(list(upper_word)))
    return upper_word == reversed_word

def get_change(coins):
    quaters = math.floor(coins/25)
    coins -= 25 * quaters
    dimes = math.floor(coins/10)
    coins -= 10 * dimes
    nickles = math.floor(coins/5)
    coins -= 5 * nickles
    pennies = coins
    return [quaters,dimes,nickles,pennies]
    
    
  

class TestFunctions(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse_list([1,2,3,4]),[4,3,2,1])
        self.assertEqual(reverse_list(['H','E','L','L','O']),['O','L','L','E','H'])
    
    def test_palindrome(self):
        self.assertTrue(is_palindrome('malayalam'))
        self.assertFalse(is_palindrome('reuben'))
    
    def test_change(self):
        self.assertEqual(get_change(100),[4,0,0,0])
        self.assertEqual(get_change(69),[2,1,1,4])

    def setUp(self) :
        print("running setup")
    
    def tearDown(self):
        print("running tearDown")
    


if __name__ == '__main__':
    unittest.main()