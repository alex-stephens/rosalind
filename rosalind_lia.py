from scipy.stats import binom


def compute_probablility(k, N):
    # At each generation, the probability of an organism having the Aa genotype is 0.5 when mating with only Aa organisms. I did check this with code, but deleted that code so you'll have to take my word for it.
    p_Aa = 0.5
    p_AaBb = p_Aa**2

    # Compute probability of having at least N organisms with the AaBb genotype out of a total of 2**k in the the kth generation. Uses the survival function, which is 1 - cdf.
    return binom(2**k, p_AaBb).sf(N - 1)


def main():
    data = "5 8"
    k, N = map(int, data.split())

    prob = compute_probablility(k, N)
    print(f"{prob:.3f}")


if __name__ == "__main__":
    main()
