from itertools import permutations, product


def main():
    n = 5

    prod = list(product([-1, 1], repeat=n))
    perm = list(permutations(range(1, n + 1)))

    print(len(prod) * len(perm))

    for p in prod:
        for q in perm:
            print(*[p[i] * q[i] for i in range(n)])


if __name__ == "__main__":
    main()
