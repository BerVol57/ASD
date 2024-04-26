class Node:
    def __init__(self, data) -> None:
        self.data = data

    def __str__(self) -> str:
        return str(self.data)


def update_value(a: int, b: int, c: int = 1) -> int:
    return (a + c) % b


class CyclicQueue:
    head: int = -1
    tail: int = -1
    list: list

    def __init__(self, maxlen) -> None:
        self.maxlen = maxlen
        self.list = [None] * maxlen

    def is_empty(self) -> bool:
        return self.head == self.tail == -1

    def enqueue(self, data) -> None:
        is_empty = self.is_empty()
        self.tail += 1

        new_node = Node(data)
        if is_empty:
            self.head = self.tail
            self.list[self.head] = new_node
        else:
            if self.tail == self.maxlen:
                self.list = self.list[1::]+[new_node]
                self.tail -= 1
            else:
                self.list[self.tail] = new_node

    def dequeue(self) -> Node:
        if self.is_empty():
            raise "Queue is empty"
        else:
            node = self.list[self.head]
            self.list[self.head] = None
            self.head = update_value(self.head, self.maxlen)
            return node

    def __str__(self) -> str:
        result_output = "["
        for i in range(len(self.list)):
            node = self.list[i]
            if i == self.maxlen-1:
                result_output += str(node)
            else:
                result_output += str(node) + ", "
        result_output += "]"
        return result_output


CQ = CyclicQueue(3)
CQ.enqueue(1)
print(CQ)
CQ.enqueue(12)
print(CQ)
CQ.enqueue(123)
print(CQ)
CQ.enqueue(1234)
print(CQ)
print(CQ.dequeue())
print(CQ)
