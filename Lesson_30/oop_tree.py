from typing import Optional


class BinaryTree:

    def __init__(self, root_obj) -> None:
        self.key: str = str(root_obj)
        self.left_child: Optional[BinaryTree] = None
        self.right_child: Optional[BinaryTree] = None

    def insert_left(self, new_node) -> None:
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node) -> None:
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t: BinaryTree = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self) -> "Optional[BinaryTree]":
        return self.right_child

    def get_left_child(self) -> "Optional[BinaryTree]":
        return self.left_child

    def set_root_val(self, obj) -> None:
        self.key = obj

    def get_root_val(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return f"BinaryTree: {self.key}"

    def pre_order(self) -> None:
        print(self.key, end=' ')
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self) -> None:
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.key, end=' ')

    def in_order(self) -> None:
        if self.left_child:
            self.left_child.in_order()
        print(self.get_root_val(), end=' ')
        if self.right_child:
            self.right_child.in_order()

    def is_leaf(self):
        if not self.left_child and not self.right_child:
            return True
        else: return False


if __name__ == "__main__":
    tr = BinaryTree(8)
    tr.insert_left(5)
    tr.insert_right(4)
    tr.get_left_child().insert_left(9)
    tr.get_left_child().insert_right(7)
    seven = tr.get_left_child().get_right_child()
    seven.insert_left(1)
    seven.insert_right(12)
    seven.get_right_child().insert_left(2)
    tr.get_right_child().insert_right(11)
    tr.get_right_child().get_right_child().insert_left(3)
    tr.pre_order()
    print()
    tr.in_order()
    print()
    tr.post_order()
    print()

