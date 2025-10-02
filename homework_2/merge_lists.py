import pytest

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_with_dummy(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 if list1 else list2
    return dummy.next

def merge_without_dummy(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    current = head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return head

def to_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_1():
    l1 = to_list([1,2,4])
    l2 = to_list([1,3,4])
    merged = merge_with_dummy(l1, l2)
    assert to_array(merged) == [1,1,2,3,4,4]

def test_2():
    assert merge_with_dummy(None, None) is None
    assert merge_without_dummy(None, None) is None

def test_3():
    l1 = to_list([1,2,3])
    assert to_array(merge_with_dummy(l1, None)) == [1,2,3]
    assert to_array(merge_without_dummy(l1, None)) == [1,2,3]

def test_4():
    l1 = to_list([5,6,7])
    l2 = to_list([1,2,3])
    merged = merge_with_dummy(l1, l2)
    assert to_array(merged) == [1,2,3,5,6,7]

def test_5():
    l1 = to_list([4,5,9,10])
    l2 = to_list([1,6,7,11,24,34,56])
    merged = merge_with_dummy(l1, l2)
    assert to_array(merged) == [1,4,5,6,7,9,10,11,24,34,56]
    
def test_5():
    l1 = to_list([1,1,1,1])
    l2 = to_list([1,1,1,1,1,1])
    merged = merge_with_dummy(l1, l2)
    assert to_array(merged) == [1,1,1,1,1,1,1,1,1,1]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
