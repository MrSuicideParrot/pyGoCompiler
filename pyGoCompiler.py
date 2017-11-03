from plintax import parser
from argparse import ArgumentParser
from os.path import isfile


def main():
    argsParser = ArgumentParser(description='Compiler the Go in Python3')

    argsParser.add_argument('-p', '--print_tree', action='store_true', help='Print the abstract tree')
    argsParser.add_argument('-f', '--file', type=str, required=True, help='File')

    args = argsParser.parse_args()

    if not isfile(args.file):
        print('ERRO: Ficheiro inexistente!')
        exit(1)

    with open(args.file, "r") as fd:
        abstract_tree = parser.parse(''.join(fd.readlines()))

    if args.print_tree:
        abstract_tree.pprint()


if __name__ == '__main__':
    main()
