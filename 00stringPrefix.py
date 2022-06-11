from itertools import combinations


def compare(dct, x, y):
    return dct[x] == dct[y]


string_dict = {
    "_default": "string",
    "_format": f"string",
    "_bytes": b"string",
    "_unicode": u"string",
    "_raw": r"string"
}

for c in combinations(string_dict.keys(), 2):
    print(f"compare {c[0]} & {c[1]} -> {compare(string_dict, c[0], c[1])}")
