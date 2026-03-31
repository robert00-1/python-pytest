# Correct import from the lib package
from lib.palindrome import longest_palindromic_substring

# ---------------- Basic Cases ----------------
def test_basic_babad():
    result = longest_palindromic_substring("babad")
    # "bab" or "aba" are valid
    assert result in ["bab", "aba"]

def test_basic_cbbd():
    result = longest_palindromic_substring("cbbd")
    assert result == "bb"

def test_single_character():
    result = longest_palindromic_substring("a")
    assert result == "a"

def test_two_characters():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]

def test_entire_string_palindrome():
    result = longest_palindromic_substring("racecar")
    assert result == "racecar"

# ---------------- Edge Cases ----------------
def test_empty_string():
    result = longest_palindromic_substring("")
    assert result == ""

def test_long_string():
    s = "a" * 1000
    result = longest_palindromic_substring(s)
    assert result == s

def test_no_multi_char_palindrome():
    s = "abcd" * 250  # length = 1000
    result = longest_palindromic_substring(s)
    # Only single letters are valid palindromes
    assert len(result) == 1

# ---------------- Special Cases ----------------
def test_palindrome_in_middle():
    s = "abcddcbaefg"
    result = longest_palindromic_substring(s)
    assert result == "abcddcba"

def test_multiple_palindromes_same_length():
    s = "abbcccbbbca"
    result = longest_palindromic_substring(s)
    assert result in ["bbcccbb", "bcccb"]

def test_numeric_characters():
    s = "123321xyz"
    result = longest_palindromic_substring(s)
    assert result == "123321"