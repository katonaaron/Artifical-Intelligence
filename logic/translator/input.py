"""
Functions for processing the input data.
"""

from commands import Command, Formulas

commentSymbol = "%"
lineSeparator = "."


def processLine(line):
    """
    Processes a single line of the input. It removes the comments and the leading and trailing whitespaces.

    :param line: a line of the input data
    :return: the result after processing, or None if the result is empty.
    """

    # Remove comments
    line = line.split(commentSymbol, 1)[0]

    # Remove leading and trailing whitespace
    line = line.strip()

    # Remove empty lines
    if not line:
        return None

    return line


def changeLineSeparator(lines, separator):
    """
    Given a list of lines, changes the line separator to the given one.
    Thus merges all the lines and separates them by the given separator.

    :param lines: list containing the lines of the input data
    :param separator: the desired line separator
    :return: list of strings representing the lines of the input data separated by the given parameter
    """

    lines = " ".join(lines).split(separator)

    if lines[-1]:
        raise ValueError("Terminating \"%s\" not found" % lineSeparator)

    return map(lambda x: x.strip(), lines[:-1])


def processLines(lines):
    """
    Processes each line of the input data.

    :param lines: list of lines of the input data
    :return: list of non-empty lines of the input data, separated by `lineSeparator`
    """

    # Process each line. Remove the empty lines.
    lines = filter(lambda x: x, map(processLine, lines))

    if not lines:
        raise ValueError("Input file is empty")

    # Change the line separator from the endline character to a different one.
    # Thus merging the lines not terminating in the new character.
    lines = changeLineSeparator(lines, lineSeparator)

    return lines


def linesToCommandsAndFormulas(lines):
    """
    Transforms the lines of data into lists of Command and Formulas objects.

    :param lines: lines of the input data
    :return: (commands, formulas) tuples obtained by parsing the lines
    """
    commands = []
    formulas = []
    formulaName = None
    statements = []

    for line in lines:

        if formulaName:
            if line == Formulas.endCommand:
                formulas.append(Formulas(formulaName, statements))
                formulaName = None
            else:
                statements.append(line)
        else:
            try:
                name, rest = line.split("(", 1)
                args = rest.split(")")[0].split(",")
                args = map(lambda x: x.strip(), args)
            except ValueError:
                raise ValueError("Invalid command format: \"%s\"" % line)

            if name == Formulas.commandName:
                formulaName = args[0]
                statements = []
            else:
                command = Command(name, args)
                commands.append(command)

    return commands, formulas
