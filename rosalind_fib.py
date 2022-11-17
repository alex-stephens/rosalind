def count_pairs(n, k):

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] * k + dp[i - 1]

    return dp[-1]


def main():
    filename = "rosalind_fib.txt"

    with open(filename) as f:
        n, k = map(int, f.readline().split())

    print(count_pairs(n, k))


if __name__ == "__main__":
    main()
