from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:

    if exp < 0:
        raise ValueError

    if exp == 0:
        return 1

    return x * to_power(x, exp - 1)


print(to_power(2, 3))
print(to_power(3.5, 2))
print(to_power(2, -1))
