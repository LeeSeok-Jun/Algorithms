# N의 팩토리얼(N!) 구하기 문제

# 1. 반복적 방법을 통해 구현
def factorial_iterative(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

print(factorial_iterative(5))

# 2. 재귀적 방법을 통해 구현
def factorial_recursive(n):
    if n <= 1:
        return 1

    # n! = n * (n-1)!
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))