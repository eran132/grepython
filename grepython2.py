import argparse
import fileinput

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--regex', metavar='REGEX', required=True, help='regular expression')
parser.add_argument('-f', '--files', metavar='FILE', nargs='*', required=True, help="files to search in, stdin is "
                                                                                    "used if not file specified")

# group = parser.add_mutually_exclusive_group()
# group.add_argument('-u', '--underscore', help='prints "^" under the '
#                                               'matching text')
# group.add_argument('-c', '--color', help="highlight matching text")
# group.add_argument('-m', '--machine', help='generate machine readable '
#                                            'output')
args = parser.parse_args()

for line in fileinput.input(files=args.files if len(args.files) > 0 else ('-',)):
    print(fileinput.filename(), fileinput.filelineno(), line)

    # if optional_args.color:
    #     color_red = '\033[91m'
    #     color_end = '\033[0m'
    #     print(color_red + optional_args.regex + color_end)

    # files_with_string = args.files
    # for file in fileinput.input(files=files_with_string):
    #     if args.color:
    #         color_red = '\033[91m'
    #         color_end = '\033[0m'
    #         print(color_red + args.regex + color_end)

# print("filename:", fileinput.filename(), " line number:", fileinput.filelineno())
# for line in fileinput.input(common_args.files):
#     line = re.search(common_args.regex, line)
#     print(fileinput.filename(), fileinput.filelineno(), line)
