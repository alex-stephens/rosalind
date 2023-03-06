def main():
    filename = "rosalind_seto.txt"
    with open(filename) as f:
        n = int(f.readline().strip())
        A = set(map(int, f.readline().strip()[1:-1].split(",")))
        B = set(map(int, f.readline().strip()[1:-1].split(",")))

    S = set(range(1, n + 1))

    print(A.union(B))
    print(A.intersection(B))
    print(A.difference(B))
    print(B.difference(A))
    print(S.difference(A))
    print(S.difference(B))


if __name__ == "__main__":
    main()
