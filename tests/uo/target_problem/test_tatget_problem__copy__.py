

import unittest

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem 
from uo.target_problem.target_problem_void import TargetProblemVoid 

class Test__Copy__(unittest.TestCase):

    # Returns a new instance of TargetProblem with the same properties as the original.
    def test_returns_new_instance_with_same_properties(self):
        problem = TargetProblemVoid("problem", True)
        copy_problem = problem.__copy__()
        self.assertIsInstance(copy_problem, TargetProblem)
        self.assertEqual(copy_problem.name, problem.name)
        self.assertEqual(copy_problem.is_minimization, problem.is_minimization)

    # The new instance is a deep copy of the original instance.
    def test_new_instance_is_deep_copy(self):
        problem = TargetProblemVoid("problem", True)
        copy_problem = problem.__copy__()
        self.assertIsNot(copy_problem, problem)
        self.assertEqual(copy_problem.name, problem.name)
        self.assertEqual(copy_problem.is_minimization, problem.is_minimization)

    # The new instance is not the same object as the original instance.
    def test_new_instance_is_not_same_object(self):
        problem = TargetProblemVoid("problem", True)
        copy_problem = problem.__copy__()
        self.assertIsNot(copy_problem, problem)

    # The method raises a TypeError if called with arguments.
    def test_raises_type_error_with_arguments(self):
        problem = TargetProblemVoid("problem", True)
        with self.assertRaises(TypeError):
            problem.__copy__(1)

    # The method raises a TypeError if called on a class instead of an instance.
    def test_raises_type_error_on_class(self):
        with self.assertRaises(TypeError):
            TargetProblemVoid.__copy__()
