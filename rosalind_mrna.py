from utils import RNA_CODON_TABLE


def get_codon_freqs():
    codon_freqs = dict()
    for codon in RNA_CODON_TABLE:
        if RNA_CODON_TABLE[codon] in codon_freqs:
            codon_freqs[RNA_CODON_TABLE[codon]] += 1
        else:
            codon_freqs[RNA_CODON_TABLE[codon]] = 1
    return codon_freqs


def main():
    filename = "rosalind_mrna.txt"

    with open(filename) as f:
        data = f.readline().strip()

    modulo = 10**6

    codon_freqs = get_codon_freqs()
    stop_freq = codon_freqs["Stop"]

    num_strings = stop_freq

    for c in data:
        num_strings *= codon_freqs[c]
        num_strings %= modulo

    print(num_strings)


if __name__ == "__main__":
    main()
