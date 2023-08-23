
class Node:
    """
    Класс Node представляет узел красно-черного дерева.

    Атрибуты:
        - value: Значение узла.
        - color: Цвет узла, "red" (красный) или "black" (черный).
        - left: Левый дочерний узел.
        - right: Правый дочерний узел.
        - parent: Родительский узел.
    """
    def __init__(self, value):
        self.value = value
        self.color = 'red'  # Новые узлы всегда красные
        self.left = None
        self.right = None
        self.parent = None  # Ссылка на родительский узел
