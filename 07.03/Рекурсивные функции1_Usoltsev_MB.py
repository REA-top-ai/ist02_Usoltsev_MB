import time


def factorial_with_recursion (n):
    if n == 1: return 1
    else:
        return n * factorial_with_recursion(n-1)


def factorial_without_recursion (n):
    comp = 1
    for i in range(1, n+1):
        comp *= i
    return comp


n = 100
start = time.time()
factorial_with_recursion(n)
rec_time = time.time() - start

start = time.time()
factorial_without_recursion(n)
iter_time = time.time() - start

print(f"Рекурсия: {rec_time:.6f} сек")
print(f"Итерация: {iter_time:.6f} сек")
print(f"Итерация быстрее в {rec_time/iter_time:.2f} раз")