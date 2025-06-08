import random
import time
import matplotlib.pyplot as plt
import numpy as np


def randomized_quick_sort(nums: list, fst: int, lst: int):
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    randomized_quick_sort(nums, fst, j)
    randomized_quick_sort(nums, i, lst)


def deterministic_quick_sort(nums: list, fst: int, lst: int):
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = nums[fst]

    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    deterministic_quick_sort(nums, fst, j)
    deterministic_quick_sort(nums, i, lst)


def measure_sort_time(func, array: list, exps=5):
    times = []
    for _ in range(exps):
        start_time = time.perf_counter()
        func(array.copy(), 0, len(array) - 1)
        times.append(time.perf_counter() - start_time)
    return np.mean(times)


def generate_data(sizes: list) -> dict:
    return {size: [random.randint(0, 10**6) for _ in range(size)] for size in sizes}


def draw_results(results):
    fig, ax = plt.subplots()

    ax.plot(
        results["size"],
        results["rQS"],
        "o-",
        linewidth=2,
        label="Рандомізований QuickSort",
    )
    ax.plot(
        results["size"],
        results["dQS"],
        "o-",
        linewidth=2,
        color="orange",
        label="Детермінований QuickSort",
    )

    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого і детермінованого QuickSort")

    ax.legend(loc="upper left")

    plt.show()


def main(sizes: list, exps: int):
    results = {"size": [], "dQS": [], "rQS": []}

    for size, array in generate_data(sizes).items():
        results["size"].append(size)
        print(f"\nРозмір масиву: {size}")

        rQS_time = measure_sort_time(randomized_quick_sort, array, exps)
        results["rQS"].append(rQS_time)
        print(f"   Рандомізований QuickSort: {rQS_time:.4f} секунд")

        dQS_time = measure_sort_time(deterministic_quick_sort, array, exps)
        results["dQS"].append(dQS_time)
        print(f"   Детермінований QuickSort: {dQS_time:.4f} секунд")

    draw_results(results)


if __name__ == "__main__":
    main([10_000, 50_000, 100_000, 500_000], 5)
