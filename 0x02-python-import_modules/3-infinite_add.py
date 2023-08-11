#!/usr/bin/python3

if __name__ == '__main__':
    """Print the addition of all arguments."""
    from sys import argv

    _sum = 0
    for ele in range(len(argv) - 1):
        _sum += int(argv[ele + 1])
    print("{}".format(_sum))
