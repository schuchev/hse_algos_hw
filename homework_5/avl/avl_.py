class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        return new_root

    def add(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.value:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)

            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            balance = self._get_balance(node)

            if balance > 1 and val < node.left.value:
                return self._rotate_right(node)
            if balance < -1 and val > node.right.value:
                return self._rotate_left(node)
            if balance > 1 and val > node.left.value:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
            if balance < -1 and val < node.right.value:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

            return node

        self.root = _insert(self.root, val)

    def remove(self, val):
        def _min(node):
            while node.left:
                node = node.left
            return node

        def _delete(node, val):
            if not node:
                return None
            if val < node.value:
                node.left = _delete(node.left, val)
            elif val > node.value:
                node.right = _delete(node.right, val)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                successor = _min(node.right)
                node.value = successor.value
                node.right = _delete(node.right, successor.value)

            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            balance = self._get_balance(node)

            if balance > 1:
                if self._get_balance(node.left) >= 0:
                    return self._rotate_right(node)
                else:
                    node.left = self._rotate_left(node.left)
                    return self._rotate_right(node)
            if balance < -1:
                if self._get_balance(node.right) <= 0:
                    return self._rotate_left(node)
                else:
                    node.right = self._rotate_right(node.right)
                    return self._rotate_left(node)
            return node

        self.root = _delete(self.root, val)

    def search(self, val):
        node = self.root
        while node:
            if val == node.value:
                return True
            node = node.left if val < node.value else node.right
        return False
