import numpy as np


def compute_probablities(string, GC_content):
    probs = []

    for i in range(len(GC_content)):
        x = GC_content[i]

        p_GC = x / 2
        p_AT = (1 - x) / 2

        p = 0

        for c in string:
            if c in "GC":
                p += np.log10(p_GC)
            elif c in "AT":
                p += np.log10(p_AT)
            else:
                raise ValueError("Invalid character in string")

        probs.append(round(p, 3))

    return probs


def main():
    filename = "rosalind_prob.txt"

    with open(filename) as f:
        string = f.readline().strip()
        GC_content = list(map(float, f.readline().split()))

    probs = compute_probablities(string, GC_content)
    print(*probs)


if __name__ == "__main__":
    main()
