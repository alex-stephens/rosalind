class TrieNode:
    def __init__(self, id):
        self.id = id
        self.children = {}

    def add_child(self, letter, id):
        self.children[letter] = TrieNode(id)
        return self.children[letter]


def build_trie(strings):
    """
    Each node in the trie is a dictionary, where the keys are the letters from the strings.
    """
    # Root node of the trie
    trie = TrieNode(1)
    n = 2

    for string in strings:
        # Start at the root
        current_node = trie

        for c in string:
            # If the current node has a child with the current letter, move to that node
            if c in current_node.children:
                current_node = current_node.children[c]

            # If the current node does not have a child with the current letter, create a new node and add it as a child
            else:
                current_node = current_node.add_child(c, n)
                n += 1

    return trie


def adj_list_helper(node):
    adj_list = {}
    for c in node.children:
        adj_list[(node.id, node.children[c].id)] = c
        adj_list.update(adj_list_helper(node.children[c]))

    return adj_list


def make_adj_list(trie):
    """
    Create an adjacency list from the trie, mapping node ids (i, j) to letters.
    """
    return adj_list_helper(trie)


def print_adj_list(adj_list):
    for k in adj_list:
        print(*k, adj_list[k])


def main():
    filename = "rosalind_trie.txt"

    with open(filename) as f:
        strings = f.read().splitlines()

    trie = build_trie(strings)
    adj_list = make_adj_list(trie)
    print_adj_list(adj_list)


if __name__ == "__main__":
    main()
