def main():
    filename = "rosalind_tree.txt"

    with open(filename) as f:
        n = int(f.readline().strip())
        edges = [tuple(map(int, line.strip().split())) for line in f.readlines()]

    print(n - len(edges) - 1)


if __name__ == "__main__":
    main()
