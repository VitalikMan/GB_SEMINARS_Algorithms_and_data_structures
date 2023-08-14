from random import randint

def binary_search(array, low, high, value):
    # Проверяем оставшуюся часть массива
    while low <= high:
        mid = (low + high) // 2
        # Проверяем, является ли средний элемент искомым
        if array[mid] == value:
            return mid
        # Если искомый элемент меньше среднего элемента, проверяем левую половину массива
        elif array[mid] > value:
            high = mid - 1
        # Иначе проверяем правую половину массива
        else:
            low = mid + 1
    # Если элемент не найден, возвращаем -1
    return -1


random_array = []
for i in range(10):
    random_array.append(randint(0, 10))

print(random_array)

desired_number = 5
# random_array.sort()
# print(random_array)
result = binary_search(random_array, 0, len(random_array) - 1, desired_number)

if result != -1:
    print(f"Элемент {desired_number} найден в позиции {result}")
else:
    print("Элемент не найден")
