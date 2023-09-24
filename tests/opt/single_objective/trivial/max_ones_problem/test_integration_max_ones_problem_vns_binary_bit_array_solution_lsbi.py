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
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution import MaxOnesProblemBinaryBitArraySolution
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution_vns_support import MaxOnesProblemBinaryBitArraySolutionVnsSupport

class TestIntegrationMaxOnesProblemVnsBinaryIntSolutionLsbi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationMaxOnesProblemVnsBinaryIntSolutionLsbi\n")

    def setUp(self):
        self.output_control = OutputControl(False)
        self.problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=24)
        self.solution:MaxOnesProblemBinaryBitArraySolution = MaxOnesProblemBinaryBitArraySolution(random_seed=43434343)
        self.vns_support:MaxOnesProblemBinaryBitArraySolutionVnsSupport = MaxOnesProblemBinaryBitArraySolutionVnsSupport()
        self.optimizer:VnsOptimizer = VnsOptimizer(
                output_control=self.output_control,
                target_problem=self.problem_to_solve, 
                initial_solution=self.solution,
                problem_solution_vns_support=self.vns_support,
                evaluations_max=500, 
                seconds_max=0, 
                random_seed=None, 
                keep_all_solution_codes=False, 
                distance_calculation_cache_is_used=False,
                k_min=1, 
                k_max=3, 
                max_local_optima=10, 
                local_search_type='local_search_best_improvement')
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
        print("\ntearDownClass TestIntegrationMaxOnesProblemVnsBinaryIntSolutionLsbi")
    
if __name__ == '__main__':
    unittest.main()