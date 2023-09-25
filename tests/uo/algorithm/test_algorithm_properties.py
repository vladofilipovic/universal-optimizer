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
from uo.algorithm.output_control import OutputControl
from uo.algorithm.algorithm import Algorithm

class AlgorithmVoid(Algorithm):
    def __init__(self, name:str, output_control:OutputControl,
            target_problem:TargetProblem)->None:
        super().__init__(name, output_control, target_problem)

    def __copy__(self):
        return super().__copy__()

    def copy(self):
        return self.__copy__()

    def init(self):
        return
    def __str__(self)->str:
        return super().__str__()

    def __repr__(self)->str:
        return super().__repr__()

    def __format__(self, spec:str)->str:
        return super().__format__()


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

        self.algorithm = AlgorithmVoid(output_control=self.output_control,
                name=self.name,
                target_problem=self.problem 
        )
        return

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