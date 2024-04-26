from __future__ import annotations


class Node:
    next: Node = None
    data = None

    def __init__(self, data) -> None:
        self.data = data

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    head: Node = None
    tail: Node = None

    def __init__(self) -> None:
        pass

    def is_empty(self) -> bool:
        return self.head == self.tail is None

    def enqueue(self, data) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next, self.tail = new_node, new_node

    def dequeue(self) -> Node:
        if self.is_empty():
            raise ValueError("Queue is empty")
        else:
            node, self.head = self.head, self.head.next
            return node

    def __str__(self) -> str:
        current_node = self.head
        result_output = "["
        while current_node:
            if current_node == self.tail:
                result_output += str(current_node)+"]"
            else:
                result_output += str(current_node)+", "
            current_node = current_node.next
        return result_output


LL = LinkedList()
LL.enqueue(1)
LL.enqueue(12)
LL.enqueue(123)
print(LL)
print(LL.dequeue())
print(LL)
