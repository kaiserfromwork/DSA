# Palindrome Checker: Given a string, check if it is a palindrome using a deque.

from collections import deque
import random


def check_palindrome(word: str):
    palindrome = deque(word)
    if word == " " or word == "":
        return False

    while len(palindrome) > 1:
        if palindrome.popleft() != palindrome.pop():
            return False
        
    return True

palindrome_words = (
    ("racecar", True),
    ("hello", False),
    ("madam", True),
    ("world", False),
    ("level", True),
    ("python", False),
    ("radar", True),
    ("dequeue", False),
    ("civic", True),
    ("programming", False)
)

random_index = random.randint(0, len(palindrome_words) - 1)
word, result = palindrome_words[random_index]

print(f"Word: {word}, Expected result: {result}")
print(f"Is word Palindrome? {check_palindrome(word)}")
print(f"Is answer correct? {check_palindrome(word) == result}")