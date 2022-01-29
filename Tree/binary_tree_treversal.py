from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any, Sequence


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None


def make_tree() -> Node | None:
    return Node(1, Node(2, Node(4), Node(5)), Node(3))


def preorder(root: Node | None) -> list[int]:

    return [root.data] + preorder(root.left) + preorder(root.right) if root else []


def postorder(root: Node | None) -> list[int]:
    return postorder(root.left) + postorder(root.right) + [root.data] if root else []


def inorder(root: Node | None) -> list[int]:

    return inorder(root.left) + [root.data] + inorder(root.right) if root else []


def height(root: Node | None) -> int:

    return (max(height(root.left), height(root.right)) + 1) if root else 0


def level_order(root: Node | None) -> Sequence[Node | None]:

    output: list[Any] = []

    if root is None:
        return output

    process_queue = deque([root])

    while process_queue:
        node = process_queue.popleft()
        output.append(node.data)

        if node.left:
            process_queue.append(node.left)
        if node.right:
            process_queue.append(node.right)
    return output


def get_nodes_from_left_to_right(
    root: Node | None, level: int
) -> Sequence[Node | None]:

    output: list[Any] = []

    def populate_output(root: Node | None, level: int) -> None:
        if not root:
            return
        if level == 1:

            output.append(root.data)
        elif level > 1:
            populate_output(root.left, level - 1)
            populate_output(root.right, level - 1)

    populate_output(root, level)
    return output


def get_nodes_from_right_to_left(
    root: Node | None, level: int
) -> Sequence[Node | None]:

    output: list[Any] = []

    def populate_output(root: Node | None, level: int) -> None:
        if root is None:
            return
        if level == 1:
            output.append(root.data)
        elif level > 1:
            populate_output(root.right, level - 1)
            populate_output(root.left, level - 1)

    populate_output(root, level)
    return output


def zigzag(root: Node | None) -> Sequence[Node | None] | list[Any]:

    if root is None:
        return []

    output: list[Sequence[Node | None]] = []

    flag = 0
    height_tree = height(root)

    for h in range(1, height_tree + 1):
        if not flag:
            output.append(get_nodes_from_left_to_right(root, h))
            flag = 1
        else:
            output.append(get_nodes_from_right_to_left(root, h))
            flag = 0

    return output


def main() -> None:  # Main function for testing.

    root = make_tree()


    print(f"In-order Traversal: {inorder(root)}")
    print(f"Pre-order Traversal: {preorder(root)}")
    print(f"Post-order Traversal: {postorder(root)}", "\n")

    print(f"Height of Tree: {height(root)}", "\n")

    print("Complete Level Order Traversal: ")
    print(level_order(root), "\n")

    print("Level-wise order Traversal: ")

    for level in range(1, height(root) + 1):
        print(f"Level {level}:", get_nodes_from_left_to_right(root, level=level))

    print("\nZigZag order Traversal: ")
    print(zigzag(root))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()