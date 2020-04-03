import argparse


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--underscore', action='store_true', help='prints "^" under the '
                                                                       'matching text')
    group.add_argument('-c', '--color', action='store_true', help="highlight matching text")
    group.add_argument('-m', '--machine', action='store_true', help='generate machine readable '
                                                                    'output')
    parser.add_argument('-r', '--regex', metavar='', required=True, help='regular expression')
    parser.add_argument('-f', '--files', metavar='', required=True, help='files to search in')

    args = parser.parse_args()

    if args.color:
        color_red = '\033[91m'
        color_end = '\033[0m'
        print(color_red + args.regex + color_end)


if __name__ == '__main__':
    main()
