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
import unittest.mock as mocker

from copy import deepcopy

from datetime import datetime

from uo.target_problem.target_problem import TargetProblem 
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.exact.total_enumeration.problem_solution_te_support import ProblemSolutionTeSupport 
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

class TestTeOptimizerMethodInit(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestTeOptimizerMethodInit\n")

    def setUp(self):       

        self.oc_write_to_output = False
        self.oc_output_file = "some file path..."
        self.output_control_stub = mocker.MagicMock()
        type(self.output_control_stub).write_to_output = self.oc_write_to_output
        type(self.output_control_stub).output_file = self.oc_output_file

        self.pr_name = 'some_problem'
        self.pr_is_minimization = True
        self.pr_file_path = 'some .problem_mock file path'
        self.pr_dimension = 42
        self.problem_mock = mocker.MagicMock()
        type(self.problem_mock).name = mocker.PropertyMock(return_value=self.pr_name)
        type(self.problem_mock).is_minimization = mocker.PropertyMock(return_value=self.pr_is_minimization)
        type(self.problem_mock).file_path = mocker.PropertyMock(return_value=self.pr_file_path)
        type(self.problem_mock).dimension = mocker.PropertyMock(return_value=self.pr_dimension)

        self.solution_name = "void solution"
        self.random_seed = 42
        self.fitness_value = 42.0
        self.objective_value = -42.0
        self.is_feasible = True
        self.solution_mock = mocker.MagicMock()
        type(self.solution_mock).name = self.solution_name, 
        type(self.solution_mock).random_seed = self.random_seed,
        type(self.solution_mock).fitness_value=self.fitness_value,
        type(self.solution_mock).objective_value=self.objective_value,
        type(self.solution_mock).is_feasible= self.is_feasible
        self.solution_mock.evaluate = mocker.Mock(return_value='evaluate')

        self.te_support = mocker.MagicMock()
        self.te_support.reset = mocker.Mock(return_value='reset')

        self.te_optimizer = TeOptimizer(output_control=self.output_control_stub,
                target_problem=self.problem_mock,
                initial_solution= self.solution_mock,
                problem_solution_te_support=self.te_support )
    
    def test_init_method_should_evaluate_initial_solution_once(self):
        self.te_optimizer.execution_started = datetime.now()
        self.te_optimizer.init()
        self.solution_mock.evaluate.assert_called_once()

    def test_init_method_should_evaluate_initial_solution_once_with_supplied_problem(self):
        self.te_optimizer.execution_started = datetime.now()
        self.te_optimizer.init()
        self.solution_mock.evaluate.assert_called_once_with(self.problem_mock)

    def test_init_method_should_call_support_method_reset_once(self):
        self.te_optimizer.execution_started = datetime.now()
        self.te_optimizer.init()
        self.te_support.reset.assert_called_once()

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestTeOptimizerMethodInit")
    
if __name__ == '__main__':
    unittest.main()