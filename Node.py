class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def NormalList_to_LinkedList(arr, i=0, currentNode= None, root= None):
    if i >= len(arr):
        currentNode.next = None
        return root

    node = Node(arr[i])
    if i == 0:
        root = node
    else:
        currentNode.next = node
    return NormalList_to_LinkedList(arr, i + 1, node, root)


def LinkedList_to_NormalList(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


arr = [10, 5, -3, -3, 1, 4, -4]
res = NormalList_to_LinkedList(arr)

# [10, 5, -3, -3, 1, 4, -4]
print(LinkedList_to_NormalList(res))

# 10
# 5
# -3
# -3
# 1
# 4
# -4
while res:
    print(res.val)
    res = res.next


