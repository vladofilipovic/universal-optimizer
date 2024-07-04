from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem import FunctionOneVariableMaxProblemMax
from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem import FunctionOneVariableMaxProblemMaxElements

class TestFunctionOneVariableMaxProblem(unittest.TestCase):

    # Creating a new instance of FunctionOneVariableMaxProblemMax with valid expression, domain_low and domain_high parameters should return a FunctionOneVariableMaxProblemMax object.
    def test_valid_instance_creation(self):
        problem = FunctionOneVariableMaxProblemMax("x^2", 0, 10)
        self.assertIsInstance(problem, FunctionOneVariableMaxProblemMax)


    # Initializes a FunctionOneVariableMaxProblemMax object with a valid expression and domain_low equal to domain_high.
    def test_valid_expression_domain_low_equal_domain_high(self):
        expression = "x**2 + 2*x + 1"
        domain_low = 5.0
        domain_high = 5.0
        problem = FunctionOneVariableMaxProblemMax(expression, domain_low, domain_high)
        self.assertEqual(problem.expression, expression)
        self.assertEqual(problem.domain_low, domain_low)
        self.assertEqual(problem.domain_high, domain_high)

    # Initializes a FunctionOneVariableMaxProblemMax object with a valid expression, domain_low, and domain_high.
    def test_valid_expression_domain_low_domain_high(self):
        expression = "x**2 + 2*x + 1"
        domain_low = -10.0
        domain_high = 10.0
        problem = FunctionOneVariableMaxProblemMax(expression, domain_low, domain_high)
        self.assertEqual(problem.expression, expression)
        self.assertEqual(problem.domain_low, domain_low)
        self.assertEqual(problem.domain_high, domain_high)

    # Initializes a FunctionOneVariableMaxProblemMax object with the minimum valid values for expression, domain_low, and domain_high.
    def test_minimum_values(self):
        expression = "x"
        domain_low = float('-inf')
        domain_high = float('inf')
        problem = FunctionOneVariableMaxProblemMax(expression, domain_low, domain_high)
        self.assertEqual(problem.expression, expression)
        self.assertEqual(problem.domain_low, domain_low)
        self.assertEqual(problem.domain_high, domain_high)
    # Creating a new instance of FunctionOneVariableMaxProblemMax with invalid expression parameter should raise a ValueError.
    def test_invalid_expression_parameter(self):
        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemMax("", 0, 10)

    # Raises a ValueError if expression is None.
    def test_expression_is_none(self):
        expression = None
        domain_low = -10.0
        domain_high = 10.0
        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemMax(expression, domain_low, domain_high)

    # Raises a ValueError if expression is an empty string.
    def test_expression_is_empty_string(self):
        expression = ""
        domain_low = -10.0
        domain_high = 10.0
        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemMax(expression, domain_low, domain_high)

    # Creating a new instance of FunctionOneVariableMaxProblemMax with invalid domain_low parameter should raise a ValueError.
    def test_invalid_domain_low_parameter(self):
        with self.assertRaises(TypeError):
            FunctionOneVariableMaxProblemMax("x^2", "a", 10)

    # Creating a new instance of FunctionOneVariableMaxProblemMax with invalid domain_high parameter should raise a ValueError.
    def test_invalid_domain_high_parameter(self):
        with self.assertRaises(TypeError):
            FunctionOneVariableMaxProblemMax("x^2", 0, "b")


class Test__LoadFromFile__(unittest.TestCase):

    # Loads a valid txt file with three data elements and returns a FunctionOneVariableMaxProblemMaxElements object
    def test_valid_txt_file(self):
        # Mock the open function to return a file object
        with patch('builtins.open', mock_open(read_data='expression 1.0 2.0')) as mock_file:
            # Call the method under test
            result = FunctionOneVariableMaxProblemMax.__load_from_file__('file.txt', 'txt')

        mock_file.assert_called_with('file.txt', 'r')
        # Assert that the result is an instance of FunctionOneVariableMaxProblemMaxElements
        self.assertIsInstance(result, FunctionOneVariableMaxProblemMaxElements)
        # Assert that the expression, domain_low, and domain_high values are correct
        self.assertEqual(result.expression, 'expression')
        self.assertEqual(result.domain_low, 1.0)
        self.assertEqual(result.domain_high, 2.0)

    # Skips comments at the beginning of the file
    def test_skip_comments(self):
        # Mock the open function to return a file object with comments at the beginning
        with patch('builtins.open', mock_open(read_data='// Comment\nexpression 1.0 2.0')):
            # Call the method under test
            result = FunctionOneVariableMaxProblemMax.__load_from_file__('input.txt', 'txt')

        # Assert that the result is an instance of FunctionOneVariableMaxProblemMaxElements
        self.assertIsInstance(result, FunctionOneVariableMaxProblemMaxElements)
        # Assert that the expression, domain_low, and domain_high are correct
        self.assertEqual(result.expression, 'expression')
        self.assertEqual(result.domain_low, 1.0)
        self.assertEqual(result.domain_high, 2.0)

    # Raises FileNotFoundError when input file path is invalid
    def test_invalid_file_path(self):
        # Call the method under test with an invalid file path
        with self.assertRaises(FileNotFoundError):
            FunctionOneVariableMaxProblemMax.__load_from_file__('invalid.txt', 'txt')

    # Raises ValueError when data format is not supported
    def test_invalid_data_format(self):
        # Call the method under test with an invalid data format
        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemMax.__load_from_file__('input.txt', 'csv')

    # Raises ValueError when input file has no data
    def test_empty_file(self):
        # Mock the open function to return an empty file
        with patch('builtins.open', mock_open(read_data='')):    
            # Call the method under test
            with self.assertRaises(ValueError):
                FunctionOneVariableMaxProblemMax.__load_from_file__('empty.txt', 'txt')


    # Can load problem data from a txt file with valid format
    def test_load_from_valid_txt_file(self):
        # Arrange
        input_file_path = "valid_input.txt"
        input_format = "txt"
        expected_expression = "x^2+2*x+1"
        expected_domain_low = -10.0
        expected_domain_high = 10.0
    
        with patch('builtins.open', mock_open(read_data="x^2+2*x+1 -10.0 10.0")): 
            # Act
            result = FunctionOneVariableMaxProblemMax.from_input_file(input_file_path, input_format)
        
            # Assert
            self.assertEqual(result.expression, expected_expression)
            self.assertEqual(result.domain_low, expected_domain_low)
            self.assertEqual(result.domain_high, expected_domain_high)

class Test__FromInputFile__(unittest.TestCase):

    # Can handle comments in the input file
    def test_handle_comments_in_input_file(self):
        # Arrange
        input_file_path = "valid_input.txt"
        input_format = "txt"
        expected_expression = "x^2+2*x+1"
        expected_domain_low = -10.0
        expected_domain_high = 10.0
    
        with patch("builtins.open", mock_open(read_data="// This is a comment\nx^2+2*x+1 -10.0 10.0")):
            # Act
            result = FunctionOneVariableMaxProblemMax.from_input_file(input_file_path, input_format)
        
            # Assert
            self.assertEqual(result.expression, expected_expression)
            self.assertEqual(result.domain_low, expected_domain_low)
            self.assertEqual(result.domain_high, expected_domain_high)

    # Raises FileNotFoundError when input file path is invalid
    def test_invalid_input_file_path(self):
        # Arrange
        input_file_path = "invalid_input.txt"
        input_format = "txt"
    
        # Act & Assert
        with self.assertRaises(FileNotFoundError):
            FunctionOneVariableMaxProblemMax.from_input_file(input_file_path, input_format)

    # Raises ValueError when input format is not supported
    def test_invalid_input_format(self):
        # Arrange
        input_file_path = "valid_input.txt"
        input_format = "nsup"
    
        # Act & Assert
        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemMax.from_input_file(input_file_path, input_format)

    # Raises ValueError when input file is empty
    def test_empty_input_file(self):
        # Arrange
        input_file_path = "valid_input.txt"
        input_format = "txt"
    
        with patch("builtins.open", mock_open(read_data="")):    
            # Act & Assert
            with self.assertRaises(ValueError):
                FunctionOneVariableMaxProblemMax.from_input_file(input_file_path, input_format)

class TestStringRep(unittest.TestCase):

    # Returns a string representation of the object with the specified delimiter, indentation, and grouping symbols.
    def test_returns_string_representation_with_specified_parameters(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemMax("expression", 0, 1)
        delimiter = "|"
        indentation = 2
        indentation_symbol = "-"
        group_start = "["
        group_end = "]"
        expected_result = "|--[|--|--name=FunctionOneVariableMaxProblemMax|--is_minimization=False--|--expression=expression|--domain_low=0|--domain_high=1]"

        # Act
        result = obj.string_rep(delimiter, indentation, indentation_symbol, group_start, group_end)

        # Assert
        self.assertEqual(result, expected_result)


    # The string representation is properly indented and grouped according to the specified parameters.
    def test_properly_indents_and_groups_string_representation(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemMax("expression", 0, 1)
        delimiter = "|"
        indentation = 2
        indentation_symbol = "-"
        group_start = "["
        group_end = "]"
        expected_result = "|--[|--|--name=FunctionOneVariableMaxProblemMax|--is_minimization=False--|--expression=expression|--domain_low=0|--domain_high=1]"

        # Act
        result = obj.string_rep(delimiter, indentation, indentation_symbol, group_start, group_end)

        # Assert
        self.assertEqual(result, expected_result)

    # If the delimiter parameter is None, an empty string is returned.
    def test_returns_empty_string_if_delimiter_is_none(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemMax("expression", 0, 1)
        delimiter = None
        indentation = 2
        indentation_symbol = "-"
        group_start = "["
        group_end = "]"
        expected_result = ""

        # Act
        result = obj.string_rep(delimiter, indentation, indentation_symbol, group_start, group_end)

        # Assert
        self.assertEqual(result, expected_result)

    # If the indentation parameter is negative, an empty string is returned.
    def test_returns_empty_string_if_indentation_is_negative(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemMax("expression", 0, 1)
        delimiter = "|"
        indentation = -2
        indentation_symbol = "-"
        group_start = "["
        group_end = "]"
        expected_result = ""

        # Act
        result = obj.string_rep(delimiter, indentation, indentation_symbol, group_start, group_end)

        # Assert
        self.assertEqual(result, expected_result)

    # If the indentation_symbol parameter is None, an empty string is returned.
    def test_returns_empty_string_if_indentation_symbol_is_none(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemMax("expression", 0, 1)
        delimiter = "|"
        indentation = 2
        indentation_symbol = None
        group_start = "["
        group_end = "]"
        expected_result = ""

        # Act
        result = obj.string_rep(delimiter, indentation, indentation_symbol, group_start, group_end)

        # Assert
        self.assertEqual(result, expected_result)

    # The __str__ method should return a string representation of the FunctionOneVariableMaxProblemMax object.
    def test_str_representation(self):
        problem = FunctionOneVariableMaxProblemMax("x^2", 0, 10)
        expected = "|{||name=FunctionOneVariableMaxProblemMax|is_minimization=False|expression=x^2|domain_low=0|domain_high=10}"
        self.assertEqual(str(problem), expected)

    # The __repr__ method should return a string representation of the FunctionOneVariableMaxProblemMax object.
    def test_repr_representation(self):
        problem = FunctionOneVariableMaxProblemMax("x^2", 0, 10)
        expected = "\n{\n\nname=FunctionOneVariableMaxProblemMax\nis_minimization=False\nexpression=x^2\ndomain_low=0\ndomain_high=10}"
        self.assertEqual(repr(problem), expected)


class Test__Copy__(unittest.TestCase):

    # The method should return a new instance of the 'FunctionOneVariableMaxProblemMax' class.
    def test_return_new_instance(self):
        problem = FunctionOneVariableMaxProblemMax("x^2", 0, 10)
        new_problem = problem.__copy__()
        self.assertIsInstance(new_problem, FunctionOneVariableMaxProblemMax)

    # The new instance should be a deep copy of the original instance.
    def test_deep_copy(self):
        problem = FunctionOneVariableMaxProblemMax("x^2", 0, 10)
        new_problem = problem.__copy__()
        self.assertIsNot(problem, new_problem)

    # The new instance should have the same values for all attributes as the original instance.
    def test_same_attribute_values(self):
        problem = FunctionOneVariableMaxProblemMax("x^2", 0, 10)
        new_problem = problem.__copy__()
        self.assertEqual(problem.expression, new_problem.expression)
        self.assertEqual(problem.domain_low, new_problem.domain_low)
        self.assertEqual(problem.domain_high, new_problem.domain_high)

    # The original instance should be an instance of a subclass of 'FunctionOneVariableMaxProblemMax'. The method should return an instance of the same subclass.
    def test_subclass_instance(self):
        class SubclassProblem(FunctionOneVariableMaxProblemMax):
            pass
        problem = SubclassProblem("x^2", 0, 10)
        new_problem = problem.__copy__()
        self.assertIsInstance(problem, SubclassProblem)
        self.assertIsInstance(new_problem, SubclassProblem)


class TestExpression(unittest.TestCase):

    # Returns the expression string when called.
    def test_returns_expression_string(self):
        problem = FunctionOneVariableMaxProblemMax("x^2", 0, 10)
        self.assertEqual(problem.expression, "x^2")

    # Returns a non-empty string.
    def test_returns_non_empty_string(self):
        problem = FunctionOneVariableMaxProblemMax("x^2", 0, 10)
        self.assertTrue(problem.expression)

    # Returns a string with valid characters.
    def test_returns_string_with_valid_characters(self):
        problem = FunctionOneVariableMaxProblemMax("x^2", 0, 10)
        valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789^"
        for char in problem.expression:
            self.assertIn(char, valid_characters)

    # Raises a ValueError when expression is None.
    def test_raises_value_error_when_expression_is_none(self):
        with self.assertRaises(ValueError):
            problem = FunctionOneVariableMaxProblemMax(None, 0, 10)

    # Raises a ValueError when domain_low is not a number.
    def test_raises_value_error_when_domain_low_is_not_a_number(self):
        with self.assertRaises(TypeError):
            problem = FunctionOneVariableMaxProblemMax("x^2", "a", 10)