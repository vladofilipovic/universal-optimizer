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

class TargetProblemVoid(TargetProblem):
    
    def __init__(self, name:str, is_minimization:bool, file_path:str, dimension:int=None)->None:
        super().__init__(name, is_minimization, file_path, dimension)

    def __copy__(self):
        pr = deepcopy(self)
        return pr

    def copy(self):
        return self.__copy__()

    def load_from_file(data_representation: str)->None:
        return

    def __str__(self)->str:
        return ''

    def __repr__(self)->str:
        return ''

    def __format__(self, spec:str)->str:
        return ''
    

class TestTargetProblemProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestTargetProblemProperties\n")

    def setUp(self):
        self.problem_name = 'some problem'
        self.to_minimize = True
        self.dimension = 42
        self.file_path = 'some file path'

        self.problem = TargetProblemVoid(
                name=self.problem_name,
                is_minimization = self.to_minimize,
                dimension=self.dimension,
                file_path=self.file_path  
        )
        return
    
    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.name, self.problem_name)

    def test_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.is_minimization, self.to_minimize)

    def test_dimension_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.dimension, self.dimension)

    def test_file_path_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.file_path, self.file_path)

    def test_dimension_should_be_equal_as_value_set_by_property_setter(self):
        self.problem.dimension = 11
        self.assertEqual(self.problem.dimension, 11)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestTargetProblemProperties")
    
if __name__ == '__main__':
    unittest.main()