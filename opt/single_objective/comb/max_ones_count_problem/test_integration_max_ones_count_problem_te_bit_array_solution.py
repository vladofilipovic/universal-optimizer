from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)


import unittest   
import unittest.mock as mocker

from copy import deepcopy
from random import randint
from random import choice

from bitstring import Bits, BitArray, BitStream, pack

from uo.algorithm.output_control import OutputControl
from uo.algorithm.exact.total_enumeration.te_operations_support_bit_array import \
    TeOperationsSupportBitArray
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_bit_array_solution import MaxOnesCountProblemBitArraySolution

class TestIntegrationMaxOnesCountProblemTeBitArraySolution(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationMaxOnesCountProblemTeBitArraySolution\n")

    def setUp(self):
        self.problem_to_solve:MaxOnesCountProblem = MaxOnesCountProblem.from_dimension(dimension=12)
        self.solution:MaxOnesCountProblemBitArraySolution = MaxOnesCountProblemBitArraySolution(random_seed=43434343)
        self.te_support:TeOperationsSupportBitArray = TeOperationsSupportBitArray()
        construction_params:TeOptimizerConstructionParameters = TeOptimizerConstructionParameters()
        construction_params.problem = self.problem_to_solve
        construction_params.solution_template = self.solution
        construction_params.te_operations_support = self.te_support
        self.optimizer:TeOptimizer = TeOptimizer.from_construction_tuple(construction_params)
        self.bs = self.optimizer.optimize()

    def test_best_solution_after_optimization_should_be_optimal(self):
        result:str = '111111111111'
        self.assertEqual(self.bs.string_representation(), result)
    
    def test_best_solution_after_optimization_should_be_optimal2(self):
        result:str = '111111111111'
        self.assertEqual(self.optimizer.best_solution.string_representation(), result)

    def test_best_solution_after_optimization_should_be_optimal3(self):
        self.assertEqual(len(self.optimizer.best_solution.string_representation()), self.problem_to_solve.dimension)

    def test_best_solution_after_optimization_should_be_optimal4(self):
        self.assertEqual(len(self.bs.string_representation()), self.problem_to_solve.dimension)

    def test_best_solution_after_optimization_should_have_optimal_fitness(self):
        self.assertEqual(self.optimizer.best_solution.fitness_value, self.problem_to_solve.dimension)

    def test_best_solution_after_optimization_should_have_optimal_fitness2(self):
        self.assertEqual(self.bs.fitness_value, self.problem_to_solve.dimension)

    def test_best_solution_after_optimization_should_have_optimal_objective_value(self):
        self.assertEqual(self.optimizer.best_solution.objective_value, self.problem_to_solve.dimension)

    def test_best_solution_after_optimization_should_have_optimal_objective_value2(self):
        self.assertEqual(self.bs.objective_value, self.problem_to_solve.dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestIntegrationMaxOnesCountProblemTeBitArraySolution")
    
if __name__ == '__main__':
    unittest.main()