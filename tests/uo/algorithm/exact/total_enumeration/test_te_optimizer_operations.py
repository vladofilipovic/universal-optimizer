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

from uo.target_problem.target_problem import TargetProblem 
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.exact.total_enumeration.problem_solution_te_support import ProblemSolutionTeSupport 
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

class TestTeOptimizerOperations(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestTeOptimizerOperations\n")

    def setUp(self):       

        self.oc_write_to_output = True
        self.oc_output_file = "some file path..."
        self.output_control = mock.MagicMock()
        type(self.output_control).write_to_output = self.oc_write_to_output
        type(self.output_control).output_file = self.oc_output_file

        self.pr_name = 'some_problem'
        self.pr_is_minimization = True
        self.pr_file_path = 'some problem file path'
        self.pr_dimension = 42
        self.problem = mock.MagicMock()
        type(self.problem).name = mock.PropertyMock(return_value=self.pr_name)
        type(self.problem).is_minimization = mock.PropertyMock(return_value=self.pr_is_minimization)
        type(self.problem).file_path = mock.PropertyMock(return_value=self.pr_file_path)
        type(self.problem).dimension = mock.PropertyMock(return_value=self.pr_dimension)


        self.solution_name = "void solution"
        self.random_seed = 42
        self.fitness_value = 42.0
        self.objective_value = -42.0
        self.is_feasible = True
        self.solution = mock.MagicMock()
        type(self.solution).name = self.solution_name, 
        type(self.solution).random_seed = self.random_seed,
        type(self.solution).fitness_value=self.fitness_value,
        type(self.solution).objective_value=self.objective_value,
        type(self.solution).is_feasible= self.is_feasible
        
        self.te_support = mock.MagicMock()

        self.te_optimizer = TeOptimizer(output_control=self.output_control,
                target_problem=self.problem,
                initial_solution= self.solution,
                problem_solution_te_support=self.te_support )
        return
    
    def test_is_feasible_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.solution.is_feasible, self.is_feasible)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestTeOptimizerOperations")
    
if __name__ == '__main__':
    unittest.main()