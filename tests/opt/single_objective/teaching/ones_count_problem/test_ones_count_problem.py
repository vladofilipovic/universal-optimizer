

import unittest
import unittest.mock as mocker

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem

class TestOnesCountProblem(unittest.TestCase):

    # Creating a new instance of OnesCountProblem with a specified dimension sets the dimension property correctly
    def test_new_instance_with_dimension_sets_dimension_property(self):
        # Arrange
        dim = 5
    
        # Act
        problem = OnesCountProblem(dim)
    
        # Assert
        self.assertEqual(problem.dimension, dim)

    # The string representation of an instance of OnesCountProblem includes the dimension property
    def test_string_representation_includes_dimension_property(self):
        # Arrange
        dim = 5
        problem = OnesCountProblem(dim)
    
        # Act
        string_rep = str(problem)
    
        # Assert
        self.assertIn(f'dimension={dim}', string_rep)

    # Copying an instance of OnesCountProblem creates a new instance with the same properties
    def test_copy_creates_new_instance_with_same_properties(self):
        # Arrange
        dim = 5
        problem = OnesCountProblem(dim)
    
        # Act
        copy_problem = problem.copy()
    
        # Assert
        self.assertIsNot(problem, copy_problem)
        self.assertEqual(problem.dimension, copy_problem.dimension)

    # The OnesCountProblem class can be instantiated without a dimension parameter
    def test_instantiation_without_dimension_parameter(self):
        # Arrange
    
        # Act
        problem = OnesCountProblem()
    
        # Assert
        self.assertIsNone(problem.dimension)

    # The OnesCountProblem class can be instantiated from an input file with a specified format
    def test_instantiation_from_input_file_with_specified_format(self):
        # Arrange
        input_file_path = 'input.txt'
        input_format = 'txt'

        with mocker.patch.object(OnesCountProblem, '__load_from_file__', return_value=5):
            # Act
            problem = OnesCountProblem.from_input_file(input_file_path, input_format)
    
        # Assert
        self.assertEqual(problem.dimension, 5)

    # The from_dimension method of OnesCountProblem creates a new instance with the specified dimension
    def test_from_dimension_creates_new_instance_with_specified_dimension(self):
        # Arrange
        dim = 5
    
        # Act
        problem = OnesCountProblem.from_dimension(dim)
    
        # Assert
        self.assertEqual(problem.dimension, dim)

    # Attempting to instantiate an instance of OnesCountProblem with a non-integer dimension raises a TypeError
    def test_instantiation_with_non_integer_dimension_raises_type_error(self):
        # Arrange
        dim = '5'
    
        # Act & Assert
        with self.assertRaises(TypeError):
            problem = OnesCountProblem(dim)

    # Attempting to instantiate an instance of OnesCountProblem with a negative dimension raises a ValueError
    def test_instantiation_with_negative_dimension_raises_value_error(self):
        # Arrange
        dim = -5
    
        # Act & Assert
        with self.assertRaises(ValueError):
            problem = OnesCountProblem(dim)

    # Attempting to instantiate an instance of OnesCountProblem with a dimension of zero raises a ValueError
    def test_instantiation_with_zero_dimension_raises_value_error(self):
        # Arrange
        dim = 0
    
        # Act & Assert
        with self.assertRaises(ValueError):
            problem = OnesCountProblem(dim)

    # Attempting to instantiate an instance of OnesCountProblem from an input file with an unsupported format raises a ValueError
    def test_instantiation_from_input_file_with_unsupported_format_raises_value_error(self):
        # Arrange
        input_file_path = 'input.txt'
        input_format = 'csv'
        with mocker.patch.object(OnesCountProblem, '__load_from_file__', side_effect=ValueError):
    
            # Act & Assert
            with self.assertRaises(ValueError):
                problem = OnesCountProblem.from_input_file(input_file_path, input_format)

    # Attempting to instantiate an instance of OnesCountProblem from an input file with a missing dimension value raises a ValueError
    def test_instantiation_from_input_file_with_missing_dimension_value_raises_value_error(self):
        # Arrange
        input_file_path = 'input.txt'
        input_format = 'txt'
        with mocker.patch.object(OnesCountProblem, '__load_from_file__', return_value=None):
        
            # Act & Assert
            with self.assertRaises(ValueError):
                problem = OnesCountProblem.from_input_file(input_file_path, input_format)

    # Attempting to copy an instance of OnesCountProblem creates a new instance with the same properties, but which is not the same object
    def test_copy_creates_new_instance_with_same_properties_but_not_same_object(self):
        # Arrange
        dim = 5
        problem = OnesCountProblem(dim)
    
        # Act
        copy_problem = problem.copy()
    
        # Assert
        self.assertIsNot(problem, copy_problem)
        self.assertEqual(problem.dimension, copy_problem.dimension)