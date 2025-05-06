
import random
import time
import sys
sys.setrecursionlimit(200000)

class Metrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

def bubble_sort(arr, metrics):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            metrics.comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                metrics.swaps += 1

def selection_sort(arr, metrics):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            metrics.comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            metrics.swaps += 1

def insertion_sort(arr, metrics):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            metrics.comparisons += 1
            arr[j + 1] = arr[j]
            metrics.swaps += 1
            j -= 1
        metrics.comparisons += 1 if j >= 0 else 0
        arr[j + 1] = key

def merge_sort(arr, metrics):
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            metrics.comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                metrics.swaps += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], metrics)
    right = merge_sort(arr[mid:], metrics)
    return merge(left, right)

def quick_sort(arr, metrics):
    def partition(low, high):
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            metrics.comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                metrics.swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        metrics.swaps += 1
        return i + 1

    def quicksort_rec(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_rec(low, pi - 1)
            quicksort_rec(pi + 1, high)

    quicksort_rec(0, len(arr) - 1)

def heap_sort(arr, metrics):
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n:
            metrics.comparisons += 1
            if arr[l] > arr[largest]:
                largest = l
        if r < n:
            metrics.comparisons += 1
            if arr[r] > arr[largest]:
                largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            metrics.swaps += 1
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        metrics.swaps += 1
        heapify(i, 0)

def run_test(name, sort_func, data):
    arr = data.copy()
    metrics = Metrics()
    start = time.perf_counter()
    if name == "Merge Sort":
        arr = sort_func(arr, metrics)
    else:
        sort_func(arr, metrics)
    end = time.perf_counter()
    return {
        'tempo_ms': (end - start) * 1000,
        'comparacoes': metrics.comparisons,
        'trocas': metrics.swaps
    }

def gerar_dados(tipo, tamanho):
    if tipo == 'sorted':
        return list(range(tamanho))
    elif tipo == 'reversed':
        return list(range(tamanho, 0, -1))
    else:
        return random.sample(range(tamanho * 2), tamanho)

algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
    ("Heap Sort", heap_sort),
]

for tamanho in [100000]:
    for tipo in ['sorted', 'reversed', 'random']:
        print(f"\nTamanho: {tamanho} | Entrada: {tipo}")
        data = gerar_dados(tipo, tamanho)
        for name, func in algorithms:
            print(f"  {name}...", end=" ")
            try:
                result = run_test(name, func, data)
                print(f"Tempo: {result['tempo_ms']:.2f} ms | Comp: {result['comparacoes']} | Trocas: {result['trocas']}")
            except RecursionError:
                print("Erro: RecursionError")
