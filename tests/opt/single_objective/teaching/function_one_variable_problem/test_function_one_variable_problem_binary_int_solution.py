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
from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem_binary_int_solution import FunctionOneVariableMaxProblemBinaryIntSolution

from uo.target_solution.target_solution import TargetSolution

# Generated by CodiumAI

import unittest

class TestFunctionOneVariableMaxProblemBinaryIntSolution(unittest.TestCase):

    # Creating an instance of FunctionOneVariableMaxProblemBinaryIntSolution with valid arguments should initialize the object correctly
    def test_valid_arguments_initialization(self):
        if hasattr(TargetSolution, 'evaluation_cache_cs'):
            del TargetSolution.evaluation_cache_cs
        if hasattr(TargetSolution, 'representation_distance_cache_cs'):
            del TargetSolution.representation_distance_cache_cs
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)
        self.assertEqual(solution.domain_from, domain_from)
        self.assertEqual(solution.domain_to, domain_to)
        self.assertEqual(solution.number_of_intervals, number_of_intervals)
        self.assertIsNone(solution.fitness_value)
        self.assertIsNone(solution.fitness_values)
        self.assertIsNone(solution.objective_value)
        self.assertIsNone(solution.objective_values)
        self.assertFalse(solution.is_feasible)
        self.assertFalse(TargetSolution.evaluation_cache_cs.is_caching)
        self.assertEqual(TargetSolution.evaluation_cache_cs.max_cache_size, 0)
        self.assertFalse(TargetSolution.representation_distance_cache_cs.is_caching)
        self.assertEqual(TargetSolution.representation_distance_cache_cs.max_cache_size, 0)

    # Calling copy() method on an instance of FunctionOneVariableMaxProblemBinaryIntSolution should return a deep copy of the object
    def test_copy_method(self):
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10

        solution = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)
        copy_solution = solution.copy()

        self.assertIsNot(solution, copy_solution)
        self.assertEqual(solution.domain_from, copy_solution.domain_from)
        self.assertEqual(solution.domain_to, copy_solution.domain_to)
        self.assertEqual(solution.number_of_intervals, copy_solution.number_of_intervals)
        self.assertEqual(solution.representation, copy_solution.representation)

    # Calling domain_from getter on an instance of FunctionOneVariableMaxProblemBinaryIntSolution should return the correct value
    def test_domain_from_getter(self):
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10

        solution = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)

        self.assertEqual(solution.domain_from, domain_from)

    # Calling domain_to getter on an instance of FunctionOneVariableMaxProblemBinaryIntSolution should return the correct value
    def test_domain_to_getter(self):
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10

        solution = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)

        self.assertEqual(solution.domain_to, domain_to)

    # Calling number_of_intervals getter on an instance of FunctionOneVariableMaxProblemBinaryIntSolution should return the correct value
    def test_number_of_intervals_getter(self):
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10

        solution = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)

        self.assertEqual(solution.number_of_intervals, number_of_intervals)

    # Calling argument() method on an instance of FunctionOneVariableMaxProblemBinaryIntSolution should return the correct value
    def test_argument_method(self):
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10

        solution = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)
        representation = 5

        expected_argument = domain_from + representation * (domain_to - domain_from) / number_of_intervals
        actual_argument = solution.argument(representation)

        self.assertEqual(actual_argument, expected_argument)

    # Creating an instance of FunctionOneVariableMaxProblemBinaryIntSolution with domain_from equal to domain_to should raise a ValueError
    def test_domain_from_equal_to_domain_to(self):
        domain_from = 1.0
        domain_to = 1.0
        number_of_intervals = 10

        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)

    # Creating an instance of FunctionOneVariableMaxProblemBinaryIntSolution with number_of_intervals equal to 0 should raise a ValueError
    def test_number_of_intervals_equal_to_zero(self):
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 0

        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)

    # Calling obtain_feasible_representation() method on an instance of FunctionOneVariableMaxProblemBinaryIntSolution with representation greater than number_of_intervals should set representation to number_of_intervals
    def test_obtain_feasible_representation_greater_than_number_of_intervals(self):
        # Arrange
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)
        # Act
        solution.representation = 15
        rep = solution.obtain_feasible_representation(None)
        # Assert
        self.assertLessEqual(rep, number_of_intervals)

    # Calling obtain_feasible_representation() method on an instance of FunctionOneVariableMaxProblemBinaryIntSolution with representation less than 0 should set representation to 0
    def test_obtain_feasible_representation_less_than_zero(self):
        # Arrange
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10
        # Act
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)
        solution.representation = -5
        rep = solution.obtain_feasible_representation(None)
        # Assert
        self.assertGreaterEqual(rep, 0)

    # Calling native_representation() method on an instance of FunctionOneVariableMaxProblemBinaryIntSolution with a string containing non-binary characters should raise a ValueError
    def test_native_representation_non_binary_characters(self):
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10

        solution = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)
        representation_str = "12345"

        with self.assertRaises(ValueError):
            solution.native_representation(representation_str)


class Test__Init__(unittest.TestCase):

    # Initializes the object with valid input parameters.
    def test_valid_input_parameters(self):
        # Arrange
        domain_from = 0.0
        domain_to = 1.0
        number_of_intervals = 10
        # Act
        obj = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)
        # Assert
        self.assertEqual(obj.domain_from, domain_from)
        self.assertEqual(obj.domain_to, domain_to)
        self.assertEqual(obj.number_of_intervals, number_of_intervals)

    # Initializes the object with the minimum possible values for domain_from, domain_to, and number_of_intervals.
    def test_minimum_values(self):
        # Arrange
        domain_from = sys.float_info.min
        domain_to = sys.float_info.min
        number_of_intervals = 1
        # Act & Assert
        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)

    # Initializes the object with the maximum possible values for domain_from, domain_to, and number_of_intervals.
    def test_maximum_values(self):
        # Arrange
        domain_from = sys.float_info.max
        domain_to = sys.float_info.max
        number_of_intervals = sys.maxsize
        # Act & Assert
        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)

    # Initializes the object with the non-integer number_of_intervals.
    def test_non_integer_number_of_intervals(self):
        # Arrange
        domain_from = 0
        domain_to = 10
        number_of_intervals = 5.6
        # Act & Assert
        with self.assertRaises(TypeError):
            FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)



    # Initializes the object with domain_from and domain_to as integers.
    def test_integer_domain(self):
        # Arrange
        domain_from = 0
        domain_to = 10
        number_of_intervals = 5

        # Act
        obj = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)

        # Assert
        self.assertEqual(obj.domain_from, float(domain_from))
        self.assertEqual(obj.domain_to, float(domain_to))
        self.assertEqual(obj.number_of_intervals, number_of_intervals)

    # Initializes the object with domain_from and domain_to as floats.
    def test_float_domain(self):
        # Arrange
        domain_from = 0.0
        domain_to = 10.0
        number_of_intervals = 5

        # Act
        obj = FunctionOneVariableMaxProblemBinaryIntSolution(domain_from, domain_to, number_of_intervals)

        # Assert
        self.assertEqual(obj.domain_from, domain_from)
        self.assertEqual(obj.domain_to, domain_to)
        self.assertEqual(obj.number_of_intervals, number_of_intervals)


class Test__ObtainFeasibleHelper__(unittest.TestCase):

    # If the representation is within the range of [0, number_of_intervals], the representation should not be changed.
    def test_representation_within_range(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        # Act
        solution.representation = 3
        rep = solution.obtain_feasible_representation(problem)
        # Assert
        self.assertEqual(rep, 3)

    # If the representation is equal to number_of_intervals, the representation should be set to number_of_intervals.
    def test_representation_equal_to_number_of_intervals(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        # Act
        solution.representation = 5
        rep = solution.obtain_feasible_representation(problem)
        # Assert
        self.assertEqual(rep, 5)

    # If the representation is negative, the representation should be set to 0.
    def test_representation_negative(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        # Act
        solution.representation = -2
        rep = solution.obtain_feasible_representation(problem)
        # Assert
        self.assertGreaterEqual(rep, 0)

class TestInitRandom(unittest.TestCase):

    # When called, 'init_random' should set the 'representation' attribute of the 'FunctionOneVariableMaxProblemBinaryIntSolution' instance to a random integer between 0 and 'number_of_intervals'
    def test_set_representation_to_random_integer(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        # Act
        solution.init_random(problem)
        # Assert
        self.assertIsInstance(solution.representation, int)
        self.assertGreaterEqual(solution.representation, 0)
        self.assertLessEqual(solution.representation, solution.number_of_intervals)

    # If the 'representation' attribute is already set, calling 'init_random' should overwrite it with a new random integer between 0 and 'number_of_intervals'
    def test_overwrite_representation_with_random_integer(self):
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        solution.representation = 3
        solution.init_random(problem)
        self.assertIsInstance(solution.representation, int)
        self.assertGreaterEqual(solution.representation, 0)
        self.assertLessEqual(solution.representation, solution.number_of_intervals)



class TestCalculateQualityDirectly(unittest.TestCase):

    # Returns a QualityOfSolution object with the correct fitness value when given a valid representation and problem.
    def test_valid_representation_and_problem(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        representation = 3
        expected_fitness_value = (0 + 3*((10-0)/5)) ** 2

        # Act
        result = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertEqual(result.fitness_value, expected_fitness_value)

    # Returns a QualityOfSolution object with the is_feasible attribute set to True when given a valid representation and problem.
    def test_valid_representation_and_problem_is_feasible(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        representation = 3

        # Act
        result = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertTrue(result.is_feasible)

    # Returns a QualityOfSolution object with the correct objective value when given a valid representation and problem.
    def test_valid_representation_and_problem_objective_value(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        representation = 3
        expected_objective_value = 6.0

        # Act
        result = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertEqual(result.objective_value, expected_objective_value)


    # Returns a QualityOfSolution object with the correct fitness value when given the minimum valid representation and problem.
    def test_minimum_valid_representation_and_problem(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        representation = 0
        expected_fitness_value = 0.0

        # Act
        result = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertEqual(result.fitness_value, expected_fitness_value)

    # Returns a QualityOfSolution object with the correct fitness value when given the maximum valid representation and problem.
    def test_maximum_valid_representation_and_problem(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**3", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        representation = 5
        expected_fitness_value =  (0 + 5*((10-0)/5)) ** 3

        # Act
        result = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertEqual(result.fitness_value, expected_fitness_value)

class TestNativeRepresentation(unittest.TestCase):

    # Should correctly convert a binary string to an integer
    def test_correct_conversion(self):
        # Arrange
        binary_str = '101010'
        expected_result = 42
    
        # Act
        result = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 3).native_representation(binary_str)
    
        # Assert
        self.assertEqual(result, expected_result)

    # Should return 0 when given a binary string of all 0s
    def test_all_zeros(self):
        # Arrange
        binary_str = '000000'
        expected_result = 0
    
        # Act
        result = FunctionOneVariableMaxProblemBinaryIntSolution(0, 50, 10).native_representation(binary_str)
    
        # Assert
        self.assertEqual(result, expected_result)

    # Should return the maximum integer value when given a binary string of all 1s
    def test_all_ones(self):
        # Arrange
        binary_str = '111111'
        expected_result = int('111111', 2)
    
        # Act
        result = FunctionOneVariableMaxProblemBinaryIntSolution(0,20,3).native_representation(binary_str)
    
        # Assert
        self.assertEqual(result, expected_result)

    # Should raise a ValueError when given an empty string
    def test_empty_string(self):
        # Arrange
        binary_str = ''
    
        # Act & Assert
        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemBinaryIntSolution(0,20,3).native_representation(binary_str)

    # Should raise a ValueError when given a string with non-binary characters
    def test_non_binary_characters(self):
        # Arrange
        binary_str = '12345'
    
        # Act & Assert
        with self.assertRaises(ValueError):
            FunctionOneVariableMaxProblemBinaryIntSolution(0,20,3).native_representation(binary_str)

class TestRepresentationDistanceDirectly(unittest.TestCase):

    # Calculate distance between two binary representations with different lengths
    def test_distance_different_lengths(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 10)
        solution_code_1 = "101010"
        solution_code_2 = "110"
    
        # Act
        result = solution.representation_distance_directly(solution_code_1, solution_code_2)
    
        # Assert
        self.assertEqual(result, 3)

    # Calculate distance between two identical binary representations
    def test_distance_identical_representations(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 10)
        solution_code_1 = "101010"
        solution_code_2 = "101010"
    
        # Act
        result = solution.representation_distance_directly(solution_code_1, solution_code_2)
    
        # Assert
        self.assertEqual(result, 0)

    # Calculate distance between two different binary representations
    def test_distance_different_representations(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 10)
        solution_code_1 = "101010"
        solution_code_2 = "010101"
    
        # Act
        result = solution.representation_distance_directly(solution_code_1, solution_code_2)
    
        # Assert
        self.assertEqual(result, 6)

    # Calculate distance between a binary representation and a non-binary representation
    def test_distance_binary_and_non_binary_representations(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 10)
        solution_code_1 = "101010"
        solution_code_2 = "12345"
    
        # Act and Assert
        with self.assertRaises(ValueError):
            solution.representation_distance_directly(solution_code_1, solution_code_2)

    # Calculate distance between two binary representations with different lengths and values
    def test_distance_different_lengths_and_values(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 10)
        solution_code_1 = "101010"
        solution_code_2 = "11001100"
    
        # Act
        result = solution.representation_distance_directly(solution_code_1, solution_code_2)
    
        # Assert
        self.assertEqual(result, 5)


class TestStringRep(unittest.TestCase):

    # Returns a string representation of the object, including its superclass string representation and its string representation.
    def test_returns_string_representation(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        obj.representation = 3

        # Act
        result = obj.string_rep()
    
        # Assert
        self.assertIsInstance(result, str)
        self.assertIn("string_representation()=", result)

    # The string representation includes the string representation of the object's string representation.
    def test_includes_string_representation(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        obj.representation = 3

        # Act
        result = obj.string_rep()
    
        # Assert
        self.assertIn("string_representation()=", result)
        self.assertIn(obj.string_representation(), result)

    # The string representation is properly indented and formatted.
    def test_properly_indented_and_formatted(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        obj.representation = 3

        # Act
        result = obj.string_rep(indentation=2, indentation_symbol='  ')
    
        # Assert
        self.assertIn("string_representation()=", result)
        self.assertIn("  ", result)


    # The object has string representation.
    def test_no_string_representation(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        obj.representation = 3

        # Act
        result = obj.string_rep()
    
        # Assert
        self.assertIn("string_representation()=", result)

    # The delimiter, indentation, indentation_symbol, group_start, and group_end parameters are empty strings.
    def test_empty_parameters(self):
        # Arrange
        obj = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 5)
        obj.representation = 3

        # Act
        result = obj.string_rep(delimiter='', indentation=0, indentation_symbol='', group_start='', group_end='')
    
        # Assert
        self.assertNotIn('\n', result)
        self.assertNotIn('   ', result)
