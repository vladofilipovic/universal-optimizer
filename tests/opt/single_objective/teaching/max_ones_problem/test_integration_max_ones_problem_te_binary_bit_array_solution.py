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
from uo.algorithm.exact.total_enumeration.te_optimizer_constructor_parameters import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

from opt.single_objective.teaching.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.teaching.max_ones_problem.max_ones_problem_binary_bit_array_solution import MaxOnesProblemBinaryBitArraySolution
from opt.single_objective.teaching.max_ones_problem.max_ones_problem_binary_bit_array_solution_te_support import MaxOnesProblemBinaryBitArraySolutionTeSupport

class TestIntegrationMaxOnesProblemTeBinaryBitArraySolution(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationMaxOnesProblemTeBinaryBitArraySolution\n")

    def setUp(self):
        self.output_control = OutputControl(False)
        self.problem_to_solve:MaxOnesProblem = MaxOnesProblem.from_dimension(dimension=12)
        self.solution:MaxOnesProblemBinaryBitArraySolution = MaxOnesProblemBinaryBitArraySolution(random_seed=43434343)
        self.te_support:MaxOnesProblemBinaryBitArraySolutionTeSupport = MaxOnesProblemBinaryBitArraySolutionTeSupport()
        construction_params:TeOptimizerConstructionParameters = TeOptimizerConstructionParameters()
        construction_params.output_control = self.output_control
        construction_params.target_problem = self.problem_to_solve
        construction_params.initial_solution = self.solution
        construction_params.problem_solution_te_support = self.te_support
        self.optimizer:TeOptimizer = TeOptimizer.from_construction_tuple(construction_params)
        self.optimizer.optimize()
        return
    
    def test_best_solution_after_optimization_should_be_optimal(self):
        result:str = '111111111111'
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
        print("\ntearDownClass TestIntegrationMaxOnesProblemTeBinaryBitArraySolution")
    
if __name__ == '__main__':
    unittest.main()