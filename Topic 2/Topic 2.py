class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)
    def search(self, key):
        return self._search(self.root, key)
    def _search(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self._search(current.left, key)
        return self._search(current.right, key)

    def in_order_traversal(self):
        return self._in_order_traversal(self.root, [])

    def _in_order_traversal(self, current, result):
        if current is not None:
            self._in_order_traversal(current.left, result)
            result.append(current.key)
            self._in_order_traversal(current.right, result)
        return result

class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
bst = BinarySearchTree()
dll = DoublyLinkedList()
bst.insert(25)
bst.insert(15)
bst.insert(35)
bst.insert(10)
bst.insert(20)
dll.append("Task 1: Adjust temperature")
dll.append("Task 2: Check air quality")
dll.append("Task 3: Turn off unused zones")
print("BST In-Order Traversal:", bst.in_order_traversal())
print("Doubly Linked List Tasks:", dll.display())
