def count_pairs(n, m):

    # dp[n] is the number of new rabbits born in month n
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(max(1, i - m), i - 1):
            dp[i] += dp[j]

    # Number of rabbits alive after month n
    return sum(dp[-m:])


def main():
    filename = "rosalind_fibd.txt"

    with open(filename) as f:
        n, m = map(int, f.readline().split())

    print(count_pairs(n, m))


if __name__ == "__main__":
    main()
