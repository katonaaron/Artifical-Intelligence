class Command:
    """
    Class for representing mace4 commands.
    Commands are given as: command_name(argument1[,argument2,...]).
    """
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __str__(self):
        return "Command(%s, %s)" % (self.name, self.args)

    def __repr__(self):
        return self.__str__()


class Formulas:
    """
    Class for representing mace4 formulas.
    Formulas are given as:
        formulas(name).
            predicate1.
            [predicate2.
            ...]
        end_of_list.
    """

    commandName = "formulas"
    endCommand = "end_of_list"

    def __init__(self, name, formula_list):
        self.name = name
        self.formulaList = formula_list

    def __str__(self):
        return "Formulas(%s, %s)" % (self.name, self.formulaList)

    def __repr__(self):
        return self.__str__()
