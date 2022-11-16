def main():
    filename = "rosalind_dna.txt"

    with open(filename) as f:
        dna = f.readline()

    print(" ".join([str(dna.count(c)) for c in "ACGT"]))


if __name__ == "__main__":
    main()
