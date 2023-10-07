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

from copy import deepcopy
from random import randint
from random import choice

from bitstring import Bits, BitArray, BitStream, pack

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer_constructor_parameters import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution import MaxOnesProblemBinaryBitArraySolution
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution_vns_support import MaxOnesProblemBinaryBitArraySolutionVnsSupport

class TestIntegrationMaxOnesProblemVnsBinaryBitArraySolutionLsbi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationMaxOnesProblemVnsBinaryBitArraySolutionLsbi\n")

    def setUp(self):
        self.output_control = OutputControl(False)
        self.problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=24)
        self.solution:MaxOnesProblemBinaryBitArraySolution = MaxOnesProblemBinaryBitArraySolution(random_seed=43434343)
        self.finish_control:FinishControl = FinishControl(criteria='evaluations', evaluations_max=500)
        self.additional_stat = AdditionalStatisticsControl(keep='')
        self.vns_support:MaxOnesProblemBinaryBitArraySolutionVnsSupport = \
                MaxOnesProblemBinaryBitArraySolutionVnsSupport()
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.output_control = self.output_control
        vns_construction_params.target_problem = self.problem_to_solve
        vns_construction_params.initial_solution = self.solution
        vns_construction_params.problem_solution_vns_support = self.vns_support
        vns_construction_params.finish_control = self.finish_control
        vns_construction_params.random_seed = 43434343
        vns_construction_params.additional_statistics_control = self.additional_stat
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        vns_construction_params.local_search_type = 'local_search_best_improvement'
        self.optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        self.optimizer.optimize()
        return
    
    def test_best_solution_after_optimization_should_be_optimal(self):
        result:str = '111111111111111111111111'
        self.assertEqual(self.optimizer.best_solution.string_representation(), result)

    def test_best_solution_after_optimization_should_be_optimal_2(self):
        self.assertEqual(len(self.optimizer.best_solution.string_representation()), self.problem_to_solve.dimension)

    def test_best_solution_after_optimization_should_have_optimal_fitness(self):
        self.assertEqual(self.optimizer.best_solution.fitness_value, self.problem_to_solve.dimension)

    def test_best_solution_after_optimization_should_have_optimal_objective_value(self):
        self.assertEqual(self.optimizer.best_solution.objective_value, self.problem_to_solve.dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestIntegrationMaxOnesProblemVnsBinaryBitArraySolutionLsbi")
    
if __name__ == '__main__':
    unittest.main()