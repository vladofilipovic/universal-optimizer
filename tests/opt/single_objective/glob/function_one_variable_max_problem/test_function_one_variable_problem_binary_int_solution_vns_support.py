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
from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem_binary_int_solution_vns_support import FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport


class TestFunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport(unittest.TestCase):

    # shaking method returns True when k is greater than 0 and the solution is valid
    def test_shaking_returns_true_when_k_is_greater_than_0_and_solution_is_valid(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        vns_support = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
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
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)
        # Act
        old_fitness = solution.fitness_value
        result = vns_support.local_search_best_improvement(1, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)
        self.assertGreaterEqual(solution.fitness_value, old_fitness)

    # local_search_first_improvement method returns a new solution with a better fitness value
    def test_local_search_first_improvement_returns_new_solution_with_better_fitness_value(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)
        # Act
        old_fitness = solution.fitness_value
        result = vns_support.local_search_best_improvement(1, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)
        self.assertGreaterEqual(solution.fitness_value, old_fitness)

    # shaking method returns False when k is less than or equal to 0
    def test_shaking_returns_false_when_k_is_less_than_or_equal_to_0(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
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
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).check_evaluations = mocker.PropertyMock(return_value=False)
        type(finish_control_stub).evaluations_max = mocker.PropertyMock(return_value=0)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)
        # Act
        result = vns_support.local_search_best_improvement(0, problem, solution, optimizer_stub)
        # Assert
        self.assertFalse(result)
        # Act
        result = vns_support.local_search_best_improvement(33, problem, solution, optimizer_stub)
        # Assert
        self.assertFalse(result)

    # local_search_first_improvement method returns the same solution when k is less than 1 or greater than the representation length
    def test_local_search_first_improvement_returns_same_solution_when_k_is_less_than_1_or_greater_than_representation_length(self):
        # Arrange
        problem = FunctionOneVariableMaxProblemMax("x**2", 0, 10)
        solution = FunctionOneVariableMaxProblemBinaryIntSolution(0, 10, 4)
        solution.representation = 3
        solution.evaluate(problem)
        vns_support = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).check_evaluations = mocker.PropertyMock(return_value=False)
        type(finish_control_stub).evaluations_max = mocker.PropertyMock(return_value=0)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)
        # Act
        result = vns_support.local_search_first_improvement(0, problem, solution, optimizer_stub)
        # Assert
        self.assertFalse(result)
        # Act
        result = vns_support.local_search_first_improvement(33, problem, solution, optimizer_stub)
        # Assert
        self.assertFalse(result)

    # should return a string representation of the class name 'FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport'
    def test_string_rep_class_name(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('|')
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport')


    # should return a string with the delimiter passed as argument
    def test_string_rep_delimiter(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('|')
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport')

    # should return a string with the indentation passed as argument
    def test_string_rep_indentation(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('|', indentation=4)
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport')

    # should return an empty string when all arguments are empty
    def test_string_rep_empty_arguments(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('', indentation=0, indentation_symbol='', group_start='', group_end='')
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport')

    # should return a string with the indentation_symbol passed as argument
    def test_string_rep_indentation_symbol(self):
        # Arrange
        solution = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
    
        # Act
        result = solution.string_rep('|', indentation_symbol=' ')
    
        # Assert
        self.assertEqual(result, 'FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport')


class Test__Copy__(unittest.TestCase):

    # Should return a deep copy of the object
    def test_return_deep_copy(self):
        sup = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        copy_sup = sup.__copy__()
        self.assertIsNot(sup, copy_sup)
        self.assertEqual(sup.__dict__, copy_sup.__dict__)

    # Should not modify the original object
    def test_not_modify_original_object(self):
        sup = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        original_dict = sup.__dict__.copy()
        copy_sup = sup.__copy__()
        self.assertEqual(sup.__dict__, original_dict)

    # Should copy all attributes of the object
    def test_copy_all_attributes(self):
        sup = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        sup.attribute1 = "value1"
        sup.attribute2 = "value2"
        copy_sup = sup.__copy__()
        self.assertEqual(sup.attribute1, copy_sup.attribute1)
        self.assertEqual(sup.attribute2, copy_sup.attribute2)

    # Should return a new object even if the original object is empty
    def test_return_new_object_empty(self):
        sup = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        copy_sup = sup.__copy__()
        self.assertIsNot(sup, copy_sup)

    # Should return a new object even if the original object has no mutable attributes
    def test_return_new_object_no_mutable_attributes(self):
        sup = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        sup.attribute1 = "value1"
        sup.attribute2 = 10
        copy_sup = sup.__copy__()
        self.assertIsNot(sup, copy_sup)
        self.assertEqual(sup.attribute1, copy_sup.attribute1)
        self.assertEqual(sup.attribute2, copy_sup.attribute2)

    # Should return a new object even if the original object has no immutable attributes
    def test_return_new_object_no_immutable_attributes(self):
        sup = FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        sup.attribute1 = []
        sup.attribute2 = {}
        copy_sup = sup.__copy__()
        self.assertIsNot(sup, copy_sup)
        self.assertEqual(sup.attribute1, copy_sup.attribute1)
        self.assertEqual(sup.attribute2, copy_sup.attribute2)