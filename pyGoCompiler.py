from plintax import parser
import argparse
import sys

def main():
    argsParser = argparse.ArgumentParser()
    argsParser.add_argument('-tree', nargs=1, required=True)
    argsParser.parse_args()
    arg=str(sys.argv[2])
    if arg[-3:] == '.go':
        fd = open(arg, "r")
        result = parser.parse(''.join(fd.readlines()))
        result.pprint()
    else:
        print('O ficheiro escolhido não é código go.')


if __name__ == '__main__':
    main()