def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    # Проверки с использованием assert
    assert bubble_sort([3, 1, 2]) == [1, 2, 3], "Ошибка: bubble_sort([3, 1, 2]) должно вернуть [1, 2, 3]"
    assert bubble_sort([5, 5, 5]) == [5, 5, 5], "Ошибка: bubble_sort([5, 5, 5]) должно вернуть [5, 5, 5]"
    assert bubble_sort([-1, 0, 1]) == [-1, 0, 1], "Ошибка: bubble_sort([-1, 0, 1]) должно вернуть [-1, 0, 1]"
    assert bubble_sort([100, 99, 101]) == [99, 100, 101], "Ошибка: bubble_sort([100, 99, 101]) должно вернуть [99, 100, 101]"

