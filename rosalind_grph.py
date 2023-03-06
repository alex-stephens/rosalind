from utils import parse_fasta


def overlap(s1, s2, k):
    return s1[-k:] == s2[:k]


def build_adj_list(strings, k):
    adj = []

    for x in strings:
        for y in strings:
            if x == y:
                continue
            if overlap(strings[x], strings[y], k):
                adj.append((x, y))

    return adj


def main():
    filename = "rosalind_grph.txt"

    strings = parse_fasta(filename)

    k = 3
    adj = build_adj_list(strings, k)

    for a in adj:
        print(*a)


if __name__ == "__main__":
    main()
