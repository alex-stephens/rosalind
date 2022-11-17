import numpy as np


def main():
    filename = "rosalind_iev.txt"

    with open(filename) as f:
        data = np.array(list(map(int, f.readline().split(" "))))

    PROBS = np.array([1.0, 1.0, 1.0, 0.75, 0.5, 0.0])
    exp_offspring = 2 * np.sum(np.multiply(data, PROBS))

    print(exp_offspring)


if __name__ == "__main__":
    main()
