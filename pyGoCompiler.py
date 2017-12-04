from plintax import parser
from argparse import ArgumentParser
from tabelaDeSimbolos import Tabela
import tree
import InterCode
from os.path import isfile
from os import devnull
from sys import stderr


def main():
    debug = False

    if not debug:
        stderr = open(devnull, 'w')

    argsParser = ArgumentParser(description='Compiler the Go in Python3')

    argsParser.add_argument('-p', '--print_tree', action='store_true', help='Print the abstract tree')
    argsParser.add_argument('file', metavar='f', nargs='+', type=str, help='File')

    args = argsParser.parse_args()
    for i in args.file:
        if not isfile(i):
            print('ERRO: Ficheiro ',i,' inexistente!')
            continue

        with open(i, "r") as fd:
            abstract_tree = parser.parse(''.join(fd.readlines()))

        if args.print_tree:
            abstract_tree.pprint()

        tree.Elemento.setTable(Tabela(abstract_tree))

        x= abstract_tree.getInstructionList()

        InterCode.printASM("a.asm", x)

if __name__ == '__main__':
    main()
