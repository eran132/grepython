import argparse
import fileinput
import re


def common():
    common_parser = argparse.ArgumentParser()
    common_parser.add_argument('-r', '--regex', metavar='REGEX', required=True, help='regular expression')
    common_parser.add_argument('-f', '--files', metavar='FILE', required=True, help="files to search in, STDIN is "
                                                                                    "used if not file specified")
    common_args = common_parser.parse_args()
    for line in fileinput.input(files=common_args.files if len(common_args.files) > 0 else ('-',)):
        line = re.search(common_args.regex, line)
        print(fileinput.filename(), fileinput.filelineno(), line)


def optional():
    optional_parser = argparse.ArgumentParser()
    group = optional_parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--underscore', help='prints "^" under the '
                                                  'matching text')
    group.add_argument('-c', '--color', help="highlight matching text")
    group.add_argument('-m', '--machine', help='generate machine readable '
                                               'output')
    optional_args = optional_parser.parse_args()

    if optional_args.color:
        color_red = '\033[91m'
        color_end = '\033[0m'
        print(color_red + optional_args.regex + color_end)


if __name__ == '__common__':
    common()
