def max_sum(arr) -> int:

    total = sum(arr)
    if total % 2 == 0:
        return total

    odd_numbers = [x for x in arr if x % 2 == 1]

    return total - min(odd_numbers)


def test_max_sum():
    assert max_sum([2]) == 2  
    assert max_sum([5]) == 0     

    assert max_sum([2,2,2,2,2]) == 10
    assert max_sum([3,3,3,3,3]) == 12  

    assert max_sum([]) == 0

    assert max_sum([2, 4, 6, 8]) == 20

    assert max_sum([1, 3, 5, 7]) == 16

    assert max_sum([2,4,2,6,1,2,5,3]) == 24

if __name__ == "__main__":
    test_max_sum()
    print("Все тесты пройдены!")
