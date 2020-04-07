import argparse
import fileinput
import re


class grep:
    def __init__(self, regexstring, fileslist, colorstring, machineformat, underscoreregexstring):
        self.machineformat = machineformat
        self.underscoreregexstring = underscoreregexstring
        self.colorstring = colorstring
        self.fileslist = fileslist
        self.regexstring = regexstring

    def required_options(regexstring, fileslist):

        parser = argparse.ArgumentParser()
        parser.add_argument('-r', '--regex', metavar='REGEX', required=True, help='regular expression')
        parser.add_argument('-f', '--files', metavar='FILE', nargs='*', required=True,
                            help="files to search in")
        args = parser.parse_args()
