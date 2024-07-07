from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)


import unittest   
import unittest.mock as mocker

from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_bit_array import \
        VnsShakingSupportStandardBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_bit_array import \
        VnsLocalSearchSupportStandardBestImprovementBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_bit_array_solution import OnesCountMaxProblemBitArraySolution

class TestOnesCountMaxProblemVnsBitArraySolutionLsbi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationOnesCountMaxProblemVnsBitArraySolutionLsbi\n")

    def setUp(self):
        self.problem_to_solve:OnesCountMaxProblem = OnesCountMaxProblem.from_dimension(dimension=24)
        self.solution:OnesCountMaxProblemBitArraySolution = OnesCountMaxProblemBitArraySolution(random_seed=43434343)
        self.finish_control:FinishControl = FinishControl(criteria='evaluations', evaluations_max=1000)
        self.vns_shaking_support:VnsShakingSupportStandardBitArray = \
                VnsShakingSupportStandardBitArray(self.problem_to_solve.dimension)
        self.vns_ls_support:VnsLocalSearchSupportStandardBestImprovementBitArray = \
                VnsLocalSearchSupportStandardBestImprovementBitArray(self.problem_to_solve.dimension)
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.problem = self.problem_to_solve
        vns_construction_params.solution_template = self.solution
        vns_construction_params.vns_shaking_support = self.vns_shaking_support
        vns_construction_params.vns_ls_support = self.vns_ls_support
        vns_construction_params.finish_control = self.finish_control
        vns_construction_params.random_seed = 43434343
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        self.optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        self.bs = self.optimizer.optimize()
    
    def test_best_solution_after_optimization_should_be_all_optimal(self):
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
        print("\ntearDownClass TestIntegrationOnesCountMaxProblemVnsBitArraySolutionLsbi")
    
if __name__ == '__main__':
    unittest.main()