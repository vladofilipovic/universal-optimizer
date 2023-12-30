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
# from opt.single_objective.teaching.function_one_variable_problem.test_function_one_variable_problem_binary_int_solution_vns_support import FunctionOneVariableProblemBinaryIntSolutionVnsSupport


# import unittest
# import unitest.mock as mocker

# class TestFunctionOneVariableProblemBinaryIntSolutionVnsSupport(unittest.TestCase):

#     # shaking method returns True when k is greater than 0 and the solution is valid
#     def test_shaking_returns_true_when_k_is_greater_than_0_and_solution_is_valid(self):
#         # Arrange
#         problem = FunctionOneVariableProblem("x**2", 0, 10)
#         solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 4)
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
#         finish_control_stub = mocker.MagicMock()
#         type(finish_control_stub).check_evaluations = mocker.PropertyMock(return_value=False)
#         type(finish_control_stub).evaluations_max = mocker.PropertyMock(return_value=0)
#         optimizer_stub = mocker.MagicMock()
#         type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
#         type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
#         type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)
#         #optimizer_stub.evaluate = mocker.Mock(return_value='evaluate')

#         # Act
#         result = vns_support.shaking(1, problem, solution, optimizer_stub)

#         # Assert
#         self.assertTrue(result)

#     # local_search_best_improvement method returns a new solution with a better fitness value
#     def test_local_search_best_improvement_returns_new_solution_with_better_fitness_value(self):
#         # Arrange
#         problem = FunctionOneVariableProblem()
#         solution = FunctionOneVariableProblemBinaryIntSolution()
#         optimizer = Algorithm()
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()

#         # Act
#         new_solution = vns_support.local_search_best_improvement(1, problem, solution, optimizer)

#         # Assert
#         self.assertGreater(new_solution.fitness_value, solution.fitness_value)

#     # local_search_first_improvement method returns a new solution with a better fitness value
#     def test_local_search_first_improvement_returns_new_solution_with_better_fitness_value(self):
#         # Arrange
#         problem = FunctionOneVariableProblem()
#         solution = FunctionOneVariableProblemBinaryIntSolution()
#         optimizer = Algorithm()
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()

#         # Act
#         new_solution = vns_support.local_search_first_improvement(1, problem, solution, optimizer)

#         # Assert
#         self.assertGreater(new_solution.fitness_value, solution.fitness_value)

#     # copy method returns a deep copy of the object
#     def test_copy_returns_deep_copy_of_object(self):
#         # Arrange
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()

#         # Act
#         copy_vns_support = vns_support.copy()

#         # Assert
#         self.assertIsNot(vns_support, copy_vns_support)
#         self.assertEqual(vns_support.__dict__, copy_vns_support.__dict__)

#     # string_rep method returns a string representation of the object
#     def test_string_rep_returns_string_representation_of_object(self):
#         # Arrange
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()

#         # Act
#         result = vns_support.string_rep('|')

#         # Assert
#         self.assertEqual(result, 'FunctionOneVariableProblemBinaryIntSolutionVnsSupport')

#     # shaking method returns False when k is less than or equal to 0
#     def test_shaking_returns_false_when_k_is_less_than_or_equal_to_0(self):
#         # Arrange
#         problem = FunctionOneVariableProblem()
#         solution = FunctionOneVariableProblemBinaryIntSolution()
#         optimizer = Algorithm()
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()

#         # Act
#         result = vns_support.shaking(0, problem, solution, optimizer)

#         # Assert
#         self.assertFalse(result)

#     # shaking method returns False when the solution is not valid after shaking
#     def test_shaking_returns_false_when_solution_is_not_valid_after_shaking(self):
#         # Arrange
#         problem = FunctionOneVariableProblem()
#         solution = FunctionOneVariableProblemBinaryIntSolution()
#         solution.representation = 0xFFFFFFFF  # Set representation to all 1s
#         optimizer = Algorithm()
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()

#         # Act
#         result = vns_support.shaking(1, problem, solution, optimizer)

#         # Assert
#         self.assertFalse(result)

#     # shaking method returns False when the maximum number of tries is reached
#     def test_shaking_returns_false_when_maximum_number_of_tries_is_reached(self):
#         # Arrange
#         problem = FunctionOneVariableProblem()
#         solution = FunctionOneVariableProblemBinaryIntSolution()
#         solution.representation = 0xFFFFFFFF  # Set representation to all 1s
#         optimizer = Algorithm()
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()

#         # Act
#         result = vns_support.shaking(1, problem, solution, optimizer)

#         # Assert
#         self.assertFalse(result)

#     # local_search_best_improvement method returns the same solution when k is less than 1 or greater than the representation length
#     def test_local_search_best_improvement_returns_same_solution_when_k_is_less_than_1_or_greater_than_representation_length(self):
#         # Arrange
#         problem = FunctionOneVariableProblem()
#         solution = FunctionOneVariableProblemBinaryIntSolution()
#         optimizer = Algorithm()
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()

#         # Act
#         new_solution = vns_support.local_search_best_improvement(0, problem, solution, optimizer)

#         # Assert
#         self.assertEqual(new_solution, solution)

#         # Act
#         new_solution = vns_support.local_search_best_improvement(33, problem, solution, optimizer)

#         # Assert
#         self.assertEqual(new_solution, solution)

#     # local_search_first_improvement method returns the same solution when k is less than 1 or greater than the representation length
#     def test_local_search_first_improvement_returns_same_solution_when_k_is_less_than_1_or_greater_than_representation_length(self):
#         # Arrange
#         problem = FunctionOneVariableProblem()
#         solution = FunctionOneVariableProblemBinaryIntSolution()
#         optimizer = Algorithm()
#         vns_support = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()

#         # Act
#         new_solution = vns_support.local_search_first_improvement(0, problem, solution, optimizer)

#         # Assert
#         self.assertEqual(new_solution, solution)

#         # Act
#         new_solution = vns_support.local_search_first_improvement(33, problem, solution, optimizer)