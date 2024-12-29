import pytest
from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from io import StringIO
import sys


# Helper function to execute the code and capture output
def execute_expression(expression: str) -> str:
    input_stream = InputStream(expression)

    # Lexical and syntactical analysis
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)
    tree = parser.program()  # Assuming 'program' is the start rule in your grammar

    # Listener-based evaluation
    calc_evaluator = Evaluator()

    # Capture the output printed by the evaluator
    captured_output = StringIO()
    sys.stdout = captured_output  # Redirect stdout to capture print statements

    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)

    sys.stdout = sys.__stdout__  # Reset redirect.

    return captured_output.getvalue()

import pytest

def test_variable_declaration():
    # Test basic variable declaration
    expression = """
    let x = 42
    print x
    """
    output = execute_expression(expression)
    assert output == "42\n"

    # Test variable declaration with expression
    expression = """
    let y = (2 * 3)
    print y
    """
    output = execute_expression(expression)
    assert output == "6\n"

def test_while_loop_basic():
    expression = """
    let counter = 0
    while (counter < 3) {
        print counter
        let counter = (counter + 1)
    }
    """
    output = execute_expression(expression)
    assert output == "0\n1\n2\n"

def test_if_else_basic():
    expression = """
    let x = 10
    if (x > 5) {
        print "greater"
    } else {
        print "lesser"
    }
    """
    output = execute_expression(expression)
    assert output == "greater\n"

def test_if_elif_else():
    expression = """
    let x = 5
    if (x > 10) {
        print "greater than 10"
    } else if (x > 5) {
        print "greater than 5"
    } else {
        print "5 or less"
    }
    """
    output = execute_expression(expression)
    assert output == "5 or less\n"

def test_nested_control_structures():
    expression = """
    let i = 0
    while (i < 3) {
        if (i == 1) {
            print "one"
        } else {
            print i
        }
        let i = (i + 1)
    }
    """
    output = execute_expression(expression)
    assert output == "0\none\n2\n"

# def test_object_declaration():
#     expression = """
#     let obj = {"name": "test", "value": 42}
#     print obj
#     """
#     output = execute_expression(expression)
#     assert output == '{"name": "test", "value": 42}\n'

# def test_ternary_expression():
#     expression = """
#     let x = 5
#     print x > 3 ? "greater" : "lesser"
#     """
#     output = execute_expression(expression)
#     assert output == "greater\n"

# def test_empty_block():
#     expression = """
#     while (false) {
#         pass
#     }
#     """
#     output = execute_expression(expression)
#     assert output == ""