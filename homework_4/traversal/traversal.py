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

    def inorder(self, vals=None): 
        if vals is None: vals = []
        if self.left:
            self.left.inorder(vals)
        vals.append(self.val)
        if self.right:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals=None):  
        if vals is None: vals = []
        vals.append(self.val)
        if self.left:
            self.left.preorder(vals)
        if self.right:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals=None):  
        if vals is None: vals = []
        if self.left:
            self.left.postorder(vals)
        if self.right:
            self.right.postorder(vals)
        vals.append(self.val)
        return vals

    def reverse_inorder(self, vals=None):  
        if vals is None: vals = []
        if self.right:
            self.right.reverse_inorder(vals)
        vals.append(self.val)
        if self.left:
            self.left.reverse_inorder(vals)
        return vals

    def reverse_preorder(self, vals=None):  
        if vals is None: vals = []
        vals.append(self.val)
        if self.right:
            self.right.reverse_preorder(vals)
        if self.left:
            self.left.reverse_preorder(vals)
        return vals

    def reverse_postorder(self, vals=None): 
        if vals is None: vals = []
        if self.right:
            self.right.reverse_postorder(vals)
        if self.left:
            self.left.reverse_postorder(vals)
        vals.append(self.val)
        return vals
