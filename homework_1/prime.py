def count_primes(n: int) -> int:

    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False

    return sum(is_prime)


def test_count_primes():
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    assert count_primes(2) == 0
    assert count_primes(3) == 1  
    assert count_primes(10) == 4
    assert count_primes(15) == 6
    assert count_primes(100) == 25
    assert count_primes(-7) == 0

if __name__ == "__main__":
    test_count_primes()
    print("Все тесты пройдены!")
