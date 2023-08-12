#!/usr/bin/python3

if __name__ == '__main__':
    """Print the number of and list of arguments."""
    from sys import argv

    count = len(argv) - 1
    if count < 1:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(count, argv[1]))
    else:
        print("{} arguments:".format(count))
        for ele in range(count):
            print("{}: {}".format(ele + 1, argv[ele + 1]))
