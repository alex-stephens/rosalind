import numpy as np
from utils import parse_fasta


def build_consensus_matrix(strings):
    """Builds a consensus matrix from a list of strings.
    Rows correspond with "ACGT".
    """

    cm = np.zeros((4, len(strings[0])), dtype=int)
    char_to_ind = {"A": 0, "C": 1, "G": 2, "T": 3}

    for s in strings:
        for i, c in enumerate(s):
            cm[char_to_ind[c], i] += 1

    return cm


def print_consensus_matrix(cm):
    """Prints a consensus matrix."""
    print("A:", *cm[0])
    print("C:", *cm[1])
    print("G:", *cm[2])
    print("T:", *cm[3])


def get_consensus_string(cm):
    """Returns the consensus string of a consensus matrix."""
    consensus = ""
    for col in cm.T:
        consensus += "ACGT"[np.argmax(col)]

    return consensus


def main():
    filename = "rosalind_cons.txt"
    strings = parse_fasta(filename)

    cm = build_consensus_matrix(list(strings.values()))

    print(get_consensus_string(cm))
    print_consensus_matrix(cm)


if __name__ == "__main__":
    main()
