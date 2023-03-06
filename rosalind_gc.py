import numpy as np


def get_gc_content(string):
    counts = string.count("G") + string.count("C")
    return 100 * counts / len(string)


def main():
    filename = "rosalind_gc.txt"

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

    id = list(strings.keys())
    gc_content = np.array([get_gc_content(strings[i]) for i in id])

    ind_max = np.argmax(gc_content)
    print(id[ind_max], gc_content[ind_max], sep="\n")


if __name__ == "__main__":
    main()
