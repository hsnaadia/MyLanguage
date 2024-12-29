import pytest
from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from io import StringIO
import sys
from antlr4.tree.Tree import ParseTreeWalker


# Helper function to execute an expression and capture output
def execute_expression(expression: str) -> str:
  input_stream = InputStream(expression)
  lexer = MyLangLexer(input_stream)
  token_stream = CommonTokenStream(lexer)
  parser = MyLangParser(token_stream)
  tree = parser.program()


  evaluator = Evaluator()
  # Capture the output printed by the evaluator
  captured_output = StringIO()
  sys.stdout = captured_output  # Redirect stdout to capture print statements
  walker = ParseTreeWalker()
  walker.walk(evaluator, tree)


  sys.stdout = sys.__stdout__  # Reset stdout to normal
  return captured_output.getvalue().strip()


# Test case for do-while loop
def test_do_while():
  expression = """
let x = 0
do {
  print x
  let x = (x + 1)
} while (x < 5)
"""
  expected_output = """0\n1\n2\n3\n4\n5"""


  output = execute_expression(expression)
  assert output == expected_output, f"Output: {output}, Expected: {expected_output}"


# Test case for unless statement
def test_unless():
  expression = """
let x = 10
unless (x > 20) {
  print "x is not greater than 20"
  let x = (x + 5)
  print x
}
"""
  expected_output = """x is not greater than 20\n15\nx is not greater than 20\n20"""
  output = execute_expression(expression)
  assert output == expected_output, f"Output: {output}, Expected: {expected_output}"


if __name__ == "__main__":
  pytest.main()
