from utils import parse_fasta


def get_lcs(strings):
    shortest = min(strings, key=len)

    for length in range(len(shortest), 0, -1):
        for i in range(len(shortest) - length):
            sub = shortest[i : i + length + 1]
            if all(sub in s for s in strings):
                return sub

    return ""


def main():
    filename = "rosalind_lcsm.txt"
    strings = parse_fasta(filename)

    lcs = get_lcs(list(strings.values()))
    print(lcs)


if __name__ == "__main__":
    main()
