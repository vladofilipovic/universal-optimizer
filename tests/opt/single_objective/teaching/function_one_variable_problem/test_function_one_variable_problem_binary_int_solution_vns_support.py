from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem import FunctionOneVariableProblem
from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem_binary_int_solution import FunctionOneVariableProblemBinaryIntSolution
from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem_binary_int_solution_vns_support import FunctionOneVariableProblemBinaryIntSolutionVnsSupport


# import unittest
# import unitest.mock as mocker

class TestFunctionOneVariableProblemBinaryIntSolutionVnsSupport(unittest.TestCase):

    # shaking method returns True when k is greater than 0 and the solution is valid
    def test_shaking_returns_true_when_k_is_greater_than_0_and_solution_is_valid(self):
        # Arrange
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).check_evaluations = mocker.PropertyMock(return_value=False)
        type(finish_control_stub).evaluations_max = mocker.PropertyMock(return_value=0)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)

        # Act
        result = vns_support.shaking(1, problem, solution, optimizer_stub)

        # Assert
        self.assertTrue(result)

    # local_search_best_improvement method returns a new solution with a better fitness value
    def test_local_search_best_improvement_returns_new_solution_with_better_fitness_value(self):
        # Arrange
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).check_evaluations = mocker.PropertyMock(return_value=False)
        type(finish_control_stub).evaluations_max = mocker.PropertyMock(return_value=0)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)

        # Act
        new_solution = vns_support.local_search_best_improvement(1, problem, solution, optimizer_stub)

        # Assert
        self.assertGreaterEqual(new_solution.fitness_value, solution.fitness_value)

    # local_search_first_improvement method returns a new solution with a better fitness value
    def test_local_search_first_improvement_returns_new_solution_with_better_fitness_value(self):
        # Arrange
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).check_evaluations = mocker.PropertyMock(return_value=False)
        type(finish_control_stub).evaluations_max = mocker.PropertyMock(return_value=0)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)

        # Act
        new_solution = vns_support.local_search_first_improvement(1, problem, solution, optimizer_stub)

        # Assert
        self.assertGreaterEqual(new_solution.fitness_value, solution.fitness_value)

    # shaking method returns False when k is less than or equal to 0
    def test_shaking_returns_false_when_k_is_less_than_or_equal_to_0(self):
        # Arrange
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).check_evaluations = mocker.PropertyMock(return_value=False)
        type(finish_control_stub).evaluations_max = mocker.PropertyMock(return_value=0)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)

        # Act
        result = vns_support.shaking(0, problem, solution, optimizer_stub)

        # Assert
        self.assertFalse(result)

    # local_search_best_improvement method returns the same solution when k is less than 1 or greater than the representation length
    def test_local_search_best_improvement_returns_same_solution_when_k_is_less_than_1_or_greater_than_representation_length(self):
        # Arrange
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).check_evaluations = mocker.PropertyMock(return_value=False)
        type(finish_control_stub).evaluations_max = mocker.PropertyMock(return_value=0)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)

        # Act
        new_solution = vns_support.local_search_best_improvement(0, problem, solution, optimizer_stub)

        # Assert
        self.assertEqual(new_solution, solution)

        # Act
        new_solution = vns_support.local_search_best_improvement(33, problem, solution, optimizer_stub)

        # Assert
        self.assertEqual(new_solution, solution)

    # local_search_first_improvement method returns the same solution when k is less than 1 or greater than the representation length
    def test_local_search_first_improvement_returns_same_solution_when_k_is_less_than_1_or_greater_than_representation_length(self):
        # Arrange
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).check_evaluations = mocker.PropertyMock(return_value=False)
        type(finish_control_stub).evaluations_max = mocker.PropertyMock(return_value=0)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)

        # Act
        new_solution = vns_support.local_search_first_improvement(0, problem, solution, optimizer_stub)

        # Assert
        self.assertEqual(new_solution, solution)

        # Act
        new_solution = vns_support.local_search_first_improvement(33, problem, solution, optimizer_stub)

        # Assert
        self.assertEqual(new_solution, solution)

    # should return a string representation of the class name 'FunctionOneVariableProblemBinaryIntSolutionVnsSupport'
    def test_string_rep_class_name(self):
        # Arrange
        solution = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('|')
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableProblemBinaryIntSolutionVnsSupport')


    # should return a string with the delimiter passed as argument
    def test_string_rep_delimiter(self):
        # Arrange
        solution = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('|')
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableProblemBinaryIntSolutionVnsSupport')

    # should return a string with the indentation passed as argument
    def test_string_rep_indentation(self):
        # Arrange
        solution = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('|', indentation=4)
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableProblemBinaryIntSolutionVnsSupport')

    # should return an empty string when all arguments are empty
    def test_string_rep_empty_arguments(self):
        # Arrange
        solution = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('', indentation=0, indentation_symbol='', group_start='', group_end='')
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableProblemBinaryIntSolutionVnsSupport')

    # should return a string with the indentation_symbol passed as argument
    def test_string_rep_indentation_symbol(self):
        # Arrange
        solution = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('|', indentation_symbol=' ')
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableProblemBinaryIntSolutionVnsSupport')