from __future__ import annotations
from collections import deque


class Node:
    parent: Node = None
    left_child: Node = None
    right_child: Node = None

    def __init__(self, data) -> None:
        self.data = data

    def copy_from(self, node: Node) -> None:
        self.parent = node.parent
        self.left_child = node.left_child
        self.right_child = node.right_child
        self.data = node.data

    def __str__(self) -> str:
        return str(self.data)


def get_max_depth(node: Node) -> int:
    if node is Node:
        return 0
    else:
        lDepth = get_max_depth(node.left_child)
        rDepth = get_max_depth(node.right_child)
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


class BSTree:
    top: Node = None

    def __init__(self) -> None:
        pass

    def tree_insert(self, node_data) -> None:
        """
        Функція для створення нового вузла з вказаними даними.\n
        :param node_data:Данні які будуть міститися в ново-створеному вузлі.
        :returns: None.
        """
        new_node = Node(node_data)
        parent_current_node = None
        current_node = self.top
        #
        while current_node is not None:
            parent_current_node = current_node
            if node_data < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        #
        new_node.parent = parent_current_node
        if parent_current_node is None:
            self.top = new_node
        else:
            if node_data < parent_current_node.data:
                parent_current_node.left_child = new_node
            else:
                parent_current_node.right_child = new_node

    def tree_search(self, node_data) -> Node | None:
        """
        Функція для знаходження вузла за даними які він повинен мати.\n
        Параметри:
        :param node_data:Інформація яку повиний містити шуканий вузол.
        :return:Шуканий вузол, якщо він існує. Якщо такоого вузла не існує - повертає None.
        """
        node = self.top

        while node is not None and node_data != node.data:
            if node_data < node.data:
                node = node.left_child
            else:
                node = node.right_child
        return node

    def tree_minimum(self, node: Node | None) -> Node:
        """

        :returns:Повертає найменший вузол.
        """
        if node is None:
            node = self.top
        while node.left_child is not None:
            node = node.left_child
        return node

    def tree_maximum(self, node: Node | None) -> Node:
        """

        :returns:Повертає найбільший вузол.
        """
        if node is None:
            node = self.top
        while node.right_child is not None:
            node = node.right_child
        return node

    def tree_successor(self, node: Node) -> Node:
        """

        :returns:Повертає 'спадкоємця'.
        """
        if node.right_child is not None:
            return self.tree_minimum(node.right_child)
        parent_node = node.parent
        while parent_node is not None and node == parent_node.right_child:
            node = parent_node
            parent_node = parent_node.parent
        return parent_node

    def tree_delete(self, node: Node) -> Node:
        """

        :param node:Вузол, який користувач бажає видалити.
        :returns:Повертає видалений вузол.
        """
        if node.left_child is None or node.right_child is None:
            d_node = node
        else:
            d_node = self.tree_successor(node)
        #
        if d_node.left_child is not None:
            child_node = d_node.left_child
        else:
            child_node = d_node.right_child
        #
        if child_node is not None:
            child_node.parent = d_node.parent
        if d_node.parent is None:
            self.top = child_node
        elif d_node == d_node.parent.left_child:
            d_node.parent.left_child = child_node
        else:
            d_node.parent.right_child = child_node
        #
        if d_node != node:
            d_node.copy_from(node)
        return d_node

    def read_str(self, string_line: str) -> None:
        """

        :param string_line:Рядок, з символами, які будуть у ролі вузлів у дереві.
        """
        for symbol in string_line:
            self.tree_insert(symbol)

    def __str__(self) -> str:
        nodes = deque()
        layers = [[self.top]]
        nodes.append(self.top)
        #
        while len(nodes) != 0:
            left_most = nodes.popleft()
            if left_most in layers[-1]:
                layers.append([])

            if left_most.left_child is not None:
                nodes.append(left_most.left_child)
                layers[-1].append(left_most.left_child)

            if left_most.right_child is not None:
                nodes.append(left_most.right_child)
                layers[-1].append(left_most.right_child)
        layers = layers[:-1:]  # Забираємо останній [], він є зайвим
        depth = len(layers)
        blank = [" "*int(2**(depth + 1)-1) + " \n"]*depth
        coordinates = [[self.top, int((2**(depth + 1)-1)/2)]]
        for i_layer in range(len(layers)-1):
            for node in layers[i_layer]:
                if node.left_child is not None:
                    for coord in coordinates:
                        if coord[0] == node:
                            coordinates.append([node.left_child, -int((2**(depth - i_layer)-1)/2)+coord[1]])

                if node.right_child is not None:
                    for coord in coordinates:
                        if coord[0] == node:
                            coordinates.append([node.right_child, int((2**(depth - i_layer)-1)/2)+coord[1]])

        for i_layer in range(len(layers)):
            for node in layers[i_layer]:
                for coord in coordinates:
                    if coord[0] == node:
                        blank_string = blank[i_layer]
                        left_part = blank_string[:coord[1]]
                        right_part = blank_string[coord[1]+1:]
                        blank[i_layer] = left_part+str(coord[0])+right_part
        res = ""
        for i in blank:
            res += i
        return res

    def tree_postorder(self, is_print: bool = False) -> list[Node]:
        """

        :return: Повертає список з вузлів, отриманий постфіксним обходом деревом та виводить data вузлів, що є в списку.
        """
        node = self.top
        visited = []
        while node is not None:
            if node.left_child is not None and node.left_child not in visited:
                node = node.left_child
            elif node.right_child is not None and node.right_child not in visited:
                node = node.right_child
            else:
                visited.append(node)
                node = node.parent
        if is_print:
            for el in visited:
                print(el, end=" ")
        return visited

    def tree_clean(self) -> None:
        """
            Чистить дерево від повторюваних елементів.
        """
        node_list = self.tree_postorder()
        for node_i in node_list:
            for node_j in node_list:
                if node_i.data == node_j.data and node_i != node_j:
                    self.tree_delete(node_j)
                    node_list.remove(node_j)


test_string = "upllltpazay"
tree = BSTree()
tree.read_str(test_string)
# print(tree)
# n = tree.tree_search('p')
# print(n.data)
# tree.tree_delete(n)
# print(tree)
# tree.tree_postorder(True)
tree.tree_clean()
print(tree)
