from utils import MONISOTOPIC_MASSES


def get_weights(data):
    return sum([MONISOTOPIC_MASSES[c] for c in data])


def main():
    filename = "rosalind_prtm.txt"
    with open(filename) as f:
        s = f.readline().strip()

    print(f"{get_weights(s):.3f}")


if __name__ == "__main__":
    main()
