
import unittest
import unittest.mock as mocker

from bitstring import BitArray
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_min_problem.ones_count_min_problem import OnesCountMinProblem

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.algorithm import Algorithm
from uo.algorithm.algorithm_void import AlgorithmVoid
from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_bit_array_solution import OnesCountMaxProblemBinaryBitArraySolution
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_bit_array_solution_vns_support import OnesCountMaxProblemBinaryBitArraySolutionVnsSupport


class TestOnesCountMaxProblemBinaryBitArraySolutionVnsSupport(unittest.TestCase):

    # shaking method returns True when randomization is successful
    def test_shaking_returns_true_when_randomization_is_successful(self):
        # Arrange
        problem = OnesCountMaxProblem(dim=5)
        solution = OnesCountMaxProblemBinaryBitArraySolution(random_seed=434343)
        solution.init_from( BitArray('0b10101'), problem)
        vns_support = OnesCountMaxProblemBinaryBitArraySolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)
        # Act
        result = vns_support.shaking(5, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)

    # local_search_best_improvement method returns a solution with higher fitness value
    def test_local_search_best_improvement_returns_solution_with_higher_fitness_value11(self):
        # Arrange
        problem = OnesCountMaxProblem(dim=8)
        solution = OnesCountMaxProblemBinaryBitArraySolution(random_seed=434343)
        solution.init_from( BitArray('0b00110010'), problem)
        solution.evaluate(problem)
        vns_support = OnesCountMaxProblemBinaryBitArraySolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=4)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)
        optimizer_stub.is_first_better = mocker.Mock(return_value=True)
        # Act
        old_fitness = solution.fitness_value
        result = vns_support.local_search_best_improvement(3, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)
        self.assertGreaterEqual(solution.fitness_value, old_fitness)

    # local_search_first_improvement method returns a solution with higher fitness value
    def test_local_search_first_improvement_returns_solution_with_higher_fitness_value10(self):
        # Arrange
        problem = OnesCountMaxProblem(dim=6)
        solution = OnesCountMaxProblemBinaryBitArraySolution(random_seed=434343)
        solution.init_from( BitArray('0b000001'), problem)
        solution.evaluate(problem)
        vns_support = OnesCountMaxProblemBinaryBitArraySolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)
        # Act
        old_fitness = solution.fitness_value
        result = vns_support.local_search_first_improvement(3, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)
        self.assertGreaterEqual(solution.fitness_value, old_fitness)


    # shaking method modifies the solution representation when the number of ones in the solution representation is less than the problem dimension
    def test_shaking_modifies_solution_representation_when_number_of_ones_is_less_than_problem_dimension8(self):
        # Arrange
        problem = OnesCountMaxProblem(dim=5)
        solution = OnesCountMaxProblemBinaryBitArraySolution(random_seed=434343)
        solution.init_from( BitArray(bin='0' * problem.dimension), problem)
        vns_support = OnesCountMaxProblemBinaryBitArraySolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)
        # Act
        vns_support.shaking(5, problem, solution, optimizer_stub)
        # Assert
        self.assertNotEqual(solution.representation.bin, '0' * problem.dimension)

    # local_search_best_improvement method returns a solution with higher fitness value
    def test_local_search_best_improvement_returns_solution_with_higher_fitness_value6(self):
        # Arrange
        problem = OnesCountMaxProblem(dim=8)
        solution = OnesCountMaxProblemBinaryBitArraySolution(random_seed=434343)
        solution.init_from( BitArray('0b00110010'), problem)
        solution.evaluate(problem)
        vns_support = OnesCountMaxProblemBinaryBitArraySolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)        
        # Act
        old_fitness = solution.fitness_value
        result = vns_support.local_search_best_improvement(3, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)
        self.assertGreaterEqual(solution.fitness_value, old_fitness)

    # local_search_first_improvement method returns a solution with higher fitness value
    def test_local_search_first_improvement_returns_solution_with_higher_fitness_value4(self):
        # Arrange
        problem = OnesCountMaxProblem(dim=8)
        solution = OnesCountMaxProblemBinaryBitArraySolution(random_seed=434343)
        solution.init_from( BitArray('0b00110010'), problem)
        solution.evaluate(problem)
        vns_support = OnesCountMaxProblemBinaryBitArraySolutionVnsSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_support = mocker.PropertyMock(return_value=vns_support)        
        # Act
        old_fitness = solution.fitness_value
        result = vns_support.local_search_first_improvement(3, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)
        self.assertGreaterEqual(solution.fitness_value, old_fitness)



