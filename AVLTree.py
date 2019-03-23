from typing import Any

class Item:
    __slots__ = ['key', 'value']

    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return '({0} {1})'.format(self.key, self.value)

class AVLTree:
    __slots__ = ['item', 'height', 'left', 'right', 'children']

    def __init__(self, item: Item = None):
        self.item = item
        self.height: int = -1
        self.left: AVLTree = None
        self.right: AVLTree = None
        self.children = 0

    def _height(self, tree) -> int:
        return tree.height

    def _right_rotate(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        root.height = max(self._height(root.left), self._height(root.right)) + 1
        root.children = root.left.children + root.right.children + 1

        new_root.height = max(self._height(new_root.left), self._height(new_root.right)) + 1
        new_root.children = new_root.left.children + new_root.right.children + 1

        return new_root

    def _left_rotate(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        root.height = max(self._height(root.left), self._height(root.right)) + 1
        root.children = root.left.children + root.right.children + 1

        new_root.height = max(self._height(new_root.left), self._height(new_root.right)) + 1
        new_root.children = new_root.left.children + new_root.right.children + 1

        return new_root


    def insert(self, item: Item):
        if not self.item:
            self.item = item
            self.height = 0
            self.left = AVLTree()
            self.right = AVLTree()
            self.children = 1
            return self
        if item.key < self.item.key:
            self.left = self.left.insert(item)
        elif item.key > self.item.key:
            self.right = self.right.insert(item)

        left_height = self._height(self.left)
        right_height = self._height(self.right)

        left_children = self.left.children if self.left else 0
        right_children = self.right.children if self.right else 0

        self.height = max(left_height, right_height) + 1
        self.children = left_children + right_children + 1

        balance_factor = left_height - right_height

        if balance_factor > 1:
            # LL case
            if self._height(self.left.left) >= self._height(self.left.right):
                return self._right_rotate(self)
            # LR case
            else:
                self.left = self._left_rotate(self.left)
                return self._right_rotate(self)

        elif balance_factor < -1:
            # RR case
            if self._height(self.right.right) >= self._height(self.right.left):
                return self._left_rotate(self)
            # RL case
            else:
                self.right = self._right_rotate(self.right)
                return self._left_rotate(self)

        return self

    def inorder(self) -> None:
        if not self.item:
            return
        self.left.inorder()
        print("{0} ,height: {1}, children: {2}".format(self.item, self.height, self.children))
        self.right.inorder()

def median(root: AVLTree, k: int = None) -> Item:
    if not k:
        k = root.children // 2 + 1
    if k == root.left.children + 1:
        return root.item
    elif k <= root.left.children:
        return median(root.left, k)
    else:
        return median(root.right, k - root.left.children - 1)

if __name__ == '__main__':
    tree = AVLTree()
    print("LL case")
    for item in [3, 2, 1]:
        tree = tree.insert(Item(item, item))
    tree.inorder()

    tree = AVLTree()
    print("LR case")
    for item in [3, 1, 2]:
        tree = tree.insert(Item(item, item))
    tree.inorder()

    tree = AVLTree()
    print("RR case")
    for item in [1, 2, 3]:
        tree = tree.insert(Item(item, item))
    tree.inorder()

    tree = AVLTree()
    print("RL case")
    for item in [1, 3, 2]:
        tree = tree.insert(Item(item, item))
    tree.inorder()

    for item in range(1,8):
        tree = tree.insert(Item(item, item))
    print(median(tree))