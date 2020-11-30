"""
Functions for printing the program output to STDOUT.
"""


def printCommand(command):
    """
    Prints an instance of the Command class.

    :param command: command to be printed
    :return: None
    """
    print command.name + '(' + ', '.join(command.args) + ').'


def printCommands(commands):
    """
    Prints a list of Command objects.

    :param commands: list of commands to be printed
    :return: None
    """
    for command in commands:
        if command.args and command.args[0] not in ['arithmetic', 'domain_size']:
            printCommand(command)
    print "set(arithmetic)."
    print "assign(domain_size, 2)."


def printFormulas(formulas, mod2Output=False):
    """
    Prints an instance of the Formulas class.

    :param formulas: object to be printed
    :param mod2Output: if True: wraps each expression with "mod 2"
    :return: None
    """
    print formulas.commandName + '(' + formulas.name + ').'

    for expression in formulas.formulaList:
        if mod2Output:
            print '\t(' + str(expression) + ') mod 2 = 1.'
        else:
            print '\t' + str(expression) + ' = 1.'

    print formulas.endCommand + '.'


def printFormulasList(formulasList, mod2Output=False):
    """
    Prints a list of Formulas objects.

    :param formulasList: list of objects to be printed
    :param mod2Output: if True: wraps each expression with "mod 2"
    :return: None
    """
    for formulas in formulasList:
        printFormulas(formulas, mod2Output)
        print


def printCommandsAndFormulas(commands, formulas, mod2Output=False):
    """
    Prints a list of Command and a list of Formulas objects.

    :param commands: list of Command objects to be printed
    :param formulas: list of Formulas objects to be printed
    :param mod2Output: if True: wraps each formula expression with "mod 2"
    :return: None
    """
    printCommands(commands)
    print
    printFormulasList(formulas, mod2Output)
