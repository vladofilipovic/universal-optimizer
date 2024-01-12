

import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem

class TestOnesCountMaxProblem(unittest.TestCase):

    # Creating a new instance of OnesCountMaxProblem with a specified dimension sets the dimension property correctly
    def test_new_instance_with_dimension_sets_dimension_property(self):
        # Arrange
        dim = 5
    
        # Act
        problem = OnesCountMaxProblem(dim)
    
        # Assert
        self.assertEqual(problem.dimension, dim)

    # The string representation of an instance of OnesCountMaxProblem includes the dimension property
    def test_string_representation_includes_dimension_property(self):
        # Arrange
        dim = 5
        problem = OnesCountMaxProblem(dim)
    
        # Act
        string_rep = str(problem)
    
        # Assert
        self.assertIn(f'dimension={dim}', string_rep)

    # Copying an instance of OnesCountMaxProblem creates a new instance with the same properties
    def test_copy_creates_new_instance_with_same_properties(self):
        # Arrange
        dim = 5
        problem = OnesCountMaxProblem(dim)
    
        # Act
        copy_problem = problem.copy()
    
        # Assert
        self.assertIsNot(problem, copy_problem)
        self.assertEqual(problem.dimension, copy_problem.dimension)

    # The OnesCountMaxProblem class can be instantiated without a dimension parameter
    def test_instantiation_without_dimension_parameter(self):
        # Arrange
        dim = None

        # Act & Assert
        with self.assertRaises(TypeError):
            problem = OnesCountMaxProblem(dim)


    # The OnesCountMaxProblem class can be instantiated from an input file with a specified format
    def test_instantiation_from_input_file_with_specified_format(self):
        # Arrange
        input_file_path = 'input.txt'
        input_format = 'txt'

        with mocker.patch.object(OnesCountMaxProblem, '__load_from_file__', return_value=5):
            # Act
            problem = OnesCountMaxProblem.from_input_file(input_file_path, input_format)
    
        # Assert
        self.assertEqual(problem.dimension, 5)

    # The from_dimension method of OnesCountMaxProblem creates a new instance with the specified dimension
    def test_from_dimension_creates_new_instance_with_specified_dimension(self):
        # Arrange
        dim = 5
    
        # Act
        problem = OnesCountMaxProblem.from_dimension(dim)
    
        # Assert
        self.assertEqual(problem.dimension, dim)

    # Attempting to instantiate an instance of OnesCountMaxProblem with a non-integer dimension raises a TypeError
    def test_instantiation_with_non_integer_dimension_raises_type_error(self):
        # Arrange
        dim = '5'
    
        # Act & Assert
        with self.assertRaises(TypeError):
            problem = OnesCountMaxProblem(dim)

    # Attempting to instantiate an instance of OnesCountMaxProblem with a negative dimension raises a ValueError
    def test_instantiation_with_negative_dimension_raises_value_error(self):
        # Arrange
        dim = -5
    
        # Act & Assert
        with self.assertRaises(ValueError):
            problem = OnesCountMaxProblem(dim)

    # Attempting to instantiate an instance of OnesCountMaxProblem with a dimension of zero raises a ValueError
    def test_instantiation_with_zero_dimension_raises_value_error(self):
        # Arrange
        dim = 0
    
        # Act & Assert
        with self.assertRaises(ValueError):
            problem = OnesCountMaxProblem(dim)

    # Attempting to instantiate an instance of OnesCountMaxProblem from an input file with an unsupported format raises a ValueError
    def test_instantiation_from_input_file_with_unsupported_format_raises_value_error(self):
        # Arrange
        input_file_path = 'input.txt'
        input_format = 'csv'
        with mocker.patch.object(OnesCountMaxProblem, '__load_from_file__', side_effect=ValueError):
    
            # Act & Assert
            with self.assertRaises(ValueError):
                problem = OnesCountMaxProblem.from_input_file(input_file_path, input_format)

    # Attempting to instantiate an instance of OnesCountMaxProblem from an input file with a missing dimension value raises a ValueError
    def test_instantiation_from_input_file_with_missing_dimension_value_raises_value_error(self):
        # Arrange
        input_file_path = 'input.txt'
        input_format = 'txt'
        with mocker.patch.object(OnesCountMaxProblem, '__load_from_file__', return_value=None):
        
            # Act & Assert
            with self.assertRaises(ValueError):
                problem = OnesCountMaxProblem.from_input_file(input_file_path, input_format)

    # Attempting to copy an instance of OnesCountMaxProblem creates a new instance with the same properties, but which is not the same object
    def test_copy_creates_new_instance_with_same_properties_but_not_same_object(self):
        # Arrange
        dim = 5
        problem = OnesCountMaxProblem(dim)
    
        # Act
        copy_problem = problem.copy()
    
        # Assert
        self.assertIsNot(problem, copy_problem)
        self.assertEqual(problem.dimension, copy_problem.dimension)



class TestFromDimension(unittest.TestCase):

    # Can create a new instance of OnesCountMaxProblem with a specified dimension
    def test_create_instance_with_dimension(self):
        # Arrange
        dimension = 10
    
        # Act
        problem = OnesCountMaxProblem.from_dimension(dimension)
    
        # Assert
        self.assertIsInstance(problem, OnesCountMaxProblem)

    # The created instance has the correct dimension value
    def test_correct_dimension_value(self):
        # Arrange
        dimension = 10
    
        # Act
        problem = OnesCountMaxProblem.from_dimension(dimension)
    
        # Assert
        self.assertEqual(problem.dimension, dimension)

    # Raises a TypeError if dimension is not an integer
    def test_raises_type_error_if_dimension_not_integer(self):
        # Arrange
        dimension = "10"
    
        # Act & Assert
        with self.assertRaises(TypeError):
            OnesCountMaxProblem.from_dimension(dimension)

    # Raises a ValueError if dimension is less than or equal to zero
    def test_raises_value_error_if_dimension_less_than_or_equal_to_zero(self):
        # Arrange
        dimension = 0
    
        # Act & Assert
        with self.assertRaises(ValueError):
            OnesCountMaxProblem.from_dimension(dimension)


class Test__LoadFromFile__(unittest.TestCase):

    # Should read the dimension from a txt file with valid data format
    def test_read_dimension_from_txt_file(self):
        # Arrange
        file_path = "data.txt"
        data_format = "txt"
        expected_dimension = 10
    
        # Mock the open function and return a file object
        with patch('builtins.open', mock_open(read_data='10')) as mock_file:

            # Act
            dimension = OnesCountMaxProblem.__load_from_file__(file_path, data_format)
        
            # Assert
            self.assertEqual(dimension, expected_dimension)
            mock_file.assert_called_once_with(file_path, 'r')
            mock_file.return_value.readline.assert_called_once()

    # Should return an integer representing the dimension of the problem
    def test_return_dimension_as_integer(self):
        # Arrange
        file_path = "data.txt"
        data_format = "txt"
    
        # Mock the open function and return a file object
        with patch('builtins.open', mock_open(read_data='10')) as mock_file:
    
            # Act
            dimension = OnesCountMaxProblem.__load_from_file__(file_path, data_format)
        
            # Assert
            self.assertIsInstance(dimension, int)

    # Should raise a ValueError if data format is not txt
    def test_raise_value_error_if_data_format_not_txt(self):
        # Arrange
        file_path = "data.txt"
        data_format = "csv"
    
        # Act & Assert
        with self.assertRaises(ValueError):
            OnesCountMaxProblem.__load_from_file__(file_path, data_format)

    # Should raise a ValueError if loading from file produces invalid dimension
    def test_raise_value_error_if_loading_from_file_produces_invalid_dimension(self):
        # Arrange
        file_path = "data.txt"
        data_format = "txt"
    
        # Mock the open function and return a file object
        with patch('builtins.open', mock_open(read_data='invalid')) as mock_file:
    
            # Act & Assert
            with self.assertRaises(ValueError):
                OnesCountMaxProblem.__load_from_file__(file_path, data_format)