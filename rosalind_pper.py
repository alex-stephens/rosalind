import math


def count_partial_permutations(n, k, modulo=1000000):
    return math.comb(n, k) * math.factorial(k) % modulo


def main():
    data = "86 10"

    n, k = map(int, data.split())
    permutations = count_partial_permutations(n, k, modulo=1000000)

    print(permutations)


if __name__ == "__main__":
    main()
