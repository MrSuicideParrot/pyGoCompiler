from plintax import *

def main():
    file = True
    if not file:
        while True:
            try:
                s = input('calc > ')
            except EOFError:
                print()
                break
            if not s:
                continue
            result = parser.parse(s)
            if result is not None:
                print(result)
    else:
        fd = open("example1.go", "r")
        result = parser.parse(''.join(fd.readlines()))
        result.pprint()


if __name__ == '__main__':
    main()