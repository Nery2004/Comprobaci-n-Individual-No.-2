def largest_cross(grid: list[list[int]]) -> int:
    """
    Retorna el tamaño de la cruz (+) más grande formada por 1's.
    Si no existe una cruz válida con brazos de longitud al menos 1
    además del centro, retorna 0.
    """
    if not grid or not grid[0]:
        return 0

    n = len(grid)
    m = len(grid[0])

    left = [[0] * m for _ in range(n)]
    right = [[0] * m for _ in range(n)]
    top = [[0] * m for _ in range(n)]
    bottom = [[0] * m for _ in range(n)]

    # left
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                left[i][j] = 1 if j == 0 else left[i][j - 1] + 1

    # right
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if grid[i][j] == 1:
                right[i][j] = 1 if j == m - 1 else right[i][j + 1] + 1

    # top
    for j in range(m):
        for i in range(n):
            if grid[i][j] == 1:
                top[i][j] = 1 if i == 0 else top[i - 1][j] + 1

    # bottom
    for j in range(m):
        for i in range(n - 1, -1, -1):
            if grid[i][j] == 1:
                bottom[i][j] = 1 if i == n - 1 else bottom[i + 1][j] + 1

    best = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                arm = min(left[i][j], right[i][j], top[i][j], bottom[i][j])

                # arm = 1 significa solo el centro, no cuenta como cruz válida
                if arm >= 2:
                    size = 1 + 4 * (arm - 1)
                    best = max(best, size)

    return best


def main() -> None:
    print("Problema 2 - Cruz más grande con Programación Dinámica")
    print("-" * 58)

    grid1 = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    ]

    grid2 = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0],
    ]

    print(f"Resultado grid1: {largest_cross(grid1)}")
    print(f"Resultado grid2: {largest_cross(grid2)}")


if __name__ == "__main__":
    main()