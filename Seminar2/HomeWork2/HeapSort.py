from typing import List


class Heap:
    def __init__(self, arr: List[int]):
        self.arr = arr

    def heapify(self, size_arr: int, i: int):
        largest = i
        i_left = 2 * i + 1
        i_right = 2 * i + 2

        # проверяем левый и правый дочерние элементы текущего узла, чтобы определить наибольший элемент
        if i_left < size_arr and self.arr[i] < self.arr[i_left]:
            largest = i_left

        if i_right < size_arr and self.arr[largest] < self.arr[i_right]:
            largest = i_right

        # Если найден наибольший дочерний узел не равен текущему, они меняются местами
        # и функция heapify рекурсивно вызывается для нового индекса largest
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(size_arr, largest)

    def heap_sort(self):
        size = len(self.arr)
        # Здесь для всех узлов, начиная с последнего (верхнего) уровня,
        # вызывается функция heapify для создания двоичной кучи (построение древовидной структуры)
        for i in range(size, -1, -1):
            self.heapify(size, i)

        # Завершаем процесс сортировки, заменяя корень (нулевой элемент) кучи на i-й элемент
        # и уменьшая размер кучи. Затем для измененного массива вновь вызывается heapify
        for i in range(size - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(i, 0)