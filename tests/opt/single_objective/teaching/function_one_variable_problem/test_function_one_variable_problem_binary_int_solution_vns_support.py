
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

from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem_binary_int_solution_vns_support \
    import FunctionOneVariableProblemBinaryIntSolutionVnsSupport
from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem \
    import FunctionOneVariableProblem
from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem_binary_int_solution \
    import FunctionOneVariableProblemBinaryIntSolution

from uo.target_solution.target_solution import QualityOfSolution
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.metaheuristic.metaheuristic_void import MetaheuristicVoid
from uo.algorithm.metaheuristic.finish_control import FinishControl

class TestFunctionOneVariableProblemBinaryIntSolutionVnsSupport(unittest.TestCase):

    # Returns a deep copy of the object.
    def test_returns_deep_copy(self):
        sup = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        copy_sup = sup.__copy__()

        self.assertIsNot(copy_sup, sup)
        self.assertEqual(copy_sup.__dict__, sup.__dict__)

    # The returned object is not the same object as the original.
    def test_not_same_object(self):
        sup = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        copy_sup = sup.__copy__()

        self.assertIsNot(copy_sup, sup)

    # The returned object has the same attributes and values as the original.
    def test_same_attributes_and_values(self):
        sup = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        copy_sup = sup.__copy__()

        self.assertEqual(copy_sup.__dict__, sup.__dict__)

    # If the object has circular references, the method should still return a deep copy.
    def test_circular_references(self):
        sup = FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        sup.circular_ref = sup
        copy_sup = sup.__copy__()

        self.assertIsNot(copy_sup, sup)


# Generated by CodiumAI

class TestShaking(unittest.TestCase):

    # Given a valid k, problem, solution, and optimizer, 'shaking' method should generate a random mask of k bits and apply it to the solution's representation, then evaluate the solution and return True.
    def test_valid_input_return_true(self):
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 100)
        
        optimizer = mocker.Mock(spec = MetaheuristicVoid)
        type(optimizer).finish_control = mocker.Mock(spec=FinishControl)
        type(optimizer.finish_control).check_evaluations = mocker.Mock(return_value = False)
        type(optimizer.finish_control).evaluations_max = mocker.PropertyMock(return_value = 0)
        type(optimizer).problem = problem
        type(optimizer).evaluation = mocker.PropertyMock(return_value = 0)

        solution.representation = 0

        k = 5

        result = FunctionOneVariableProblemBinaryIntSolutionVnsSupport().shaking(k, problem, solution, optimizer)

        self.assertTrue(result)

    # If the solution's representation bit count is less than or equal to the representation length, 'shaking' method should return True.
    def test_representation_bit_count_less_than_or_equal_to_representation_length_return_true(self):
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 32)
        
        optimizer = mocker.Mock(spec = MetaheuristicVoid)
        type(optimizer).finish_control = mocker.Mock(spec=FinishControl)
        type(optimizer.finish_control).check_evaluations = mocker.Mock(return_value = False)
        type(optimizer.finish_control).evaluations_max = mocker.PropertyMock(return_value = 0)
        type(optimizer).problem = problem
        type(optimizer).evaluation = mocker.PropertyMock(return_value = 0)

        k = 5

        # Set representation bit count to 32
        solution.representation = int('1' * 32, 2)

        result = FunctionOneVariableProblemBinaryIntSolutionVnsSupport().shaking(k, problem, solution, optimizer)

        self.assertTrue(result)

    # If the optimizer's evaluation count exceeds the maximum allowed evaluations, 'shaking' method should return False.
    def test_optimizer_evaluation_count_exceeds_maximum_evaluations_return_false(self):
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 100)
        
        optimizer = mocker.Mock(spec = MetaheuristicVoid)
        type(optimizer).finish_control = mocker.Mock(spec=FinishControl)
        type(optimizer.finish_control).check_evaluations = mocker.Mock(return_value = True)
        type(optimizer.finish_control).evaluations_max = mocker.PropertyMock(return_value = 5)
        type(optimizer).problem = problem

        k = 5

        # Set optimizer evaluation count to 11
        type(optimizer).evaluation = mocker.PropertyMock(return_value = 11)

        result = FunctionOneVariableProblemBinaryIntSolutionVnsSupport().shaking(k, problem, solution, optimizer)

        self.assertFalse(result)

    # If k is less than 1 or greater than the representation length, 'shaking' method should return False.
    def test_k_less_than_1_return_false(self):
        problem = FunctionOneVariableProblem("x**2", 0, 10)
        
        solution = FunctionOneVariableProblemBinaryIntSolution(0, 10, 100)
        
        optimizer = mocker.Mock(spec = MetaheuristicVoid)
        type(optimizer).finish_control = mocker.Mock(spec=FinishControl)
        type(optimizer.finish_control).check_evaluations = mocker.Mock(return_value = True)
        type(optimizer.finish_control).evaluations_max = mocker.PropertyMock(return_value = 5)
        type(optimizer).problem = problem

        k = 0

        result = FunctionOneVariableProblemBinaryIntSolutionVnsSupport().shaking(k, problem, solution, optimizer)

        self.assertFalse(result)
