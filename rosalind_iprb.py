import numpy as np


def prob_draw_homo(x, N):
    return x * (x - 1) / (N * (N - 1))


def prob_draw_hetero(x, y, N):
    return x * y / (N * (N - 1))


def main():
    filename = "rosalind_iprb.txt"

    with open(filename) as f:
        k, m, n = map(int, f.readline().split())

    P_DOMINANT = np.array([[1, 1, 1], [1, 0.75, 0.5], [1, 0.5, 0]])
    p_drawn = np.zeros([3, 3])

    N = k + m + n
    vals = [k, m, n]

    for i, x in enumerate(vals):
        for j, y in enumerate(vals):
            if i == j:
                p_drawn[i][j] = prob_draw_homo(x, N)
            else:
                p_drawn[i][j] = prob_draw_hetero(x, y, N)

    print(np.sum(np.multiply(P_DOMINANT, p_drawn)))


if __name__ == "__main__":
    main()
