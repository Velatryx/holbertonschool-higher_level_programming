#!/usr/bin/python3


def best_score(a_dictionary):
    for key, value in a_dictionary.items():
        best = next(iter(a_dictionary.values()))
        if value > best:
            best = value
            best_key = key
    return best_key


if __name__ == "__main__":
    a_dictionary = {'Hello': 12, 'Bye': 14, 'Dummy': 10}
    print(best_score(a_dictionary))
