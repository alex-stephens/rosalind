from utils import parse_fasta, RNA_CODON_TABLE


def translate(rna):
    protein = ""

    for i in range(0, len(rna), 3):
        codon = rna[i : i + 3]
        if RNA_CODON_TABLE[codon] == "Stop":
            break
        protein += RNA_CODON_TABLE[codon]

    return protein


def main():
    filename = "rosalind_splc.txt"

    strings = parse_fasta(filename, ordered=True)
    keys = list(strings.values())

    dna = keys[0]
    introns = keys[1:]

    for intron in introns:
        dna = dna.replace(intron, "")
    rna = dna.replace("T", "U")

    print(translate(rna))


if __name__ == "__main__":
    main()
