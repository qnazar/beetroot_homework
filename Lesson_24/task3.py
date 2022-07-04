def mult(a: int, n: int) -> int:

    if n < 0:
        raise ValueError

    if n == 0:
        return 0

    return a + mult(a, n-1)


print(mult(2, 4))
