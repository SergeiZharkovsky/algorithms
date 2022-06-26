def solution(root):
    if root.left and root.right:
        return max(root.value, solution(root.left), solution(root.right))
    elif root.left and not root.right:
        return max(root.value, solution(root.left))
    elif root.right and not root.left:
        return max(root.value, solution(root.right))
    else:
        return root.value


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
