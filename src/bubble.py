"""Module implements bubble sort."""


def bubble_sort(numbers):
    """Bubble-Sort a list of numbers."""
    idx = len(numbers) - 1
    for _ in range(idx):
        for i, x in enumerate(numbers[:idx]):
            try:
                if numbers[i] > numbers[i + 1]:
                    temp = numbers[i]
                    numbers[i], numbers[i + 1] = numbers[i + 1], temp
                    if numbers[i + 1] is numbers[idx]:
                        idx -= 1
            except TypeError:
                raise ValueError("This doesn't bubble strings.")
    return numbers


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'bubble_sort([x for x in range(100)])',
        "from __main__ import bubble_sort"
    )
    worst = Timer(
        'bubble_sort([x for x in range(100)][::-1])',
        "from __main__ import bubble_sort; from random import randint"
        )
    random = Timer(
        'bubble_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import bubble_sort; from random import randint"
    )
    print("#================= best case search 10000x ==============#")
    print(best.timeit(number=1000))
    print('')
    print("#================= worse case search 10000x==============#")
    print(worst.timeit(number=1000))
    print('')
    print("#================= random case search 10000x=============#")
    print(worst.timeit(number=1000))
    print('')
