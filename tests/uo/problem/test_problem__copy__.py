

import unittest

from copy import deepcopy

from uo.problem.problem import Problem 
from uo.problem.problem_void import ProblemVoid 

class Test__Copy__(unittest.TestCase):

    # Returns a new instance of Problem with the same properties as the original.
    def test_returns_new_instance_with_same_properties(self):
        problem = ProblemVoid("problem", True)
        copy_problem = problem.__copy__()
        self.assertIsInstance(copy_problem, Problem)
        self.assertEqual(copy_problem.name, problem.name)
        self.assertEqual(copy_problem.is_minimization, problem.is_minimization)

    # The new instance is a deep copy of the original instance.
    def test_new_instance_is_deep_copy(self):
        problem = ProblemVoid("problem", True)
        copy_problem = problem.__copy__()
        self.assertIsNot(copy_problem, problem)
        self.assertEqual(copy_problem.name, problem.name)
        self.assertEqual(copy_problem.is_minimization, problem.is_minimization)

    # The new instance is not the same object as the original instance.
    def test_new_instance_is_not_same_object(self):
        problem = ProblemVoid("problem", True)
        copy_problem = problem.__copy__()
        self.assertIsNot(copy_problem, problem)

    # The method raises a TypeError if called with arguments.
    def test_raises_type_error_with_arguments(self):
        problem = ProblemVoid("problem", True)
        with self.assertRaises(TypeError):
            problem.__copy__(1)

    # The method raises a TypeError if called on a class instead of an instance.
    def test_raises_type_error_on_class(self):
        with self.assertRaises(TypeError):
            ProblemVoid.__copy__()
