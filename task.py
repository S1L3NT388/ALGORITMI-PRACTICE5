import sys
import time
import random

sys.setrecursionlimit(200000)


def partition(arr: list[float], low: int, high: int, ascending: bool) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        condition = (arr[j] <= pivot) if ascending else (arr[j] >= pivot)
        if condition:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort_internal(arr: list[float], low: int, high: int, ascending: bool):
    if low < high:
        pi = partition(arr, low, high, ascending)
        _quick_sort_internal(arr, low, pi - 1, ascending)
        _quick_sort_internal(arr, pi + 1, high, ascending)


def quick_sort(arr: list[float], ascending: bool = True) -> None:
    if len(arr) > 1:
        _quick_sort_internal(arr, 0, len(arr) - 1, ascending)


def is_sorted(arr: list[float], ascending: bool = True) -> bool:
    for i in range(1, len(arr)):
        if ascending:
            if arr[i - 1] > arr[i]:
                return False
        else:
            if arr[i - 1] < arr[i]:
                return False
    return True


def benchmark(size: int, ascending: bool):
    data = [random.uniform(-10000.0, 10000.0) for _ in range(size)]

    start_time = time.perf_counter()
    quick_sort(data, ascending=ascending)
    end_time = time.perf_counter()

    duration_ms = (end_time - start_time) * 1000
    sorted_ok = is_sorted(data, ascending=ascending)

    direction_str = "Зростання (ASC)" if ascending else "Спадання (DESC)"
    print(f"Розмір: {size:7d} | Напрямок: {direction_str} | Впорядковано: {str(sorted_ok):5} | Час: {duration_ms:8.2f} ms")


if __name__ == "__main__":
    print("=== Практична робота №5: Тестування QuickSort ===")

    test_sizes = [1_000, 10_000, 100_000]

    print("\n--- Сортування за зростанням (ascending=True) ---")
    for size in test_sizes:
        benchmark(size, ascending=True)

    print("\n--- Сортування за спаданням (ascending=False) ---")
    for size in test_sizes:
        benchmark(size, ascending=False)