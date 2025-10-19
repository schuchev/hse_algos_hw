class BST:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if val == self.val:
            return  
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BST(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BST(val)


def is_bst_valid(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not (min_val < node.val < max_val):
        return False
    return is_bst_valid(node.left, min_val, node.val) and is_bst_valid(node.right, node.val, max_val)
