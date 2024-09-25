
import unittest
import unittest.mock as mocker
import networkx as nx

from bitstring import BitArray
from random import randint, choice

from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_attraction_support_one_point_bit_array import \
    EmAttractionSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support_one_point_bit_array import \
    EmMutationSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_direction_support_one_point_bit_array import \
    EmDirectionSupportOnePointBitArray

from opt.single_objective.comb.set_covering_problem.set_covering_problem import SetCoveringProblem
from opt.single_objective.comb.set_covering_problem.set_covering_problem_bit_array_solution import \
    SetCoveringProblemBitArraySolution


class TestSetCoveringProblemBitArraySolutionEmSupport(unittest.TestCase):

    # mutation method returns True when mutation is successful
    def test_mutation_returns_none(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]

        problem = SetCoveringProblem(universe=universe, subsets=subsets)
        solution = SetCoveringProblemBitArraySolution(random_seed=434343)
        solution.init_from( BitArray(length=len(subsets)), problem)
        em_attr_support = EmAttractionSupportOnePointBitArray()
        em_mut_support = EmMutationSupportOnePointBitArray(0.005)
        em_dir_support = EmDirectionSupportOnePointBitArray()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub)
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).em_support_attraction = mocker.PropertyMock(return_value=em_attr_support)
        type(optimizer_stub).em_support_direction = mocker.PropertyMock(return_value=em_dir_support)
        # Act
        result = em_mut_support.mutation(problem, solution, optimizer_stub)
        # Assert
        self.assertIsNone(result)

    def test_direction_returns_correct_type(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]

        problem = SetCoveringProblem(universe=universe, subsets=subsets)
        solution = SetCoveringProblemBitArraySolution(random_seed=434343)
        solution.init_from( BitArray(length=len(subsets)), problem)
        em_attr_support = EmAttractionSupportOnePointBitArray()
        em_mut_support = EmMutationSupportOnePointBitArray(0.005)
        em_dir_support = EmDirectionSupportOnePointBitArray()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub)
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).em_support_attraction = mocker.PropertyMock(return_value=em_attr_support)
        type(optimizer_stub).em_support_direction = mocker.PropertyMock(return_value=em_dir_support)
        # Act
        result = em_mut_support.mutation(problem, solution, optimizer_stub)
        # Assert
        self.assertIsNone(result)