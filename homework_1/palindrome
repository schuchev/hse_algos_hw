import pytest

def is_palindrome_number(n: int) -> bool:
    
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    cur = n
    reversed = 0

    while n > 0:
        digit = n % 10
        reversed = reversed * 10 + digit
        n //= 10

    return cur == reversed

def test_palindromes():
    
    assert is_palindrome_number(1)
    assert is_palindrome_number(121)
    assert is_palindrome_number(1221)
    assert is_palindrome_number(12321)
    assert is_palindrome_number(1111)
    assert is_palindrome_number(111)


    assert not is_palindrome_number(10)
    assert not is_palindrome_number(123)
    assert not is_palindrome_number(34593)
    assert not is_palindrome_number(111111111111111111111121111111)
    
    with pytest.raises(ValueError):
        is_palindrome_number(0)
    with pytest.raises(ValueError):
        is_palindrome_number(-1)
    with pytest.raises(ValueError):
        is_palindrome_number(-121)
    with pytest.raises(ValueError):
        is_palindrome_number(5.1234)
    with pytest.raises(ValueError):
        is_palindrome_number("123")

    
if __name__ == "__main__":
    test_palindromes()
    print("Все тесты пройдены!")
