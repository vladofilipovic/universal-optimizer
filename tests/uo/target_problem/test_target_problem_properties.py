
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem 
from uo.target_problem.target_problem_void import TargetProblemVoid 

class TestTargetProblemProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestTargetProblemProperties\n")

    def setUp(self):
        self.problem_name = 'some problem'
        self.to_minimize = True

        self.problem = TargetProblemVoid(
                name=self.problem_name,
                is_minimization = self.to_minimize,
        )
    
    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.name, self.problem_name)

    def test_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.is_minimization, self.to_minimize)

    def test_invalid_name_problem_initialization(self):
        invalid_name = 'invalid name'
        problem = TargetProblemVoid(
            name=invalid_name,
            is_minimization=self.to_minimize,
        )
        self.assertEqual(problem.name, invalid_name)

    # Test problem initialization with an empty name
    def test_empty_name_problem_initialization(self):
        empty_name = ''
        problem = TargetProblemVoid(
            name=empty_name,
            is_minimization=self.to_minimize,
        )
        self.assertEqual(problem.name, empty_name)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestTargetProblemProperties")
    
if __name__ == '__main__':
    unittest.main()