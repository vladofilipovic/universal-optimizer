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

from uo.target_problem.target_problem import TargetProblem
from uo.target_problem.target_problem_void import TargetProblemVoid
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic 
from uo.algorithm.metaheuristic.metaheuristic_void import MetaheuristicVoid

class TestMetaheuristicProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestMetaheuristicProperties\n")

    def setUp(self):
        self.metaheuristicName = 'Name of the metaheuristic'

        self.evaluations_max = 42
        self.iterations_max = 42
        self.seconds_max = 42
        self.finish_control_mock =  mocker.MagicMock(spec=FinishControl)
        type(self.finish_control_mock).evaluations_max = self.evaluations_max
        type(self.finish_control_mock).iterations_max = self.iterations_max
        type(self.finish_control_mock).seconds_max = self.seconds_max
        self.finish_control_mock.copy = mocker.Mock(return_value=self.finish_control_mock)

        self.random_seed = 42

        self.additional_statistics_control_stub = mocker.MagicMock(spec=AdditionalStatisticsControl)
        
        self.output_control_stub = mocker.MagicMock(spec=OutputControl)
        type(self.output_control_stub).write_to_output = False

        self.problem_mock = mocker.MagicMock(spec=TargetProblemVoid)
        type(self.problem_mock).name = 'some_problem'
        type(self.problem_mock).is_minimization = True
        self.problem_mock.copy = mocker.Mock(return_value=self.problem_mock)

        self.optimizer = MetaheuristicVoid(
                name=self.metaheuristicName,
                finish_control=self.finish_control_mock, 
                random_seed=self.random_seed, 
                additional_statistics_control=self.additional_statistics_control_stub, 
                output_control=self.output_control_stub,
                target_problem=self.problem_mock
        )
    
    def test_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.name, self.metaheuristicName)

    def test_evaluations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.finish_control.evaluations_max, self.finish_control_mock.evaluations_max)

    def test_iterations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.finish_control.iterations_max, self.finish_control_mock.iterations_max)

    def test_seconds_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.finish_control.seconds_max, self.finish_control_mock.seconds_max)

    def test_random_seed_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.random_seed, self.random_seed)

    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.target_problem.name, self.problem_mock.name)

    def test_problem_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.target_problem.is_minimization, self.problem_mock.is_minimization)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestMetaheuristicProperties")
    
if __name__ == '__main__':
    unittest.main()