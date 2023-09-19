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

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_int_solution import MaxOnesProblemBinaryIntSolution
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_int_solution_vns_support import MaxOnesProblemBinaryIntSolutionVnsSupport

class TestMaxOnesProblemBinaryIntSolutionVnsExecution(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestMaxOnesProblemBinaryIntSolutionVnsExecution\n")

    def setUp(self):
        self.problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=22)
        self.initial_solution:MaxOnesProblemBinaryIntSolution = MaxOnesProblemBinaryIntSolution()
        self.initial_solution.random_init(self.problem_to_solve)
        self.vns_support:MaxOnesProblemBinaryIntSolutionVnsSupport = MaxOnesProblemBinaryIntSolutionVnsSupport()
        self.optimizer:VnsOptimizer = VnsOptimizer(target_problem=self.problem_to_solve, 
                initial_solution=self.initial_solution, 
                problem_solution_vns_support=self.vns_support,
                evaluations_max=500, 
                seconds_max=0, 
                random_seed=42, 
                keep_all_solution_codes=False, 
                k_min=1, 
                k_max=3, 
                max_local_optima=10, 
                local_search_type='local_search_best_improvement')
        self.optimizer.solution_code_distance_cache_cs.is_caching = False
        self.optimizer.output_control.write_to_output_file = False
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
        print("\ntearDownClass TestMaxOnesProblemBinaryIntSolutionVnsExecution")
    
if __name__ == '__main__':
    unittest.main()