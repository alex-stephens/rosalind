def main():
    filename = "rosalind_revc.txt"

    with open(filename) as f:
        s = f.readline()

    print(reverse(complement(s)))


def reverse(s):
    return s[::-1]


def complement(s):
    COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([COMPLEMENT[c] for c in s])


if __name__ == "__main__":
    main()
