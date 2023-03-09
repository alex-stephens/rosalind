from urllib.request import urlopen

# def is_match()


def expand_motif(motif):
    expanded = []
    stack = []

    for i, c in enumerate(motif):
        if c == "{":
            stack.append(i)
        elif c == "}":
            start = stack.pop()
            end = i
            expanded.append(motif[start : end + 1])
        elif c == "[":
            stack.append(i)
        elif c == "]":
            start = stack.pop()
            end = i
            expanded.append(motif[start : end + 1])
        elif len(stack) == 0:
            expanded.append(c)

    return tuple(expanded)


def get_sequences(ids):
    sequences = {}

    for id in ids:
        id_shortened = id.split("_")[0]
        url = f"http://www.uniprot.org/uniprot/{id_shortened}.fasta"
        with urlopen(url) as f:
            file = f.read().decode("utf-8")
            lines = file.splitlines()
            sequence = "".join(lines[1:])
            sequences[id] = sequence

    return sequences


def is_match(sequence, motif):
    """Returns true if the given sequence exactly matches the motif."""
    if len(sequence) != len(motif):
        return False

    for i in range(len(sequence)):
        if motif[i].startswith("["):
            if sequence[i] not in motif[i][1:-1]:
                return False
        elif motif[i].startswith("{"):
            if sequence[i] in motif[i][1:-1]:
                return False
        elif sequence[i] != motif[i][0]:
            return False

    return True


def get_indices_of_motif(sequence, motif):
    indices = []
    n = len(motif)

    for i in range(len(sequence) - n + 1):
        if is_match(sequence[i : i + n], motif):
            indices.append(i + 1)

    return indices


def main():
    filename = "rosalind_mprt.txt"

    with open(filename) as f:
        ids = [line.strip() for line in f]

    sequences = get_sequences(ids)
    motif = expand_motif("N{P}[ST]{P}")

    for id in sequences:
        indices = get_indices_of_motif(sequences[id], motif)
        if len(indices) > 0:
            print(id)
            print(*indices)


if __name__ == "__main__":
    main()
