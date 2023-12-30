from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem import FunctionOneVariableProblem
from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem import FunctionOneVariableProblemElements

class TestFunctionOneVariableProblem(unittest.TestCase):

    # Creating a new instance of FunctionOneVariableProblem with valid expression, domain_low and domain_high parameters should return a FunctionOneVariableProblem object.
    def test_valid_instance_creation(self):
        problem = FunctionOneVariableProblem("x^2", 0, 10)
        self.assertIsInstance(problem, FunctionOneVariableProblem)

    # The __str__ method should return a string representation of the FunctionOneVariableProblem object.
    def test_str_representation(self):
        problem = FunctionOneVariableProblem("x^2", 0, 10)
        expected = "|{||name=FunctionOneVariableProblem|is_minimization=False|expression=x^2|domain_low=0|domain_high=10}"
        self.assertEqual(str(problem), expected)

    # The __repr__ method should return a string representation of the FunctionOneVariableProblem object.
    def test_repr_representation(self):
        problem = FunctionOneVariableProblem("x^2", 0, 10)
        expected = "\n{\n\nname=FunctionOneVariableProblem\nis_minimization=False\nexpression=x^2\ndomain_low=0\ndomain_high=10}"
        self.assertEqual(repr(problem), expected)


    # Initializes a FunctionOneVariableProblem object with a valid expression and domain_low equal to domain_high.
    def test_valid_expression_domain_low_equal_domain_high(self):
        expression = "x**2 + 2*x + 1"
        domain_low = 5.0
        domain_high = 5.0
        problem = FunctionOneVariableProblem(expression, domain_low, domain_high)
        self.assertEqual(problem.expression, expression)
        self.assertEqual(problem.domain_low, domain_low)
        self.assertEqual(problem.domain_high, domain_high)

    # Initializes a FunctionOneVariableProblem object with a valid expression, domain_low, and domain_high.
    def test_valid_expression_domain_low_domain_high(self):
        expression = "x**2 + 2*x + 1"
        domain_low = -10.0
        domain_high = 10.0
        problem = FunctionOneVariableProblem(expression, domain_low, domain_high)
        self.assertEqual(problem.expression, expression)
        self.assertEqual(problem.domain_low, domain_low)
        self.assertEqual(problem.domain_high, domain_high)

    # Initializes a FunctionOneVariableProblem object with the minimum valid values for expression, domain_low, and domain_high.
    def test_minimum_values(self):
        expression = "x"
        domain_low = float('-inf')
        domain_high = float('inf')
        problem = FunctionOneVariableProblem(expression, domain_low, domain_high)
        self.assertEqual(problem.expression, expression)
        self.assertEqual(problem.domain_low, domain_low)
        self.assertEqual(problem.domain_high, domain_high)
    # Creating a new instance of FunctionOneVariableProblem with invalid expression parameter should raise a ValueError.
    def test_invalid_expression_parameter(self):
        with self.assertRaises(ValueError):
            FunctionOneVariableProblem("", 0, 10)

    # Raises a ValueError if expression is None.
    def test_expression_is_none(self):
        expression = None
        domain_low = -10.0
        domain_high = 10.0
        with self.assertRaises(ValueError):
            FunctionOneVariableProblem(expression, domain_low, domain_high)

    # Raises a ValueError if expression is an empty string.
    def test_expression_is_empty_string(self):
        expression = ""
        domain_low = -10.0
        domain_high = 10.0
        with self.assertRaises(ValueError):
            FunctionOneVariableProblem(expression, domain_low, domain_high)

    # Creating a new instance of FunctionOneVariableProblem with invalid domain_low parameter should raise a ValueError.
    def test_invalid_domain_low_parameter(self):
        with self.assertRaises(ValueError):
            FunctionOneVariableProblem("x^2", "a", 10)

    # Creating a new instance of FunctionOneVariableProblem with invalid domain_high parameter should raise a ValueError.
    def test_invalid_domain_high_parameter(self):
        with self.assertRaises(ValueError):
            FunctionOneVariableProblem("x^2", 0, "b")


class Test__LoadFromFile__(unittest.TestCase):

    # Loads a valid txt file with three data elements and returns a FunctionOneVariableProblemElements object
    def test_valid_txt_file(self):
        # Mock the open function to return a file object
        with patch('builtins.open', mock_open(read_data='expression 1.0 2.0')) as mock_file:
            # Call the method under test
            result = FunctionOneVariableProblem.__load_from_file__('file.txt', 'txt')

        mock_file.assert_called_with('file.txt', 'r')
        # Assert that the result is an instance of FunctionOneVariableProblemElements
        self.assertIsInstance(result, FunctionOneVariableProblemElements)
        # Assert that the expression, domain_low, and domain_high values are correct
        self.assertEqual(result.expression, 'expression')
        self.assertEqual(result.domain_low, 1.0)
        self.assertEqual(result.domain_high, 2.0)

