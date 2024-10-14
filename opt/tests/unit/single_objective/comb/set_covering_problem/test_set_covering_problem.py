import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.comb.min_set_cover_problem.min_set_cover_problem import MinSetCoverProblem
from opt.single_objective.comb.min_set_cover_problem.min_set_cover_problem import MinSetCoverProblem

class TestMinSetCoverProblem(unittest.TestCase):

    # Creating a new instance of MinSetCoverProblem with a specified universe and subsets
    def test_new_instance_with_universe_and_subsets_set_both_properties(self):
        
        #Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]
    
        # Act
        problem = MinSetCoverProblem(universe, subsets)
    
        # Assert
        self.assertEqual(problem.universe, universe)
        self.assertEqual(problem.subsets, subsets)

    # The string representation of an instance of MinSetCoverProblem includes universe and subset properties
    def test_string_representation_includes_universe_and_subset_property(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]
        problem = MinSetCoverProblem(universe, subsets)
    
        # Act
        string_rep = str(problem)
        print("String rep: ", string_rep)
    
        # Assert
        self.assertIn('universe = ' + str(universe), string_rep)
        self.assertIn('subsets=' + str(subsets), string_rep)

    # Copying an instance of MinSetCoverProblem creates a new instance with the same properties
    def test_copy_creates_new_instance_with_same_properties(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]
        problem = MinSetCoverProblem(universe, subsets)
    
        # Act
        copy_problem = problem.copy()
    
        # Assert
        self.assertIsNot(problem, copy_problem)
        self.assertEqual(problem.universe, copy_problem.universe)
        self.assertEqual(problem.subsets, copy_problem.subsets)

    # Attempting to instantiate an instance of MinSetCoverProblem with a universe type that is not set raises a TypeError
    def test_instantiation_with_non_set_universe_raises_type_error(self):
        # Arrange
        universe = '5'
        subsets = [{1, 2, 3}, {3, 4, 5}]
        # Act & Assert
        with self.assertRaises(TypeError):
            problem = MinSetCoverProblem(universe, subsets)

    # The created instance has the correct dimension value
    def test_correct_dimension_value(self):
        # Arrange
        universe = {0, 1, 2, 3}
        subsets = [{0, 1, 2}, {1, 3}]
    
        # Act
        problem = MinSetCoverProblem(universe, subsets)
    
        # Assert
        self.assertEqual(problem.dimension, len(problem.subsets))

    # Attempting to copy an instance of MaxOnesCountProblem creates a new instance with the same properties, but which is not the same object
    def test_copy_creates_new_instance_with_same_properties_but_not_same_object(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]
        problem = MinSetCoverProblem(universe, subsets)
    
        # Act
        copy_problem = problem.copy()
    
        # Assert
        self.assertIsNot(problem, copy_problem)
        self.assertEqual(problem.universe, copy_problem.universe)
        self.assertEqual(problem.subsets, copy_problem.subsets)