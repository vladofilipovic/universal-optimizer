from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent.parent.parent)

import unittest
import unittest.mock as mocker

from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem_binary_int_solution \
    import FunctionOneVariableProblemBinaryIntSolution
from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem \
    import FunctionOneVariableProblem

from uo.target_solution.target_solution import QualityOfSolution
from uo.target_solution.target_solution import TargetSolution



class TestFunctionOneVariableProblemBinaryIntSolution(unittest.TestCase):

    # Creating an instance of FunctionOneVariableProblemBinaryIntSolution with valid inputs should initialize all attributes correctly
    def test_valid_inputs_initialization(self):
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        self.assertEqual(solution.domain_from, 0)
        self.assertEqual(solution.domain_to, 10)
        self.assertEqual(solution.number_of_intervals, 5)
        self.assertIsNone(solution.fitness_value)
        self.assertIsNone(solution.fitness_values)
        self.assertIsNone(solution.objective_value)
        self.assertIsNone(solution.objective_values)
        self.assertFalse(solution.is_feasible)
        self.assertFalse(TargetSolution.evaluation_cache_cs.is_caching)
        self.assertEqual(TargetSolution.evaluation_cache_cs.max_cache_size, 0)
        self.assertFalse(TargetSolution.representation_distance_cache_cs.is_caching)
        self.assertEqual(TargetSolution.representation_distance_cache_cs.max_cache_size, 0)

    # Calling copy() method on an instance of FunctionOneVariableProblemBinaryIntSolution should return a deep copy of the instance
    def test_copy_method(self):
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        solution_copy = solution.copy()
        self.assertIsNot(solution, solution_copy)
        self.assertEqual(solution.domain_from, solution_copy.domain_from)
        self.assertEqual(solution.domain_to, solution_copy.domain_to)
        self.assertEqual(solution.number_of_intervals, solution_copy.number_of_intervals)
        self.assertEqual(solution.representation, solution_copy.representation)

    # Calling argument() method on an instance of FunctionOneVariableProblemBinaryIntSolution with a valid representation should return the corresponding argument
    def test_argument_method(self):
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        solution.representation = 3
        argument = solution.argument(solution.representation)
        self.assertEqual(argument, 6)

    # Creating an instance of FunctionOneVariableProblemBinaryIntSolution with domain_from greater than domain_to should raise an exception
    def test_invalid_domain_from(self):
        with self.assertRaises(Exception):
            FunctionOneVariableProblemBinaryIntSolution(10, 0, 5)

    # Creating an instance of FunctionOneVariableProblemBinaryIntSolution with number_of_intervals less than or equal to 0 should raise an exception
    def test_invalid_number_of_intervals(self):
        with self.assertRaises(Exception):
            FunctionOneVariableProblemBinaryIntSolution(0, 10, -5)

    # When the representation is smaller than or equal to the number of intervals, the representation should not change.
    def test_representation_smaller_or_equal_to_intervals(self):
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        solution.representation = 3
        solution.__make_to_be_feasible_helper__(problem)
        self.assertEqual(solution.representation, 3)

    # When the representation is equal to the number of intervals, the representation should be set to the number of intervals.
    def test_representation_equal_to_intervals(self):
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        solution.representation = 5
        solution.__make_to_be_feasible_helper__(problem)
        self.assertEqual(solution.representation, 5)

    # When the representation is greater than the number of intervals, the representation should be set to the number of intervals.
    def test_representation_greater_than_intervals(self):
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        solution.representation = 7
        solution.__make_to_be_feasible_helper__(problem)
        self.assertEqual(solution.representation, 5)

    # When the representation is negative, the representation should be set to zero.
    def test_negative_representation(self):
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        solution.representation = -2
        solution.__make_to_be_feasible_helper__(problem)
        self.assertEqual(solution.representation, 0)   
    
    def test_valid_fitness_value(self):
        # Create a mock problem
        problem = mocker.Mock(spec=FunctionOneVariableProblem)
        problem.expression = "x**2"
    
        # Create an instance of FunctionOneVariableProblemBinaryIntSolution
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
    
        # Call the calculate_quality_directly method with a valid representation
        result = solution.calculate_quality_directly(3, problem)
    
        # Assert that the result is a QualityOfSolution object
        self.assertIsInstance(result, QualityOfSolution)
    
        # Assert that the fitness value is not None
        self.assertIsNotNone(result.fitness_value)

    def test_valid_is_feasible_true(self):
        # Create a mock problem
        problem = mocker.Mock(spec=FunctionOneVariableProblem)
        problem.expression = "x**2"
    
        # Create an instance of FunctionOneVariableProblemBinaryIntSolution
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
    
        # Call the calculate_quality_directly method with a valid representation
        result = solution.calculate_quality_directly(3, problem)
    
        # Assert that the result is a QualityOfSolution object
        self.assertIsInstance(result, QualityOfSolution)
    
        # Assert that is_feasible is True
        self.assertTrue(result.is_feasible)

    # Returns a QualityOfSolution object with objective_value equal to fitness_value when given a valid representation and problem.
    def test_valid_objective_value_equals_fitness_value(self):
        # Create a mock problem
        problem = mocker.Mock(spec=FunctionOneVariableProblem)
        problem.expression = "x**2"
    
        # Create an instance of FunctionOneVariableProblemBinaryIntSolution
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
    
        # Call the calculate_quality_directly method with a valid representation
        result = solution.calculate_quality_directly(3, problem)
    
        # Assert that the result is a QualityOfSolution object
        self.assertIsInstance(result, QualityOfSolution)
    
        # Assert that objective_value is equal to fitness_value
        self.assertEqual(result.objective_value, result.fitness_value)

    def test_invalid_problem_expression(self):
        # Create a mock problem with an invalid expression
        problem = mocker.Mock(spec=FunctionOneVariableProblem)
        problem.expression = "x**2 +"
    
        # Create an instance of FunctionOneVariableProblemBinaryIntSolution
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
    
        # Assert that a SyntaxError is raised when calling the calculate_quality_directly method
        with self.assertRaises(SyntaxError):
            solution.calculate_quality_directly(3, problem)

    # The input string is a valid binary representation, and the method returns the corresponding integer value.
    def test_valid_binary_representation(self):
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        result = solution.native_representation('101')
        self.assertEqual(result, 5)

    # The input string is '0', and the method returns 0.
    def test_zero_representation(self):
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        result = solution.native_representation('0')
        self.assertEqual(result, 0)

    # The input string is '1', and the method returns 1.
    def test_one_representation(self):
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        result = solution.native_representation('1')
        self.assertEqual(result, 1)

    # The input string is an empty string, and the method raises a ValueError with an appropriate error message.
    def test_empty_string_representation(self):
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        with self.assertRaises(ValueError) as context:
            solution.native_representation('')
        self.assertEqual(str(context.exception), "invalid literal for int() with base 2: ''")

    # The input string contains a non-binary character, and the method raises a ValueError with an appropriate error message.
    def test_non_binary_character_representation(self):
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 5)
        with self.assertRaises(ValueError) as context:
            solution.native_representation('01a01')
        self.assertEqual(str(context.exception), "invalid literal for int() with base 2: '01a01'")