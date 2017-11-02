from plintax import parser
from argparse import ArgumentParser

def main():
    argsParser = ArgumentParser(description='Compilador de código go em python.')
    argsParser.add_argument('-t', '--tree', nargs=1, type=str, dest='file', required=True)
    args=argsParser.parse_args()
    arg=args.file[0]
    if arg[-3:] == '.go':
        fd = open(arg, "r")
        result = parser.parse(''.join(fd.readlines()))
        result.pprint()
    else:
        print('O ficheiro escolhido não é código go.')

if __name__ == '__main__':
    main()