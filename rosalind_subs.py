def main():
    filename = "rosalind_subs.txt"

    with open(filename) as f:
        s = f.readline().strip()
        t = f.readline().strip()

    n, m = len(s), len(t)
    locs = []

    for i in range(n - m + 1):
        if s[i : i + m] == t:
            locs.append(i + 1)

    print(*locs)


if __name__ == "__main__":
    main()
