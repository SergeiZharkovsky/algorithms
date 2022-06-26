from node import Node


def find_parent(node, key):
    if node.value > key:
        sub_tree = node.left
    else:
        sub_tree = node.right

    if sub_tree is None:
        return node
    return find_parent(sub_tree, key)


def insert(root, key):
    node = find_parent(root, key)

    if node.value > key:
        node.left = Node(value=key)
    else:
        node.right = Node(value=key)

    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6
