"""Реализую сортировку пузырьком"""
import time
from random import randint
arr = [randint(0, 100) for i in range(20)]
log_text = f"Исходный массив(первые 20 элементов): \n{arr[0:21]}"

def timeit(func):
    """Функция декоратор для измерения времени выполнения функции"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_runer = f"Время выполнения функции: {(end - start)*1000:.3f} ms"
        return result, time_runer
    return wrapper

@timeit
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr_sort, time_run = bubble_sort(arr)
log_text += f"\nЭлементов в массиве: {len(arr)} \nОтсортированный массив(первые 20 элементов): \n{arr_sort[0:21]} \nВремя выполнения функции: {time_run}\n\n"
with open('log.txt', "a", encoding="utf-8") as file:
    file.write(log_text)