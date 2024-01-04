
import sys
import unittest   
import unittest.mock as mocker

from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl


class Test__Init_22(unittest.TestCase):

    # Creates a new instance of AdditionalStatisticsControl with default values.
    def test_default_values(self):
        # Arrange
        # Act
        statistics_control = AdditionalStatisticsControl()
        # Assert
        self.assertEqual(statistics_control.keep, "")
        self.assertEqual(statistics_control.max_local_optima, 10)

    # Creates a new instance of AdditionalStatisticsControl with valid input values.
    def test_valid_input_values(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima = 5
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima, 5)

    # Creates a new instance of AdditionalStatisticsControl with the maximum value for max_local_optima.
    def test_maximum_max_local_optima(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima = sys.maxsize
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima, sys.maxsize)

    # Creates a new instance of AdditionalStatisticsControl with the minimum value for max_local_optima.
    def test_minimum_max_local_optima(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima = 0
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima, 0)

    # Creates a new instance of AdditionalStatisticsControl with a valid string for keep.
    def test_valid_string_keep(self):
        # Arrange
        keep = "all_solution_code"
        max_local_optima = 5
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code")
        self.assertEqual(statistics_control.max_local_optima, 5)

    # Creates a new instance of AdditionalStatisticsControl with an empty string for keep.
    def test_empty_string_keep(self):
        # Arrange
        keep = ""
        max_local_optima = 5
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, "")
        self.assertEqual(statistics_control.max_local_optima, 5)

    # Raises a TypeError if keep is not a string.
    def test_keep_not_string(self):
        # Arrange
        keep = 123
        max_local_optima = 5
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(keep, max_local_optima)

    # Raises a TypeError if max_local_optima is not an integer.
    def test_max_local_optima_not_integer(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima = 5.5
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(keep, max_local_optima)

    # Raises a ValueError if max_local_optima is less than zero.
    def test_max_local_optima_less_than_zero(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima = -1
        # Act & Assert
        with self.assertRaises(ValueError):
            AdditionalStatisticsControl(keep, max_local_optima)

    # Creates a new instance of AdditionalStatisticsControl with valid parameters and keep parameter set to 'more_local_optima'.
    def test_keep_more_local_optima(self):
        # Arrange
        keep = 'more_local_optima'
        max_local_optima = 10
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, 'more_local_optima')
        self.assertEqual(statistics_control.max_local_optima, 10)

    # Creates a new instance of AdditionalStatisticsControl with valid parameters and keep parameter set to 'all_solution_code, more_local_optima'.
    def test_keep_all_solution_code_and_more_local_optima(self):
        # Arrange
        keep = 'all_solution_code, more_local_optima'
        max_local_optima = 10
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, 'all_solution_code, more_local_optima')
        self.assertEqual(statistics_control.max_local_optima, 10)

    # Creates a new instance of AdditionalStatisticsControl with valid parameters and max_local_optima set to 0.
    def test_max_local_optima_zero(self):
        # Arrange
        keep = ''
        max_local_optima = 0
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, '')
        self.assertEqual(statistics_control.max_local_optima, 0)

    # Creates a new instance of AdditionalStatisticsControl with a string containing only whitespace for keep.
    def test_whitespace_keep(self):
        # Arrange
        keep = " "
        # Act
        statistics_control = AdditionalStatisticsControl(keep=keep)
        # Assert
        self.assertEqual(statistics_control.keep, "")
        self.assertEqual(statistics_control.max_local_optima, 10)

    # Creates a new instance of AdditionalStatisticsControl with a string containing an invalid value for keep.
    def test_invalid_keep(self):
        # Arrange
        keep = "invalid_value"
        # Act & Assert
        with self.assertRaises(ValueError):
            statistics_control = AdditionalStatisticsControl(keep=keep)

    # Creates a new instance of AdditionalStatisticsControl with a string containing multiple valid values for keep.
    def test_multiple_valid_keep(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        # Act
        statistics_control = AdditionalStatisticsControl(keep=keep)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima, 10)

    # Creates a new instance of AdditionalStatisticsControl with a string containing multiple valid and invalid values for keep.
    def test_valid_and_invalid_values_for_keep(self):
        # Arrange
        keep = "all_solution_code, more_local_optima, invalid_value"
        max_local_optima = 10
        # Act
        with self.assertRaises(ValueError):
            statistics_control = AdditionalStatisticsControl(keep, max_local_optima)

    # Creates a new instance of AdditionalStatisticsControl with a very large value for max_local_optima.
    def test_large_value_for_max_local_optima(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima = sys.maxsize
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima, sys.maxsize)

    # Creates a new instance of AdditionalStatisticsControl with a very small value for max_local_optima.
    def test_small_value_for_max_local_optima(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima = 5
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima, max_local_optima)
        
class TestMaxLocalOptima(unittest.TestCase):

    # Returns the value of the private attribute '__max_local_optima' when called.
    def test_returns_max_local_optima_value(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code, more_local_optima', max_local_optima=5)    
        # Act
        result = control.max_local_optima
        # Assert
        self.assertEqual(result, 5)

    # Returns an integer value.
    def test_returns_integer_value(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code, more_local_optima', max_local_optima=5)
        # Act
        result = control.max_local_optima
        # Assert
        self.assertIsInstance(result, int)

    # Raises a TypeError when 'max_local_optima' is not an integer.
    def test_raises_type_error_when_max_local_optima_not_integer(self):
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(keep='all_solution_code, more_local_optima', max_local_optima='5')
            

class TestKeepAllSolutionCodes(unittest.TestCase):

    # Returns a boolean indicating if all solution codes should be kept
    def test_returns_boolean_indicating_if_all_solution_codes_should_be_kept(self):
        # Arrange
        control = AdditionalStatisticsControl()
        # Act
        result = control.keep_all_solution_codes
        # Assert
        self.assertIsInstance(result, bool)

    # Returns True if all solution codes should be kept
    def test_returns_true_if_all_solution_codes_should_be_kept(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code')
        # Act
        result = control.keep_all_solution_codes
        # Assert
        self.assertTrue(result)

    # Raises a TypeError if the representation parameter is not a string
    def test_raises_type_error_if_representation_parameter_is_not_string(self):
        # Arrange
        control = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(TypeError):
            control.add_to_all_solution_codes_if_required(123)

    # Raises an AttributeError if the keep_all_solution_codes property is not a boolean
    def test_raises_attribute_error_if_keep_all_solution_codes_property_is_not_boolean(self):
        # Arrange
        control = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(AttributeError):
            control.keep_all_solution_codes = 'True'
            

class TestKeepMoreLocalOptima(unittest.TestCase):

    # Returns False if keep_more_local_optima is False.
    def test_returns_false_if_keep_more_local_optima_is_false(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl()
        # Act
        result = statistics_control.keep_more_local_optima
        # Assert
        self.assertFalse(result)

    # Returns False if solution_to_add_rep is already in more_local_optima.
    def test_returns_false_if_solution_to_add_rep_is_already_in_more_local_optima(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 0.5
        best_solution_rep = "best_solution"
        # Add solution_to_add_rep to more_local_optima
        statistics_control.more_local_optima[solution_to_add_rep] = solution_to_add_fitness
        # Act
        result = statistics_control.add_to_more_local_optima_if_required(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertFalse(result)

    # Raises TypeError if solution_to_add_rep is not a string.
    def test_raises_type_error_if_solution_to_add_rep_is_not_a_string(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = 123
        solution_to_add_fitness = 0.5
        best_solution_rep = "best_solution"
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima_if_required(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)

    # Raises TypeError if best_solution_rep is not a string.
    def test_raises_type_error_if_best_solution_rep_is_not_a_string(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = "fitness"
        best_solution_rep = "best_solution"
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima_if_required(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
            
    # Raises TypeError if solution_to_add_fitness is not a float or list of floats.
    def test_raises_type_error_if_solution_to_add_fitness_is_not_a_float_or_float_list(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = "fitness"
        best_solution_rep = 42
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima_if_required(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
            

class TestAllSolutionCodes(unittest.TestCase):

    # Setting a non-empty set of solution codes should update the __all_solution_codes attribute
    def test_set_non_empty_solution_codes(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl()
        solution_codes = {'code1', 'code2', 'code3'}
        # Act
        statistics_control.all_solution_codes = solution_codes
        # Assert
        self.assertEqual(statistics_control.all_solution_codes, solution_codes)

    # Setting an empty set of solution codes should not update the __all_solution_codes attribute
    def test_set_empty_solution_codes(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl()
        solution_codes = set()
        # Act
        statistics_control.all_solution_codes = solution_codes
        # Assert
        self.assertEqual(statistics_control.all_solution_codes, set())

    # Setting a set of solution codes with duplicate values should update the __all_solution_codes attribute with only unique values
    def test_set_duplicate_solution_codes(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl()
        solution_codes = {'code1', 'code2', 'code2', 'code3'}
        # Act
        statistics_control.all_solution_codes = solution_codes
        # Assert
        self.assertEqual(statistics_control.all_solution_codes, {'code1', 'code2', 'code3'})

    # Setting the all_solution_codes property with a None value should raise a TypeError
    def test_set_all_solution_codes_with_none_value(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.all_solution_codes = None

    # Setting the all_solution_codes property with a non-set value should raise a TypeError
    def test_set_all_solution_codes_with_non_set_value(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.all_solution_codes = "solution_codes"


class TestMoreLocalOptima(unittest.TestCase):

    # Setting a new dictionary of local optima with valid input should update the __more_local_optima attribute
    def test_valid_input_updates_attribute(self):
        # Arrange
        additional_stats = AdditionalStatisticsControl()
        new_local_optima = {'solution1': 0.5, 'solution2': [0.3, 0.4]}
        # Act
        additional_stats.more_local_optima = new_local_optima
        # Assert
        self.assertEqual(additional_stats.more_local_optima, new_local_optima)

    # Setting an empty dictionary of local optima should update the __more_local_optima attribute to an empty dictionary
    def test_empty_input_updates_attribute(self):
        # Arrange
        additional_stats = AdditionalStatisticsControl()
        # Act
        additional_stats.more_local_optima = {}
        # Assert
        self.assertEqual(additional_stats.more_local_optima, {})

    # Setting the __more_local_optima attribute to None should update it to an empty dictionary
    def test_none_input_updates_attribute(self):
        # Arrange
        additional_stats = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(TypeError):
            additional_stats.more_local_optima = None

    # Setting a new dictionary of local optima with more than max_local_optima elements should remove the oldest element
    def test_max_local_optima_elements_removes_oldest_element(self):
        # Arrange
        additional_stats = AdditionalStatisticsControl('more_local_optima', max_local_optima=2)
        additional_stats.more_local_optima = {'solution1': 0.5, 'solution2': [0.3, 0.4]}
        new_local_optima = {'solution3': 0.6}
        # Act
        success = additional_stats.add_to_more_local_optima_if_required('solution3', 0.6, 'solution1')
        # Assert
        self.assertTrue(success)
        self.assertEqual(len(additional_stats.more_local_optima), 2)
        self.assertIn('solution3', additional_stats.more_local_optima.keys())

    # Setting the __more_local_optima attribute to an empty dictionary when keep_more_local_optima is False should not update the attribute
    def test_empty_input_does_not_update_attribute_when_keep_more_local_optima_is_false(self):
        # Arrange
        additional_stats = AdditionalStatisticsControl(keep='all_solution_code')
        # Act
        additional_stats.more_local_optima = {}
        # Assert
        self.assertEqual(additional_stats.more_local_optima, {})