
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.problem.problem import Problem 
from uo.problem.problem_void_min_so import ProblemVoidMinSO 

class TestProblemProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestProblemProperties\n")

    def setUp(self):
        self.problem_name = 'some problem'
        self.to_minimize = True

        self.problem = ProblemVoidMinSO(
                name=self.problem_name,
                is_minimization = self.to_minimize,
        )
    
    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.name, self.problem_name)

    def test_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.is_minimization, self.to_minimize)

    def test_invalid_name_problem_initialization(self):
        invalid_name = 'invalid name'
        problem = ProblemVoidMinSO(
            name=invalid_name,
            is_minimization=self.to_minimize,
        )
        self.assertEqual(problem.name, invalid_name)

    # Test problem initialization with an empty name
    def test_empty_name_problem_initialization(self):
        empty_name = ''
        problem = ProblemVoidMinSO(
            name=empty_name,
            is_minimization=self.to_minimize,
        )
        self.assertEqual(problem.name, empty_name)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestProblemProperties")

class TestPorblrmCopy(unittest.TestCase):

    # Returns a new instance of Problem with the same properties as the original.
    def test_returns_new_instance_with_same_properties(self):
        problem = ProblemVoidMinSO("problem", True)
        copy_problem = problem.__copy__()
        self.assertIsInstance(copy_problem, Problem)
        self.assertEqual(copy_problem.name, problem.name)
        self.assertEqual(copy_problem.is_minimization, problem.is_minimization)

    # The new instance is a deep copy of the original instance.
    def test_new_instance_is_deep_copy(self):
        problem = ProblemVoidMinSO("problem", True)
        copy_problem = problem.__copy__()
        self.assertIsNot(copy_problem, problem)
        self.assertEqual(copy_problem.name, problem.name)
        self.assertEqual(copy_problem.is_minimization, problem.is_minimization)

    # The new instance is not the same object as the original instance.
    def test_new_instance_is_not_same_object(self):
        problem = ProblemVoidMinSO("problem", True)
        copy_problem = problem.__copy__()
        self.assertIsNot(copy_problem, problem)

    # The method raises a TypeError if called with arguments.
    def test_raises_type_error_with_arguments(self):
        problem = ProblemVoidMinSO("problem", True)
        with self.assertRaises(TypeError):
            problem.__copy__(1)

    # The method raises a TypeError if called on a class instead of an instance.
    def test_raises_type_error_on_class(self):
        with self.assertRaises(TypeError):
            ProblemVoidMinSO.__copy__()

if __name__ == '__main__':
    unittest.main()