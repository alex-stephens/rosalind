def LIS(s):
    n = len(s)

    # dp[i] is a tuple of (length, previous element) for the LIS ending at s[i]
    dp = [(1, None)] * n

    #
    for i in range(1, n):
        for j in range(i):
            if s[i] > s[j] and dp[i][0] < dp[j][0] + 1:
                dp[i] = (dp[j][0] + 1, j)

    # Find the LIS
    i = dp.index(max(dp, key=lambda x: x[0]))  # index of the final element of the LIS
    lis = [s[i]]

    while dp[i][1] is not None:
        i = dp[i][1]
        lis.append(s[i])

    return lis[::-1]


def LDS(s):
    return LIS(s[::-1])[::-1]


def main():
    filename = "rosalind_lgis.txt"
    with open(filename) as f:
        n = int(f.readline().strip())
        s = list(map(int, f.readline().strip().split()))

    print(*LIS(s))
    print(*LDS(s))


if __name__ == "__main__":
    main()
