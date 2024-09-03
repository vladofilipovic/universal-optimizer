import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.comb.set_covering_problem.set_covering_problem import SetCoveringProblem
from opt.single_objective.comb.set_covering_problem.set_covering_problem import SetCoveringProblem

class TestSetCoveringProblem(unittest.TestCase):

    # Creating a new instance of SetCoveringProblem with a specified universe and subsets
    def test_new_instance_with_universe_and_subsets_set_both_properties(self):
        
        #Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]
    
        # Act
        problem = SetCoveringProblem(universe, subsets)
    
        # Assert
        self.assertEqual(problem.universe, universe)
        self.assertEqual(problem.subsets, subsets)

    # The string representation of an instance of SetCoveringProblem includes universe and subset properties
    def test_string_representation_includes_universe_and_subset_property(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]
        problem = SetCoveringProblem(universe, subsets)
    
        # Act
        string_rep = str(problem)
    
        # Assert
        self.assertIn('universe =' + str(universe), string_rep)
        self.assertIn('subsets=' + str(subsets), string_rep)

    # Copying an instance of SetCoveringProblem creates a new instance with the same properties
    def test_copy_creates_new_instance_with_same_properties(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]
        problem = SetCoveringProblem(universe, subsets)
    
        # Act
        copy_problem = problem.copy()
    
        # Assert
        self.assertIsNot(problem, copy_problem)
        self.assertEqual(problem.universe, copy_problem.universe)
        self.assertEqual(problem.subsets, copy_problem.subsets)


    # The SetCoveringProblem class can be instantiated from an input that is written in files
    def test_instantiation_from_input_file(self):
        # Arrange
        input_universe_path = 'universe.txt'
        input_subset_path = 'subsets.json'
        with mocker.patch.object(SetCoveringProblem, '__load_from_file__', side_effect=ValueError):
    
            # Act & Assert
            with self.assertRaises(ValueError):
                problem = SetCoveringProblem.from_input_file(input_universe_path, input_subset_path)

    # Attempting to copy an instance of OnesCountMaxProblem creates a new instance with the same properties, but which is not the same object
    def test_copy_creates_new_instance_with_same_properties_but_not_same_object(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]
        problem = SetCoveringProblem(universe, subsets)
    
        # Act
        copy_problem = problem.copy()
    
        # Assert
        self.assertIsNot(problem, copy_problem)
        self.assertEqual(problem.universe, copy_problem.universe)
        self.assertEqual(problem.subsets, copy_problem.subsets)
