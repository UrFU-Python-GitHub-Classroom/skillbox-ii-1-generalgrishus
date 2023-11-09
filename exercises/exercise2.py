"""Любимый палиндром"""


def is_palindrome(s: str) -> bool:
    reversed_str = ''.join(reversed(s))
    if (s == reversed_str):
        return True
    return False