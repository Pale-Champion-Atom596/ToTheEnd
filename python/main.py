import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--filename", type=str)


def main(filename=None):
    if filename is None:
        filename = input("File to be opened: ")
    print(filename)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.filename)
