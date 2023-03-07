def compute_internal_nodes(n):
    """Computes the number of internal nodes of a binary tree with n leaves."""

    return n - 2


def main():
    n = 8188
    print(compute_internal_nodes(n))


if __name__ == "__main__":
    main()
