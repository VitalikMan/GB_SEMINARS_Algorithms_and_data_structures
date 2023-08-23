from red_black_tree import RedBlackTree


def main():
    """
    Создает пример красно-черного дерева и выводит его на экран в виде пирамиды.
    """
    rb_tree = RedBlackTree()
    values = [10, 20, 30, 5, 25, 28, 3, 8, 10, 3, 1, 7, 11]

    for value in values:
        rb_tree.add_node(value)

    # Выводим визуальное отображение красно-черного дерева
    print("\nВизуальное отображение дерева: \n")
    rb_tree.display()


if __name__ == "__main__":
    main()
