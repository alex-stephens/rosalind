import numpy as np

from utils import parse_fasta


def calculate_distance(s1, s2):
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance / len(s1)


def build_distance_matrix(strings):
    n = len(strings)
    dm = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1):
            dm[i][j] = calculate_distance(strings[i], strings[j])
            dm[j][i] = dm[i][j]

    return dm


def main():
    filename = "rosalind_pdst.txt"
    strings = list(parse_fasta(filename).values())

    dm = build_distance_matrix(strings)
    for row in dm:
        print(*row)


if __name__ == "__main__":
    main()
