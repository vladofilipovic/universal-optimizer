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
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_bit_array_solution import OnesCountMaxProblemBinaryBitArraySolution
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_bit_array_solution_te_support import OnesCountMaxProblemBinaryBitArraySolutionTeSupport

class TestOnesCountMaxProblemTeBinaryBitArraySolution(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationOnesCountMaxProblemTeBinaryBitArraySolution\n")

    def setUp(self):
        self.output_control = OutputControl(False)
        self.problem_to_solve:OnesCountMaxProblem = OnesCountMaxProblem.from_dimension(dimension=12)
        self.solution:OnesCountMaxProblemBinaryBitArraySolution = OnesCountMaxProblemBinaryBitArraySolution(random_seed=43434343)
        self.te_support:OnesCountMaxProblemBinaryBitArraySolutionTeSupport = OnesCountMaxProblemBinaryBitArraySolutionTeSupport()
        construction_params:TeOptimizerConstructionParameters = TeOptimizerConstructionParameters()
        construction_params.output_control = self.output_control
        construction_params.problem = self.problem_to_solve
        construction_params.solution_template = self.solution
        construction_params.problem_solution_te_support = self.te_support
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
        print("\ntearDownClass TestIntegrationOnesCountMaxProblemTeBinaryBitArraySolution")
    
if __name__ == '__main__':
    unittest.main()