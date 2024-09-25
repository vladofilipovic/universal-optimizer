import unittest
import unittest.mock as mocker

from bitstring import BitArray
from random import randint, choice
import random
import numpy as np

from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_attraction_support_one_point_bit_array import \
    EmAttractionSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support_one_point_bit_array import \
    EmMutationSupportOnePointBitArray

from opt.single_objective.comb.set_covering_problem.set_covering_problem import SetCoveringProblem
from opt.single_objective.comb.set_covering_problem.set_covering_problem_bit_array_solution import \
    SetCoveringProblemBitArraySolution


class TestSetCoveringProblemBitArraySolutionEmSupport(unittest.TestCase):

    # mutation method returns True when mutation is successful
    def test_mutation_returns_none(self):
        # Arrange
        n = randint(0, 500)
        universe_set = set(np.linspace(0, n, n + 1))

        universe_list = list(universe_set)
        universe_set_integer = set()
        for i in range(len(universe_list)):
                universe_set_integer.add(int(universe_list[i]))
        universe_list = list(universe_set_integer)

        m = randint(1, 50)
        subsets = []

        for i in range(len(universe_set_integer)):
                subsets.append({i})

        for i in range(m):
            number_of_elements = randint(1, n)
            random.shuffle(universe_list)
            subset = set(universe_list[0:number_of_elements])
            subsets.append(subset)

        problem = SetCoveringProblem(universe = universe_set, subsets = subsets)
        solution = SetCoveringProblemBitArraySolution(random_seed=434343)
        solution.init_from( BitArray(length=len(subsets)), problem)
        em_attr_support = EmAttractionSupportOnePointBitArray()
        em_mut_support = EmMutationSupportOnePointBitArray(0.005)
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub)
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).em_support_attraction = mocker.PropertyMock(return_value=em_attr_support)
        # Act
        result = em_mut_support.mutation(problem, solution, optimizer_stub)
        # Assert
        self.assertIsNone(result)