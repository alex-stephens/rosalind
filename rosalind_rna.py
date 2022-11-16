def main():
    filename = "rosalind_rna.txt"

    with open(filename) as f:
        dna = f.readline()

    print(dna.replace("T", "U"))


if __name__ == "__main__":
    main()
