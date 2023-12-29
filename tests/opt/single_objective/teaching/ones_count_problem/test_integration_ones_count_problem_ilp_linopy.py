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

from linopy import Model

from bitstring import Bits, BitArray, BitStream, pack

from uo.algorithm.output_control import OutputControl
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_ilp_linopy import \
        OnesCountProblemIntegerLinearProgrammingSolver

class TestIntegrationOnesCountProblemIlpLinopy(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationOnesCountProblemIlpLinopy\n")

    def setUp(self):
        self.output_control = OutputControl(False)
        self.problem_to_solve:OnesCountProblem = OnesCountProblem.from_dimension(dimension=12)
        self.optimizer:OnesCountProblemIntegerLinearProgrammingSolver = OnesCountProblemIntegerLinearProgrammingSolver(
            output_control=self.output_control,
            problem=self.problem_to_solve
        )
        self.optimizer.optimize()
        return
    
    def test_best_solution_after_optimization_should_be_optimal(self):
        result = ''
        expected = ''
        for i in range(self.optimizer.model.nvars):
            result += str(int(self.optimizer.model.solution.x[i]))
            expected += '1'
        self.assertEqual(expected, result)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestIntegrationOnesCountProblemIlpLinopy")
    
if __name__ == '__main__':
    unittest.main()