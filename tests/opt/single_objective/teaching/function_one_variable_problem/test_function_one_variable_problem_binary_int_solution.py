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
import unittest.mock as mock

from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem_binary_int_solution \
    import FunctionOneVariableProblemBinaryIntSolution

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
        #self.assertFalse(solution.evaluation_cache_is_used)
        #self.assertEqual(solution.evaluation_cache_max_size, 0)
        #self.assertFalse(solution.distance_calculation_cache_is_used)
        #self.assertEqual(solution.distance_calculation_cache_max_size, 0)

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
