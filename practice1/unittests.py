import unittest

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
class TestBubbleSort(unittest.TestCase):

    def test_sort(self):
        """Тестирование сортировки на стандартных данных"""
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(bubble_sort([5, 5, 5]), [5, 5, 5])
        self.assertEqual(bubble_sort([-1, 0, 1]), [-1, 0, 1])
        self.assertEqual(bubble_sort([100, 99, 101]), [99, 100, 101])

    def test_empty(self):
        """Тестирование пустого списка"""
        self.assertEqual(bubble_sort([]), [])

    def test_single_element(self):
        """Тестирование списка с одним элементом"""
        self.assertEqual(bubble_sort([42]), [42])

    def test_sorted(self):
        """Тестирование уже отсортированного списка"""
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])

    def test_reverse_order(self):
        """Тестирование списка в обратном порядке"""
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])

    def test_mixed(self):
        """Тестирование списка с случайным порядком"""
        self.assertEqual(bubble_sort([9, 1, 5, 3, 7, 2]), [1, 2, 3, 5, 7, 9])


if __name__ == "__main__":
    unittest.main()
