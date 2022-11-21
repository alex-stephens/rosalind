from itertools import permutations, product


def alphabet_sort_key(alphabet, x):
    """Returns a key for sorting x according to the order of the letters in alphabet."""
    return [alphabet.index(c) for c in x]


def main():
    filename = "rosalind_lexv.txt"

    with open(filename) as f:
        lines = f.readlines()

    alphabet = lines[0].split()
    n = int(lines[1])

    perm = []
    for i in range(n):
        for p in product(alphabet, repeat=i + 1):
            perm.append("".join(p))

    # Print each permutation sorted according to the English alphabet
    for p in sorted(perm, key=lambda x: alphabet_sort_key(alphabet, x)):
        print(p)


if __name__ == "__main__":
    main()
