"""Test Suite for Exercise 2"""

from exercises import exercise2

def test_is_palindrome_1():
    assert exercise2.is_palindrome('asddsa') == True

def test_is_palindrome_2():
    assert exercise2.is_palindrome('asdsa') == True

def test_is_palindrome_3():
    assert exercise2.is_palindrome('asda') == False
