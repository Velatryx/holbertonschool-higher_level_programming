#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except:
            break
    print()
    return count


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 'Hello']
    print(safe_print_list(my_list, x=9))
