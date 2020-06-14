"""
Short script calculating sqrt
"""
import sys
import math

def main():
    args = sys.argv[1:]
    try:
        num = int(args[0])
    except SyntaxError:
        print('Please provide an integer number ./main.py number')
        sys.exit(1)
    except IndexError:
        print('Please provide an integer number ./main.py number')
        sys.exit(1)
    except ValueError:
        print('Please provide an integer number ./main.py number')
        sys.exit(1)

    for i in range(num):
        print(i, math.sqrt(i))


if __name__ == '__main__':
    main()
