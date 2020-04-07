import argparse
import fileinput
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--regex', help='regular expression')
    parser.add_argument('-f', '--files', nargs='*', help="files to search in, stdin is "
                                                         "used if not file specified",
                        default='-')
    args = parser.parse_args()
    pattern = re.compile(args.regex)

    for line in fileinput.input(args.files):
        if pattern.search(line):
            if fileinput.isstdin():
                format_of_print = '{lineno}:{line}'
            else:
                format_of_print = '{files:<10}:{lineno:<10}:{line}'
            print(format_of_print.format(files=fileinput.filename(), lineno=fileinput.filelineno(),
                                         line=line.rstrip()))
