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
        self.finish_control_mock =  mocker.MagicMock()
        type(self.finish_control_mock).evaluations_max = self.evaluations_max
        type(self.finish_control_mock).iterations_max = self.iterations_max
        type(self.finish_control_mock).seconds_max = self.seconds_max

        self.random_seed = 42

        self.additional_statistics_control_stub = mocker.MagicMock()
        
        self.output_control_stub = mocker.MagicMock()
        type(self.output_control_mock).write_to_output = False

        self.problem_mock = mocker.MagicMock()
        type(self.problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(self.problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(self.problem_mock).file_path = mocker.PropertyMock(return_value='some file path')
        type(self.problem_mock).dimension = mocker.PropertyMock(return_value=42)

        self.optimizer = MetaheuristicVoid(
                name=self.metaheuristicName,
                finish_control=self.finish_control_mock, 
                random_seed=self.random_seed, 
                additional_statistics_control=self.additional_statistics_control_stub, 
                output_control=self.output_control,
                target_problem=self.problem_mock
        )
    
    def test_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.name, self.metaheuristicName)

    def test_evaluations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.finish_control_mock.evaluations_max, self.evaluations_max)

    def test_iterations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.finish_control_mock.iterations_max, self.iterations_max)

    def test_seconds_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.finish_control_mock.seconds_max, self.seconds_max)

    def test_random_seed_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.random_seed, self.random_seed)

    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.target_problem.name, self.problem_mock.name)

    def test_problem_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.target_problem.is_minimization, self.problem_mock.is_minimization)

    def test_problem_file_path_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.target_problem.file_path, self.problem_mock.file_path)

    def test_problem_dimension_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.target_problem.dimension, self.problem_mock.dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestMetaheuristicProperties")
    
if __name__ == '__main__':
    unittest.main()