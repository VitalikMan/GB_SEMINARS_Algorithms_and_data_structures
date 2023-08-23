from Seminar4.HomeWork4.node import Node


class RedBlackTree:
    """
    Класс RedBlackTree представляет красно-черное дерево.

    Атрибуты:
        - root: Корневой узел дерева.

    Методы:
        - init(): Инициализирует корень дерева как None.
        - add_node(value): Добавляет узел со значением `value` в дерево.
        - in_order_traversal(node): Возвращает список узлов в порядке в-первую очередь.
        - display(): Выводит дерево на консоль в виде пирамиды.

    Внутренние методы:
        - _balance(node): Балансирует дерево с учетом добавленного узла.
        - _get_uncle(node): Возвращает дядю указанного узла.
        - _rotate_left(node): Выполняет левый поворот для указанного узла.
        - _rotate_right(node): Выполняет правый поворот для указанного узла.
        - _print_tree(node, indent, last): Рекурсивно формирует строку с визуализацией дерева.
    """
    def __init__(self):
        self.root = None

    def init(self):
        self.root = None  # По умолчанию корень - None

    def add_node(self, value):
        new_node = Node(value)
        # Если дерево пустое, сделать новый узел корнем и закрасить его чёрным цветом
        if self.root is None:
            self.root = new_node
            new_node.color = 'black'
        else:
            current_node = self.root
            while True:
                # Если значение добавляемого узла меньше значения текущего узла
                if value < current_node.value:
                    # Если левый узел текущего узла пустой, добавить туда новый узел
                    if current_node.left is None:
                        current_node.left = new_node
                        new_node.parent = current_node
                        break
                    # В противном случае перейти к левому узлу текущего узла
                    else:
                        current_node = current_node.left
                # Если значение добавляемого узла больше или равно значения текущего узла
                else:
                    # Если правый узел текущего узла пустой, добавить туда новый узел
                    if current_node.right is None:
                        current_node.right = new_node
                        new_node.parent = current_node
                        break
                    # В противном случае перейти к правому узлу текущего узла
                    else:
                        current_node = current_node.right
        # После добавления нового узла выполнить балансировку дерева
        self._balance(new_node)

    def _balance(self, node):
        # Если добавленный узел - корень дерева
        if node.parent is None:
            node.color = 'black'
            return
        # Если родитель узла черный, все условия красно-черного дерева соблюдены
        if node.parent.color == 'black':
            return
        parent = node.parent
        grandparent = parent.parent
        # Если родитель и дедушка узла находятся на одном уровне
        if grandparent is None:
            return
        # Если родитель и дядя узла красные
        uncle = self._get_uncle(node)
        if uncle is not None and uncle.color == 'red':
            parent.color = 'black'
            uncle.color = 'black'
            grandparent.color = 'red'
            self._balance(grandparent)
            return
        # Если родитель красный, а дядя черный
        if node == parent.right and parent == grandparent.left:
            self._rotate_left(parent)
            node = node.left
        elif node == parent.left and parent == grandparent.right:
            self._rotate_right(parent)
            node = node.right
        parent = node.parent
        grandparent = parent.parent
        parent.color = 'black'
        grandparent.color = 'red'
        if node == parent.left:
            self._rotate_right(grandparent)
        else:
            self._rotate_left(grandparent)

    def _get_uncle(self, node):
        parent = node.parent
        grandparent = parent.parent
        if grandparent is None:
            return None
        if parent == grandparent.left:
            return grandparent.right
        else:
            return grandparent.left

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child
        left_child.right = node
        node.parent = left_child

    def in_order_traversal(self, node):
        if node is None:
            return []
        left_traversal = self.in_order_traversal(node.left)
        right_traversal = self.in_order_traversal(node.right)
        return left_traversal + [node.value] + right_traversal


    def _print_tree(self, node, indent="", last=True):
        if node is None:
            return ""

        output = ""
        output += self._print_tree(node.right, indent + ("|   " if last else "    "), False)
        output += indent
        output += "`-- " if last else "|-- "
        output += f"{node.value} [{node.color}]\n"
        output += self._print_tree(node.left, indent + ("    " if last else "|   "), True)
        return output

    def display(self):
        print(self._print_tree(self.root))
