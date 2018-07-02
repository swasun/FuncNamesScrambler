from parser import Parser
from scrambler import Scrambler
from replacer import Replacer

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="The file that contains the function names to scramble")
    parser.add_argument("--password", help="The password used to encrypt the function names")
    args = parser.parse_args()

    parser = Parser(args.file, def_excludes=['main'], call_excludes=['printf'])

    scrambler = Scrambler(parser, args.password)

    func_names = scrambler.scramble_func_names()

    with open(args.file, 'r') as file:
        source_code = file.read()

    replacer = Replacer(source_code, func_names)

    print(replacer.replace())