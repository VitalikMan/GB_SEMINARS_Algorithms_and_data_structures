from HeapSort import Heap
from random import randint


def main():
    array = [randint(0, 50) for _ in range(10)]
    print("Список со случайными числами:\n", array)

    heap = Heap(array)
    heap.heap_sort()

    print("Сортированный список методом пирамидальной сортировки:\n", heap.arr)


if __name__ == "__main__":
    main()
