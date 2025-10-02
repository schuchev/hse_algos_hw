import pytest

def validate(pushed, popped):
    stack = []
    j = 0 
    
    for i in pushed:
        stack.append(i) 
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    
    return not stack

def test_1():
    pushed = [1,2,3,4,5]
    popped = [1,3,5,4,2]
    assert validate(pushed, popped) == True

def test_2():
    pushed = [1,2,3]
    popped = [3,1,2]
    assert validate(pushed, popped) == False

def test_3():
    pushed = [1]
    popped = [1]
    assert validate(pushed, popped) == True

def test_4():
    pushed = []
    popped = []
    assert validate(pushed, popped) == True

def test_5():
    pushed = [1,2,3]
    popped = [3,2,1]
    assert validate(pushed, popped) == True

def test_6():
    pushed = [1,5,9,10,4,6]
    popped = [9,10,4,1,5,6]
    assert validate(pushed, popped) == False

def test_7():
    pushed = [1,5,9,10,4,6]
    popped = [9,10,4,6,5,1]
    assert validate(pushed, popped) == True
    
if __name__ == "__main__":
    pytest.main([__file__, "-v"])