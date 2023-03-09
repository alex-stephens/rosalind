from utils import parse_fasta


def complement(s):
    COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(list(map(lambda x: COMPLEMENT[x], s)))


def find_palindromes(s):
    LMIN = 4
    LMAX = 12

    palindromes = []

    for length in range(LMIN, LMAX + 1, 2):
        for i in range(len(s) - length + 1):
            sub = s[i : i + length]
            if sub == complement(sub[::-1]):
                palindromes.append((i + 1, length))

    return sorted(palindromes, key=lambda x: x[0])


def main():
    filename = "rosalind_revp.txt"
    strings = parse_fasta(filename)

    palindromes = find_palindromes(list(strings.values())[0])

    for p in palindromes:
        print(*p)


if __name__ == "__main__":
    main()
