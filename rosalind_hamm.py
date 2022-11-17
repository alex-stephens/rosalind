def main():
    filename = "rosalind_hamm.txt"

    with open(filename) as f:
        s = f.readline().strip()
        t = f.readline().strip()

    print(sum([x != y for x, y in zip(s, t)]))


if __name__ == "__main__":
    main()
