"""
Main program
"""

import getopt
import os
import sys

from expression import formulasToExpressionTree, createSubstitutions
from input import processLines, linesToCommandsAndFormulas
from output import printCommandsAndFormulas

# Name of the program
programName = os.path.basename(__file__)

# Program configuration
inputFile = sys.stdin
mod2Output = False
collect = False
substitute = False
merge = False

# Help message
usage = "%s [options] [-f <inputfile>]" % programName
description = "A converter from propositional logic to modular arithmetic in the mace4 format"
help_message = """
Usage: %s

%s

Options:
    -c,\t--collect\tCollects the terms of each expression by the decreasing frequency of their symbols.
    -h,\t--help\t\tPrints help message
    -f,\t--file string\tPath to the input file. If the option is missing, the program reads from STDIN 
    -m,\t--merge\t\tMerges all the expressions of a "formulas" section into a single expression.
    \t--mod\t\tWraps all expressions in "mod 2"
    -s,\t--subs\t\tSubstitutes symbols with their corresponding expression. The substitutions must be given in the "a <-> f(b)." format in "formulas(substitutions)."
""" % (usage, description)


def processArguments(argv):
    """
    Reads the command line arguments of the program and updates respectively the global variables

    :param argv: the command line arguments, list of strings
    :return: None
    """
    global inputFile, mod2Output, collect, substitute, merge

    try:
        opts, args = getopt.getopt(argv, "hcsmf:", ["mod", "help", "collect", "subs", "merge","file="])
    except getopt.GetoptError:
        print help_message
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            print help_message
            sys.exit()
        elif opt in ['-f', '--file']:
            inputFile = open(arg, 'r')
        elif opt == '--mod':
            mod2Output = True
        elif opt in ['-c', '--collect']:
            collect = True
        elif opt in ['-s', '--subs']:
            substitute = True
        elif opt in ['-m', '--merge']:
            merge = True


def main(argv):
    """
    Main program.

    Reads the command line arguments.
    Reads and processes the input data.
    Prints the result to STDOUT.

    :param argv: the command line arguments, list of strings
    :return: None
    """
    processArguments(argv)
    lines = processLines(inputFile.readlines())

    commands, formulas = linesToCommandsAndFormulas(lines)

    substitutions = None
    if substitute:
        try:
            substitutionFormulas = next(f for f in formulas if f.name == "substitutions")
        except StopIteration:
            raise ValueError('Cannot substitute. \"formulas(substitutions).\" does not exists')
        substitutions = createSubstitutions(substitutionFormulas.formulaList)
        formulas.remove(substitutionFormulas)

    formulas = map(lambda f: formulasToExpressionTree(f, simplify=True, collect=collect, substitutions=substitutions, merge=merge),
                   formulas)

    printCommandsAndFormulas(commands, formulas, mod2Output=mod2Output)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except ValueError as e:
        sys.stderr.write('Error: ' + str(e))
        sys.exit(1)
