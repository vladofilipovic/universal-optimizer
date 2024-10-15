
import unittest   
import unittest.mock as mocker

from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_int import \
        VnsShakingSupportStandardInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_int import \
        VnsLocalSearchSupportStandardBestImprovementInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_fi_int import \
        VnsLocalSearchSupportStandardFirstImprovementInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_int_solution import \
        MaxOnesCountProblemIntSolution

class TestIntegrationMaxOnesCountProblemVnsIntSolutionLsfi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationMaxOnesCountProblemVnsIntSolutionLsfi\n")

    def setUp(self):
        self.problem_to_solve:MaxOnesCountProblem = MaxOnesCountProblem.from_dimension(dimension=22)
        self.solution:MaxOnesCountProblemIntSolution = MaxOnesCountProblemIntSolution()
        self.finish_control:FinishControl = FinishControl(criteria='evaluations', evaluations_max=5000)
        self.vns_shaking_support:VnsShakingSupportStandardInt = \
                VnsShakingSupportStandardInt(self.problem_to_solve.dimension)
        self.vns_ls_support:VnsLocalSearchSupportStandardFirstImprovementInt = \
                VnsLocalSearchSupportStandardFirstImprovementInt(self.problem_to_solve.dimension)
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
        result = int('0b1111111111111111111111', base=0)
        self.assertEqual(self.optimizer.best_solution.representation, result)

    def test_best_solution_after_optimization_should_have_optimal_fitness(self):
        self.assertEqual(self.optimizer.best_solution.fitness_value, self.problem_to_solve.dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestIntegrationMaxOnesCountProblemVnsIntSolutionLsfi")
    
if __name__ == '__main__':
    unittest.main()