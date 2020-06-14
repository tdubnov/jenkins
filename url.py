"""
Short script calculating sqrt
"""
import sys

def main():
    args = sys.argv[1:]
    print(args)
    try:
        urls = int(args[0])
        sys.exit(1)
    except IndexError:
        print('Please provide at least one url')
        sys.exit(1)
    except ValueError:
        print('Please provide an integer number ./main.py number')
        sys.exit(1)


if __name__ == '__main__':
    main()
