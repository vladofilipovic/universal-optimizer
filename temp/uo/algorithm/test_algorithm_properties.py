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

from uo.target_problem.target_problem import TargetProblem
from uo.algorithm.output_control import OutputControl
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.algorithm_void import AlgorithmVoid

class TestAlgorithmProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestAlgorithmProperties\n")

    def setUp(self):
        self.name = "some algorithm"
        self.evaluations_max = 42
        self.seconds_max = 42

        self.oc_write_to_output = True
        self.oc_output_file = "some file path..."
        self.output_control = mocker.MagicMock()
        type(self.output_control).write_to_output = self.oc_write_to_output
        type(self.output_control).output_file = self.oc_output_file

        self.pr_name = 'some_problem'
        self.pr_is_minimization = True
        self.pr_file_path = 'some problem file path'
        self.pr_dimension = 42
        self.problem = mocker.MagicMock()
        type(self.problem).name = mocker.PropertyMock(return_value=self.pr_name)
        type(self.problem).is_minimization = mocker.PropertyMock(return_value=self.pr_is_minimization)
        type(self.problem).file_path = mocker.PropertyMock(return_value=self.pr_file_path)
        type(self.problem).dimension = mocker.PropertyMock(return_value=self.pr_dimension)

        self.algorithm = AlgorithmVoid(output_control=self.output_control,
                name=self.name,
                target_problem=self.problem 
        )


    def test_name_should_be_as_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.name, self.name)

    def test_problem_name_should_be_same_that_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.target_problem.name, self.pr_name)

    def test_problem_is_minimization_should_be_same_that_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.target_problem.is_minimization, self.pr_is_minimization)

    def test_problem_file_path_should_be_same_that_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.target_problem.file_path, self.pr_file_path)

    def test_problem_dimension_should_be_same_that_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.target_problem.dimension, self.pr_dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestAlgorithmProperties")
    
if __name__ == '__main__':
    unittest.main()