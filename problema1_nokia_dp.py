
## `problema1_nokia_dp.py`
from functools import lru_cache

# Lista de movimientos válidos desde cada dígito.
# Se incluye quedarse en la misma tecla.
ADJ = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [2, 1, 3, 5],
    3: [3, 2, 6],
    4: [4, 1, 5, 7],
    5: [5, 2, 4, 6, 8],
    6: [6, 3, 5, 9],
    7: [7, 4, 8],
    8: [8, 5, 7, 9, 0],
    9: [9, 6, 8],
}


@lru_cache(maxsize=None)
def dp(digit: int, length: int) -> int:
    """
    Retorna la cantidad de secuencias válidas de longitud `length`
    que inician en el dígito `digit`.
    """
    if length == 1:
        return 1

    total = 0
    for nxt in ADJ[digit]:
        total += dp(nxt, length - 1)
    return total


def total_combinations(n: int) -> int:
    """
    Retorna la cantidad total de combinaciones válidas de longitud n,
    pudiendo iniciar desde cualquier dígito del 0 al 9.
    """
    if n <= 0:
        return 0

    total = 0
    for digit in range(10):
        total += dp(digit, n)
    return total


def main() -> None:
    print("Problema 1 - Teclado Nokia con Programación Dinámica")
    print("-" * 55)

    test_n_2 = 2
    result_n_2 = total_combinations(test_n_2)
    print(f"n = {test_n_2} -> {result_n_2}")

    test_n_10 = 10
    result_n_10 = total_combinations(test_n_10)
    print(f"n = {test_n_10} -> {result_n_10}")


if __name__ == "__main__":
    main()