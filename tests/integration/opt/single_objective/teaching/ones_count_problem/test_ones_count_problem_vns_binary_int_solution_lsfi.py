

import unittest   
import unittest.mock as mocker

from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_int_solution import OnesCountProblemBinaryIntSolution
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_int_solution_vns_support import OnesCountProblemBinaryIntSolutionVnsSupport

class TestOnesCountProblemVnsBinaryIntSolutionLsfi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationOnesCountProblemVnsBinaryIntSolutionLsfi\n")

    def setUp(self):
        self.output_control = OutputControl(False)
        self.problem_to_solve:OnesCountProblem = OnesCountProblem.from_dimension(dimension=22)
        self.solution:OnesCountProblemBinaryIntSolution = OnesCountProblemBinaryIntSolution()
        self.finish_control:FinishControl = FinishControl(criteria='evaluations', evaluations_max=5000)
        self.vns_support:OnesCountProblemBinaryIntSolutionVnsSupport = OnesCountProblemBinaryIntSolutionVnsSupport()
        self.additional_stat = AdditionalStatisticsControl(keep='')
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.output_control = self.output_control
        vns_construction_params.target_problem = self.problem_to_solve
        vns_construction_params.solution_template = self.solution
        vns_construction_params.problem_solution_vns_support = self.vns_support
        vns_construction_params.finish_control = self.finish_control
        vns_construction_params.random_seed = 43434343
        vns_construction_params.additional_statistics_control = self.additional_stat
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        vns_construction_params.local_search_type = 'local_search_first_improvement'
        self.optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        self.optimizer.optimize()
        return
    
    def test_best_solution_after_optimization_should_be_all_optimal(self):
        result = int('0b1111111111111111111111', base=0)
        self.assertEqual(self.optimizer.best_solution.representation, result)

    def test_best_solution_after_optimization_should_have_optimal_fitness(self):
        self.assertEqual(self.optimizer.best_solution.fitness_value, self.problem_to_solve.dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestIntegrationOnesCountProblemVnsBinaryIntSolutionLsfi")
    
if __name__ == '__main__':
    unittest.main()