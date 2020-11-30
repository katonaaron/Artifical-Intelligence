"""
Functions for
- creating sympy expression trees in mod 2 arithmetics from proposition logic.
- transforming sympy expression trees
"""
import re

import sympy
from sympy import Mul, Add, Symbol, Poly

from commands import Formulas

# Priorities of the propositional logic operators
priority = {
    "(": 0,
    ")": 0,
    "->": 1,
    "<->": 1,
    "|": 2,
    "&": 3,
    "-": 4
}


def is_symbol_char(char):
    """
    Verifies whether a character can be part of a symbol or not.

    :param char: character to be verified
    :return: True or False
    """
    return re.search("^[a-zA-z0-9]+$", char) is not None


def operatorStringToExpression(operator, *operands):
    """
    Given a string representing a propositional logic operator, returns a simpy expression which is the modular
    arithmetic translation of the operator.

    This function simplifies the expression according to the rules of general algebra and does not consider the rules of
    the mod 2 arithmetics.

    :param operator: string representing a propositional logic operator
    :param operands: list of simpy expressions or integers
    :return: simpy expression which results from applying the operands to the translated operator
    """
    if operator == "&":
        return Mul(*operands)
    elif operator == "-":
        return Add(operands[0], 1)
    elif operator == "|":
        return Add(Add(*operands), Mul(*operands))
    elif operator == "<->":
        return Add(Add(*operands), 1)
    elif operator == "->":
        return Add(Mul(*operands), Add(operands[0], 1))
    else:
        raise ValueError("Unknown operator \"%s\"" % operator)


def splitProposition(proposition):
    """
    Splits a proposition into terms of operands and operators.

    :param proposition: proposition to be split
    :return: list of strings representing the operands and operators of the proposition in order
    """
    terms = []
    is_symbol = is_symbol_char(proposition[0])
    term = ""

    def addTerm(t):
        t = t.strip()
        if t:
            terms.append(t)

    for char in proposition:
        is_symbol2 = is_symbol_char(char)

        if char in " ":
            addTerm(term)
            term = ""
            is_symbol = False
            continue

        if char in "()":
            addTerm(term)
            term = ""
            is_symbol = False
            terms.append(char)
            continue

        if is_symbol == is_symbol2:
            term = term + char
        else:
            addTerm(term)
            term = char

        is_symbol = is_symbol2

    if term:
        addTerm(term)

    return terms


def buildExpressionTree(proposition, substitutions=None):
    """
    Builds a sympy expression tree from the given proposition in propositional logic.

    The result is an expression (tree) in modulo 2 arithmetics. However it is simplified based only on the general rules
    of algebra. E.g. x * x will be x**2 instead of x.

    Substitutes the symbols to the simpy expressions associated with them in the substitutions dictionary.

    :param proposition: string, in propositional logic
    :param substitutions: a dictionary whose elements are (string_symbol, (expression, symbols)).
                          No substitution if None is given.
        string_symbol: the string which will be substituted
        expression: a sympy expression which substitutes the string
        symbols: the list of sympy symbols that are present in the expression
    :return: a simpy expression (tree)
    """
    operators = set(priority.keys())

    node_stack = []
    term_stack = []
    symbols = set()

    terms = splitProposition(proposition)

    def createAndPush():
        """
        Creates a new node and pushes to the node stack

        :return: None
        """
        op = term_stack.pop()

        if op == '-':
            # Unary operator
            node = operatorStringToExpression(op, node_stack.pop())
        else:
            # Binary operator
            right = node_stack.pop()
            left = node_stack.pop()
            node = operatorStringToExpression(op, left, right)

        node_stack.append(node)

    for term in terms:
        if term == '(':
            term_stack.append(term)
        elif term not in operators:
            if not substitutions or term not in substitutions:
                node = Symbol(term)
                symbols.add(node)
            else:
                node, node_symbols = substitutions[term]
                symbols.update(node_symbols)
            node_stack.append(node)
        elif priority[term] > 0:
            while term_stack \
                    and term_stack[-1] != '(' \
                    and priority[term_stack[-1]] >= priority[term]:
                createAndPush()

            term_stack.append(term)

        elif term == ')':
            while term_stack and term_stack[-1] != '(':
                createAndPush()
            term_stack.pop()

    while term_stack:
        createAndPush()

    return node_stack[-1], symbols


def simplifyExpression(expr, symbols):
    """
    Simplifies a sympy expression by applying also the rules of the boolean ring.

    1. Uses the sympy.simplify function for modulus 2 (implicitly, by creating a polynomial).
    2. Replaces all the powers with their bases. Because x * x = x for all x in {0, 1}.

    :param expr: sympy expression to be simplified
    :param symbols: symbols that are used in the expression
    :return: the simplified sympy expression
    """

    def recurse_replace(expr, func):
        """
        Traverses the expression tree in a DFS order and replaces all nodes with the result of applying them to the
        given function.

        :param expr: the expression tree
        :param func: the transformation function
        :return: the transformed expression tree
        """
        if len(expr.args) == 0:
            return expr
        else:
            new_args = tuple(recurse_replace(a, func) for a in expr.args)
            return func(expr, new_args)

    def rewrite(expr, new_args):
        """
        Traverses the arguments of a sympy expression node. If an argument is a power, it is replaced by the base of the
        power.

        :param expr: expression node or polynomial whose arguments are verified
        :param new_args: a list of nodes (simpy expression or integer) that would be the new arguments of the expr node.
        :return: an object having the same type as expr, and having as arguments the transformed new_args list.
        """
        args = []

        for arg in new_args:
            if hasattr(arg, 'is_Pow') and arg.is_Pow:
                args.append(arg.args[0])
            else:
                args.append(arg)

        if hasattr(expr, 'is_Poly') and expr.is_Poly:
            return Poly(args[0], expr.gens)
        else:
            new_node = type(expr)(*args)
            return new_node

    p = Poly(expr, symbols, modulus=2)
    p = recurse_replace(p, rewrite).set_modulus(2)

    return p.as_expr()


def getSymbolsByDecreasingFrequency(expression):
    """
    Returns all the symbols of the given sympy expression in decreasing order of their frequency of appearance.

    Example:
    expression: m1 + r1*r2 + r1 + 1
    frequency: {m1: 1, r2: 1, r1: 2}
    result: [r1, m1, r2]

    :param expression: sympy expression
    :return: list of sympy symbols
    """
    freq = {}
    for node in sympy.preorder_traversal(expression):
        if hasattr(node, 'is_Symbol') and node.is_Symbol:
            freq[node] = freq.get(node, 0) + 1
    symbols = sorted(freq.keys(), key=lambda k: freq[k], reverse=True)
    return symbols


def collectExpression(expression):
    """
    Groups the terms of the expressions, based on the frequency of its symbols.

    Example:
    expression: m1 + r1*r2 + r1 + 1
    frequency: {m1: 1, r2: 1, r1: 2}
    result: m1 + r1*(r2 + 1) + 1

    :param expression:
    :return:
    """
    symbols = getSymbolsByDecreasingFrequency(expression)
    return sympy.collect(expression, symbols)


def formulasToExpressionTree(formulas, merge=False, simplify=False, collect=False, substitutions=None):
    """
    Transforms a Formulas object, by replacing the propositional logic propositions with sympy algebraic expressions.

    :param formulas: the Formulas object whose propositions are to be transformed
    :param merge: specifies whether to create a single expression from all the expressions of the Formulas object by
                  multiplying them (logical AND)
    :param simplify: specifies whether to simplify the expressions using the rules of the boolean ring.
                     If False is given, the result can have coefficients and powers that are not part of the ring.
    :param collect: specifies whether to collect the terms of each expression by the decreasing frequency of their
                    symbols.
    :param substitutions: a dictionary whose elements are (string_symbol, (expression, symbols)).
                          No substitution if None is given.
        string_symbol: the string which will be substituted
        expression: a sympy expression which substitutes the string
        symbols: the list of sympy symbols that are present in the expression
    :return: Formula object with the same name, but the propositions replaced with simpy expression(s)
    """
    symbols = set()

    def transform(prop):
        expr, sym = buildExpressionTree(prop, substitutions)
        symbols.update(sym)
        return expr

    expressions = map(transform, formulas.formulaList)

    if merge:
        expressions = [reduce(lambda a, b: Mul(a, b), expressions, 1)]

    if simplify:
        expressions = map(lambda e: simplifyExpression(e, symbols), expressions)

    if collect:
        expressions = map(collectExpression, expressions)

    return Formulas(formulas.name, expressions)


def createSubstitutions(predicates):
    """
    Given a list of predicates in the form of `a <-> f(b)`, returns a dictionary which associates
    to each symbol `a` the sympy expression representing `f(b)` and the used symbols.

    :param predicates: list of strings, each having the form `a <-> f(b)`, where `a` is a string propositional logic
                       symbol, and `f(b)` is the proposition which replaces `a`.
    :return: a dictionary whose elements are (string_symbol, (expression, symbols)).
        string_symbol: the string which will be substituted
        expression: a sympy expression which substitutes the string
        symbols: the list of sympy symbols that are present in the expression
    """
    substitutions = {}

    for predicate in predicates:
        terms = splitProposition(predicate)
        if len(terms) < 2 or terms[1] != '<->':
            raise ValueError('Substitutions of type `a <-> f(b)` are supported only')
        substitutions[terms[0]] = buildExpressionTree(" ".join(terms[2:]))

    return substitutions
