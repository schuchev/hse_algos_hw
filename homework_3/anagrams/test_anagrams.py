import pytest
from anagrams import anagrams

def test_1():
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = anagrams(strs)
    result = [set(group) for group in result]
    trues = [set(["bat"]), set(["nat","tan"]), set(["ate","eat","tea"])]
    assert all(group in result for group in trues)

def test_2():
    assert anagrams([]) == []

def test_3():
    strs = ["abc", "def", "ghi"]
    result = anagrams(strs)
    result = [set(group) for group in result]
    trues = [set(["abc"]), set(["def"]), set(["ghi"])]
    assert all(group in result for group in trues)

def test_4():
    strs = ["a", "b", "ab", "ba", "abc", "cab"]
    result = anagrams(strs)
    result = [set(group) for group in result]
    trues = [set(["a"]), set(["b"]), set(["ab","ba"]), set(["abc","cab"])]
    assert all(group in result for group in trues)

