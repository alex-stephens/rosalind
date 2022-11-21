from itertools import product


def main():
    filename = "rosalind_lexf.txt"

    with open(filename) as f:
        lines = f.readlines()

    alphabet = lines[0].split()
    n = int(lines[1])

    perm = list(product(alphabet, repeat=n))

    # Print each permutation sorted according to the English alphabet
    for p in sorted(perm):
        print("".join(p))


if __name__ == "__main__":
    main()
