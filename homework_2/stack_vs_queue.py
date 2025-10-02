import pytest
 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head=None
    def push(self,value):
        node=Node(value)
        node.next=self.head
        self.head=node
    def pop(self):
        if self.head==None:
            raise IndexError('нет элементов в стэке')
        value=self.head.value
        self.head=self.head.next
        return value 

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None 
    def push(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node 
        if self.tail:
            self.tail.next=node 
        self.tail=node
    def pop(self):
        if self.head is None:
            raise IndexError('нет элементов в очереди')
        value=self.head.value 
        self.head=self.head.next 
        if self.head is None:
            self.tail=None 
        return value
 

def test_stack():
    s = Stack()
    s.push(10)
    s.push(15)
    s.push(5)
    
    assert s.pop() == 5
    assert s.pop() == 15
    assert s.pop() == 10

    with pytest.raises(IndexError):
        s.pop()

def test_queue():
    q = Queue()
    q.push(4)
    q.push(7)
    q.push(14)
    
    assert q.pop() == 4
    assert q.pop() == 7
    assert q.pop() == 14

    with pytest.raises(IndexError):
        q.pop()


if __name__ == "__main__":
    pytest.main([__file__,"-v"])