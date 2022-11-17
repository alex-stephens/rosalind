from math import factorial
from itertools import permutations


def main():
    n = 7

    print(factorial(n))
    print(*[" ".join(map(str, p)) for p in permutations(range(1, n + 1))], sep="\n")


if __name__ == "__main__":
    main()
