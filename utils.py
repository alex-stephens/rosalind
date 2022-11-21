def parse_fasta(filename):
    """Parses a FASTA file and returns a dictionary of the form {id: sequence}."""
    strings = dict()
    cur_id = None

    with open(filename) as f:

        while True:

            line = f.readline().strip()
            if not line:
                break

            if line.startswith(">"):
                cur_id = line[1:]
                strings[cur_id] = ""
                continue

            strings[cur_id] += line

    return strings
