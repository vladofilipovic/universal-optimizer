import sys
import unittest   
import unittest.mock as mocker

from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

class TestAdditionalStatisticsControl(unittest.TestCase):

    # Creating an instance of AdditionalStatisticsControl with valid parameters should initialize all properties correctly.
    def test_valid_parameters_initialization(self):
        # Arrange
        keep = 'all_solution_code'
        max_local_optima_count = 10
        # Act
        control = AdditionalStatisticsControl(keep=keep, 
                            max_local_optima_count=max_local_optima_count)
        # Assert
        self.assertEqual(control.keep_all_solution_codes, True)
        self.assertEqual(control.keep_more_local_optima, False)
        self.assertEqual(control.max_local_optima_count, max_local_optima_count)

    # Setting the 'keep' property with valid values should update the 'keep_all_solution_codes' and 'keep_more_local_optima' properties correctly.
    def test_valid_keep_property_update(self):
        # Arrange
        control = AdditionalStatisticsControl()
        # Act
        control.keep = 'all_solution_code'
        # Assert
        self.assertEqual(control.keep_all_solution_codes, True)
        self.assertEqual(control.keep_more_local_optima, False)
        # Act
        control.keep = 'more_local_optima'
        # Assert
        self.assertEqual(control.keep_all_solution_codes, False)
        self.assertEqual(control.keep_more_local_optima, True)    
        # Act
        control.keep = 'all_solution_code, more_local_optima'
        # Assert
        self.assertEqual(control.keep_all_solution_codes, True)
        self.assertEqual(control.keep_more_local_optima, True)

    # Calling 'add_to_all_solution_codes' with 'keep_all_solution_codes' set to True should add the solution representation to the 'all_solution_codes' set.
    def test_add_to_all_solution_codes_if_required(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code')
        representation = 'solution_representation'
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertIn(representation, control.all_solution_codes)

    # Calling 'add_to_more_local_optima' with 'keep_more_local_optima' set to True and a new solution representation should add the solution to the 'more_local_optima' dictionary.
    def test_add_to_more_local_optima_new_solution(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='more_local_optima')
        solution_to_add_rep = 'solution_representation'
        solution_to_add_fitness = 0.5
        best_solution_rep = 'best_solution_representation'
        # Act
        result = control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertTrue(result)
        self.assertIn(solution_to_add_rep, control.more_local_optima)
        self.assertEqual(control.more_local_optima[solution_to_add_rep], solution_to_add_fitness)

    # Calling 'add_to_more_local_optima' with 'keep_more_local_optima' set to True and an existing solution representation should not add the solution to the 'more_local_optima' dictionary.
    def test_add_to_more_local_optima_existing_solution(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='more_local_optima')
        solution_to_add_rep = 'solution_representation'
        solution_to_add_fitness = 0.5
        best_solution_rep = 'best_solution_representation'
        control.more_local_optima[solution_to_add_rep] = solution_to_add_fitness
        # Act
        result = control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertFalse(result)
        self.assertIn(solution_to_add_rep, control.more_local_optima)
        self.assertEqual(control.more_local_optima[solution_to_add_rep], solution_to_add_fitness)

    # Creating an instance of AdditionalStatisticsControl with invalid 'keep' parameter should raise a TypeError.
    def test_invalid_keep_parameter_type(self):
        # Arrange
        keep = 123
        max_local_optima_count = 10
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(True, keep, max_local_optima_count)

    # Creating an instance of AdditionalStatisticsControl with invalid 'max_local_optima_count' parameter should raise a TypeError.
    def test_invalid_max_local_optima_parameter_type(self):
        # Arrange
        keep = 'all_solution_code, more_local_optima'
        max_local_optima_count = '10'
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(True, keep, max_local_optima_count)

    # Setting the 'keep' property with invalid values should raise a ValueError.
    def test_invalid_keep_property_value(self):
        # Arrange
        control = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(ValueError):
            control.keep = 'invalid_value'
            

class Test__DetermineKeepHelper__999(unittest.TestCase):

    # Determines which criteria should be checked during execution
    def test_determine_keep_helper_criteria_checked(self):
        # Arrange
        keep = 'all_solution_code, more_local_optima'
        obj = AdditionalStatisticsControl()
        # Act
        obj.__determine_keep_helper__(keep)
        # Assert
        self.assertTrue(obj.keep_all_solution_codes)
        self.assertTrue(obj.keep_more_local_optima)

    # Sets the 'keep_all_solution_codes' and 'keep_more_local_optima' flags to False by default
    def test_determine_keep_helper_flags_default(self):
        # Arrange
        obj = AdditionalStatisticsControl()
        # Act
        # Assert
        self.assertFalse(obj.keep_all_solution_codes)
        self.assertFalse(obj.keep_more_local_optima)

    # Parses the 'keep' parameter and sets the corresponding flags to True
    def test_determine_keep_helper_parse_keep_parameter3(self):
        # Arrange
        keep = 'all_solution_code, more_local_optima'
        obj = AdditionalStatisticsControl()
        # Act
        obj.__determine_keep_helper__(keep)
        # Assert
        self.assertTrue(obj.keep_all_solution_codes)
        self.assertTrue(obj.keep_more_local_optima)

    # Raises a TypeError if the 'keep' parameter is not a string
    def test_determine_keep_helper_keep_not_string(self):
        # Arrange
        keep = 123
        obj = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(TypeError):
            obj.__determine_keep_helper__(keep)

    # Raises a TypeError if the 'max_local_optima_count' parameter is not an integer
    def test_determine_keep_helper_max_local_optima_not_integer(self):
        # Arrange
        keep = 'all_solution_code, more_local_optima'
        max_local_optima_count = '10'
        obj = AdditionalStatisticsControl()
    
        # Act & Assert
        with self.assertRaises(TypeError):
            obj.__determine_keep_helper__(keep, max_local_optima_count)

    # Raises a ValueError if the 'keep' parameter contains an invalid value
    def test_determine_keep_helper_invalid_value(self):
        # Arrange
        keep = 'invalid_value'
        obj = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(ValueError):
            obj.__determine_keep_helper__(keep)
            

class TestAddToAllSolutionCodesIfRequired998(unittest.TestCase):

    # If keep_all_solution_codes is False, do not add the representation to all_solution_codes.
    def test_keep_all_solution_codes_false(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='more_local_optima')
        representation = "solution1"
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertNotIn(representation, control.all_solution_codes)

    # If keep_all_solution_codes is True, add the representation to all_solution_codes.
    def test_keep_all_solution_codes_true(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code')
        representation = "solution1"
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertIn(representation, control.all_solution_codes)

    # If all_solution_codes is empty, add the representation to all_solution_codes.
    def test_all_solution_codes_empty2(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code')
        representation = "solution1"
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertIn(representation, control.all_solution_codes)

    # If representation is not a string, raise a TypeError.
    def test_representation_not_string(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code')
        representation = 123
        # Act & Assert
        with self.assertRaises(TypeError):
            control.add_to_all_solution_codes(representation)

    # If all_solution_codes is not a set, raise an AttributeError.
    def test_all_solution_codes_not_set(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='more_local_optima')
        representation = "solution1"
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertEqual(len(control.all_solution_codes), 0)
        

    # If all_solution_codes already contains the representation, do not add it again.
    def test_representation_already_in_all_solution_codes(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code')
        representation = "solution1"
        control.add_to_all_solution_codes (representation)
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertEqual(len(control.all_solution_codes), 1)
        

class TestAddToMoreLocalOptimaIfRequired997(unittest.TestCase):

    # Add a new solution to the local optima structure when it is empty
    def test_add_to_more_local_optima_empty_structure(self):
        # Arrange
        control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 0.8
        best_solution_rep = "best_solution"
        # Act
        result = control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertTrue(result)
        self.assertEqual(len(control.more_local_optima), 1)
        self.assertEqual(control.more_local_optima[solution_to_add_rep], solution_to_add_fitness)

    # Add a new solution to the local optima structure when it is not full
    def test_add_to_more_local_optima_not_full_structure(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 0.8
        best_solution_rep = "best_solution"
        statistics_control.add_to_more_local_optima("existing_solution", 0.5, "existing solution")
        # Act
        result = statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertTrue(result)
        self.assertEqual(len(statistics_control.more_local_optima), 2)
        self.assertEqual(statistics_control.more_local_optima[solution_to_add_rep], solution_to_add_fitness)

    # Add a new solution to the local optima structure when it is full but the new solution is better than at least one of the existing ones
    def test_add_to_more_local_optima_full_structure_new_solution_better(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 0.8
        best_solution_rep = "best_solution"
        statistics_control.add_to_more_local_optima("existing_solution1", 0.5, "existing_solution1")
        statistics_control.add_to_more_local_optima("existing_solution2", 0.6, "existing_solution1")
        # Act
        result = statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertTrue(result)
        self.assertEqual(len(statistics_control.more_local_optima), 3)
        self.assertEqual(statistics_control.more_local_optima[solution_to_add_rep], solution_to_add_fitness)

    # Return False when the keep_more_local_optima property is False
    def test_add_to_more_local_optima_keep_more_local_optima_false(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl()
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 0.8
        best_solution_rep = "best_solution"
        # Act
        result = statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertFalse(result)
        self.assertEqual(len(statistics_control.more_local_optima), 0)

    # Return False when the keep_more_local_optima property is False
    def test_add_to_more_local_optima_keep_more_local_optima_false2(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('all_solution_code')
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 0.8
        best_solution_rep = "best_solution"
        # Act
        result = statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertFalse(result)
        self.assertEqual(len(statistics_control.more_local_optima), 0)

    # Return False when the solution_to_add_rep parameter is not a string
    def test_add_to_more_local_optima_solution_to_add_rep_not_string(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = 123
        solution_to_add_fitness = 0.8
        best_solution_rep = "best_solution"
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)


class TestMaxLocalOptima996(unittest.TestCase):

    # Returns the value of the private attribute '__max_local_optima' when called.
    def test_returns_max_local_optima_value2(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='more_local_optima', 
                            max_local_optima_count=10)    
        # Act
        result = control.max_local_optima_count
        # Assert
        self.assertEqual(result, 10)

    # Returns an integer value.
    def test_returns_integer_value(self):
        # Arrange
        control = AdditionalStatisticsControl(max_local_optima_count=12)
        # Act
        result = control.max_local_optima_count
        # Assert
        self.assertIsInstance(result, int)

    # The value returned is the maximum number of local optima that will be kept.
    def test_returns_maximum_number_of_local_optima(self):
        # Arrange
        control = AdditionalStatisticsControl(max_local_optima_count=12)
        # Act
        result = control.max_local_optima_count
        # Assert
        self.assertEqual(result, 12)

    # Raises a TypeError if the value of the attribute '__max_local_optima' is not an integer.
    def test_raises_type_error_if_max_local_optima_not_integer(self):
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(max_local_optima_count='10')

    # The value of the attribute '__max_local_optima' can be zero.
    def test_max_local_optima_can_be_zero(self):
        # Arrange
        control = AdditionalStatisticsControl(max_local_optima_count=0)
        # Act
        result = control.max_local_optima_count
        # Assert
        self.assertEqual(result, 0)

    # The value of the attribute '__max_local_optima' can be negative.
    def test_max_local_optima_can_not_be_negative(self):
        # Act & Assert
        with self.assertRaises(ValueError):
            AdditionalStatisticsControl(max_local_optima_count=-10)


class TestInit995(unittest.TestCase):

    # Creates a new instance of AdditionalStatisticsControl with default values.
    def test_default_values(self):
        # Arrange
        # Act
        statistics_control = AdditionalStatisticsControl()
        # Assert
        self.assertEqual(statistics_control.keep, "")
        self.assertEqual(statistics_control.max_local_optima_count, 10)

    # Creates a new instance of AdditionalStatisticsControl with valid input values.
    def test_valid_input_values(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima_count = 5
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima_count, 5)

    # Creates a new instance of AdditionalStatisticsControl with the maximum value for max_local_optima_count.
    def test_maximum_max_local_optima_count(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima_count = sys.maxsize
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima_count, sys.maxsize)

    # Creates a new instance of AdditionalStatisticsControl with the minimum value for max_local_optima_count.
    def test_minimum_max_local_optima_count(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima_count = 0
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima_count, 0)

    # Creates a new instance of AdditionalStatisticsControl with a valid string for keep.
    def test_valid_string_keep(self):
        # Arrange
        keep = "all_solution_code"
        max_local_optima_count = 5
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code")
        self.assertEqual(statistics_control.max_local_optima_count, 5)

    # Creates a new instance of AdditionalStatisticsControl with an empty string for keep.
    def test_empty_string_keep(self):
        # Arrange
        keep = ""
        max_local_optima_count = 5
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, "")
        self.assertEqual(statistics_control.max_local_optima_count, 5)

    # Raises a TypeError if keep is not a string.
    def test_keep_not_string(self):
        # Arrange
        keep = 123
        max_local_optima_count = 5
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(keep, max_local_optima_count)

    # Raises a TypeError if max_local_optima_count is not an integer.
    def test_max_local_optima_not_integer(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima_count = 5.5
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(keep, max_local_optima_count)

    # Raises a ValueError if max_local_optima_count is less than zero.
    def test_max_local_optima_less_than_zero(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima_count = -1
        # Act & Assert
        with self.assertRaises(ValueError):
            AdditionalStatisticsControl(keep, max_local_optima_count)

    # Creates a new instance of AdditionalStatisticsControl with valid parameters and keep parameter set to 'more_local_optima'.
    def test_keep_more_local_optima(self):
        # Arrange
        keep = 'more_local_optima'
        max_local_optima_count = 10
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, 'more_local_optima')
        self.assertEqual(statistics_control.max_local_optima_count, 10)

    # Creates a new instance of AdditionalStatisticsControl with valid parameters and keep parameter set to 'all_solution_code, more_local_optima'.
    def test_keep_all_solution_code_and_more_local_optima(self):
        # Arrange
        keep = 'all_solution_code, more_local_optima'
        max_local_optima_count = 10
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, 'all_solution_code, more_local_optima')
        self.assertEqual(statistics_control.max_local_optima_count, 10)

    # Creates a new instance of AdditionalStatisticsControl with valid parameters and max_local_optima_count set to 0.
    def test_max_local_optima_zero(self):
        # Arrange
        keep = ''
        max_local_optima_count = 0
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, '')
        self.assertEqual(statistics_control.max_local_optima_count, 0)

    # Creates a new instance of AdditionalStatisticsControl with a string containing only whitespace for keep.
    def test_whitespace_keep(self):
        # Arrange
        keep = " "
        # Act
        statistics_control = AdditionalStatisticsControl(keep=keep)
        # Assert
        self.assertEqual(statistics_control.keep, "")
        self.assertEqual(statistics_control.max_local_optima_count, 10)

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
        self.assertEqual(statistics_control.max_local_optima_count, 10)

    # Creates a new instance of AdditionalStatisticsControl with a string containing multiple valid and invalid values for keep.
    def test_valid_and_invalid_values_for_keep(self):
        # Arrange
        keep = "all_solution_code, more_local_optima, invalid_value"
        max_local_optima_count = 10
        # Act
        with self.assertRaises(ValueError):
            statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)

    # Creates a new instance of AdditionalStatisticsControl with a very large value for max_local_optima_count.
    def test_large_value_for_max_local_optima(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima_count = sys.maxsize
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima_count, sys.maxsize)

    # Creates a new instance of AdditionalStatisticsControl with a very small value for max_local_optima_count.
    def test_small_value_for_max_local_optima(self):
        # Arrange
        keep = "all_solution_code, more_local_optima"
        max_local_optima_count = 5
        # Act
        statistics_control = AdditionalStatisticsControl(keep, max_local_optima_count)
        # Assert
        self.assertEqual(statistics_control.keep, "all_solution_code, more_local_optima")
        self.assertEqual(statistics_control.max_local_optima_count, max_local_optima_count)
        
class TestMaxLocalOptima994(unittest.TestCase):

    # Returns the value of the private attribute '__max_local_optima' when called.
    def test_returns_max_local_optima_value(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code, more_local_optima', max_local_optima_count=5)    
        # Act
        result = control.max_local_optima_count
        # Assert
        self.assertEqual(result, 5)

    # Returns an integer value.
    def test_returns_integer_value(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code, more_local_optima', max_local_optima_count=5)
        # Act
        result = control.max_local_optima_count
        # Assert
        self.assertIsInstance(result, int)

    # Raises a TypeError when 'max_local_optima_count' is not an integer.
    def test_raises_type_error_when_max_local_optima_not_integer(self):
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(keep='all_solution_code, more_local_optima', max_local_optima_count='5')
            

class TestKeepAllSolutionCodes993(unittest.TestCase):

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
            control.add_to_all_solution_codes(123)

    # Raises an AttributeError if the keep_all_solution_codes property is not a boolean
    def test_raises_attribute_error_if_keep_all_solution_codes_property_is_not_boolean(self):
        # Arrange
        control = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(AttributeError):
            control.keep_all_solution_codes = 'True'
            

class TestKeepMoreLocalOptima992(unittest.TestCase):

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
        result = statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
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
            statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)

    # Raises TypeError if best_solution_rep is not a string.
    def test_raises_type_error_if_best_solution_rep_is_not_a_string(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = "fitness"
        best_solution_rep = "best_solution"
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
            
    # Raises TypeError if solution_to_add_fitness is not a float or list of floats.
    def test_raises_type_error_if_solution_to_add_fitness_is_not_a_float_or_float_list(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl('more_local_optima')
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = "fitness"
        best_solution_rep = 42
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
            

class TestAllSolutionCodes991(unittest.TestCase):

    # Setting a non-empty set of solution codes should update the __all_solution_codes attribute
    def test_set_non_empty_solution_codes(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl("all_solution_code")
        solution_codes = {'code1', 'code2', 'code3'}
        # Act
        for sc in solution_codes:
            statistics_control.add_to_all_solution_codes(sc) 
        # Assert
        self.assertEqual(statistics_control.all_solution_codes, solution_codes)

    # Setting an empty set of solution codes should not update the __all_solution_codes attribute
    def test_set_empty_solution_codes(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl("all_solution_code")
        # Act & Assert
        self.assertEqual(statistics_control.all_solution_codes, set())

    # Setting a set of solution codes with duplicate values should update the __all_solution_codes attribute with only unique values
    def test_set_duplicate_solution_codes(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl("all_solution_code")
        solution_codes = {'code1', 'code2', 'code2', 'code3'}
        # Act
        for sc in solution_codes:
            statistics_control.add_to_all_solution_codes(sc) 
        # Assert
        self.assertEqual(statistics_control.all_solution_codes, {'code1', 'code2', 'code3'})

    # Setting the all_solution_codes property with a None value should raise a TypeError
    def test_set_all_solution_codes_with_none_value(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(AttributeError):
            statistics_control.all_solution_codes = None

    # Setting the all_solution_codes property with a non-set value should raise a TypeError
    def test_set_all_solution_codes_with_non_set_value(self):
        # Arrange
        statistics_control = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(AttributeError):
            statistics_control.all_solution_codes = "solution_codes"

class TestMoreLocalOptima990(unittest.TestCase):

    # Setting a new dictionary of local optima with valid input should update the __more_local_optima attribute
    def test_valid_input_updates_attribute(self):
        # Arrange
        additional_stats = AdditionalStatisticsControl("more_local_optima")
        new_local_optima = {'solution1': 0.5, 'solution2': 12}
        # Act
        for nlsk in new_local_optima.keys():
            additional_stats.add_to_more_local_optima(nlsk, new_local_optima[nlsk], "solution1") 
        # Assert
        self.assertEqual(additional_stats.more_local_optima, new_local_optima)

    # Setting the __more_local_optima attribute to None should update it to an empty dictionary
    def test_none_input_updates_attribute(self):
        # Arrange
        additional_stats = AdditionalStatisticsControl()
        # Act & Assert
        with self.assertRaises(AttributeError):
            additional_stats.more_local_optima = None

    # Setting a new dictionary of local optima with more than max_local_optima_count elements should remove the oldest element
    def test_max_local_optima_elements_removes_oldest_element(self):
        # Arrange
        additional_stats = AdditionalStatisticsControl('more_local_optima', max_local_optima_count=2)
        local_optimas = {'solution1': 0.5, 'solution2': 7}
        for nlsk in local_optimas.keys():
            additional_stats.add_to_more_local_optima(nlsk, local_optimas[nlsk], "solution1") 
        new_local_optima = {'solution3': 0.6}
        # Act
        success = additional_stats.add_to_more_local_optima('solution3', 0.6, 'solution1')
        # Assert
        self.assertTrue(success)
        self.assertEqual(len(additional_stats.more_local_optima), 2)
        self.assertIn('solution3', additional_stats.more_local_optima.keys())


class TestAddToAllSolutionCodesIfRequired989(unittest.TestCase):

    # When 'keep_all_solution_codes' is False, the method should not add the solution representation to the 'all_solution_codes' set.
    def test_keep_all_solution_codes_false(self):
        # Arrange
        representation = "solution123"
        control = AdditionalStatisticsControl(keep="")    
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertEqual(control.all_solution_codes, set())

    # When 'keep_all_solution_codes' is True, the method should add the solution representation to the 'all_solution_codes' set.
    def test_keep_all_solution_codes_true(self):
        # Arrange
        representation = "solution123"
        control = AdditionalStatisticsControl(keep="all_solution_code") 
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertEqual(control.all_solution_codes, {"solution123"})

    # When the input parameter 'representation' is an empty string, the method should not add anything to the 'all_solution_codes' set.
    def test_representation_empty_string(self):
        # Arrange
        representation = ""
        control = AdditionalStatisticsControl(keep="all_solution_code")
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertEqual(control.all_solution_codes, set())

    # When the input parameter 'representation' is a non-empty string, the method should add it to the 'all_solution_codes' set.
    def test_representation_non_empty_string(self):
        # Arrange
        representation = "solution123"
        control = AdditionalStatisticsControl(keep="all_solution_code")
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertEqual(control.all_solution_codes, {"solution123"})

    # When the input parameter 'representation' is not a string, the method should raise a TypeError.
    def test_representation_not_string(self):
        # Arrange
        representation = 123
        control = AdditionalStatisticsControl(keep="all_solution_code")
        # Act & Assert
        with self.assertRaises(TypeError):
            control.add_to_all_solution_codes(representation)

    # When the 'keep_all_solution_codes' attribute is not a boolean, the constructor should raise a TypeError.
    def test_keep_all_solution_codes_not_boolean(self):
        # Arrange & Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(keep=123)

    # When the 'all_solution_codes' attribute is not a set, the setter should raise a TypeError.
    def test_all_solution_codes_not_set(self):
        # Arrange
        control = AdditionalStatisticsControl(keep="all_solution_code")
        # Act & Assert
        with self.assertRaises(AttributeError):
            control.all_solution_codes = "solution123"

    # When the 'all_solution_codes' set already contains the input parameter 'representation', the method should not add it again.
    def test_representation_already_in_all_solution_codes(self):
        # Arrange
        representation = "solution123"
        control = AdditionalStatisticsControl(keep="all_solution_code")
        control.add_to_all_solution_codes(representation)
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertEqual(control.all_solution_codes, {"solution123"})
    

class TestAddToMoreLocalOptimaIfRequired988(unittest.TestCase):

    # Add a new solution to the local optima structure when it is not already present and the maximum number of local optima has not been reached.
    def test_add_new_solution_to_local_optima_structure(self):
        # Arrange
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 10.5
        best_solution_rep = "best_solution"
        statistics_control = AdditionalStatisticsControl("more_local_optima")
        # Act
        result = statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertTrue(result)
        self.assertEqual(statistics_control.more_local_optima[solution_to_add_rep], solution_to_add_fitness)

    # Remove a random local optima from the structure when the maximum number of local optima has been reached and the new solution is not better than the best solution so far.
    def test_remove_random_local_optima_when_max_reached(self):
        # Arrange
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 10.5
        best_solution_rep = "best_solution"
        statistics_control = AdditionalStatisticsControl("more_local_optima", max_local_optima_count=2)
        statistics_control.add_to_more_local_optima("solution2", 5.0, "solution2")
        statistics_control.add_to_more_local_optima("solution3", 7.0, "solution2")
        mocker.patch('random.choice', return_value=1)
        # Act
        result = statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertTrue(result)
        self.assertEqual(statistics_control.more_local_optima[solution_to_add_rep], solution_to_add_fitness)

    # Return True when a new solution is added to the local optima structure.
    def test_return_true_when_new_solution_added(self):
        # Arrange
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 10.5
        best_solution_rep = "best_solution"
        statistics_control = AdditionalStatisticsControl("more_local_optima")
        # Act
        result = statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
        # Assert
        self.assertTrue(result)

    # Raise a TypeError if the parameter 'solution_to_add_rep' is not a string.
    def test_raise_type_error_if_solution_to_add_rep_not_string(self):
        # Arrange
        solution_to_add_rep = 123
        solution_to_add_fitness = 10.5
        best_solution_rep = "best_solution"
        statistics_control = AdditionalStatisticsControl("more_local_optima")
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)

    # Raise a TypeError if the parameter 'solution_to_add_fitness' is not an int, float or list.
    def test_raise_type_error_if_solution_to_add_fitness_not_int_float_list(self):
        # Arrange
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = "fitness"
        best_solution_rep = "best_solution"
        statistics_control = AdditionalStatisticsControl("more_local_optima")
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)

    # Raise a TypeError if the parameter 'best_solution_rep' is not a string.
    def test_raise_type_error_if_best_solution_rep_not_string(self):
        # Arrange
        solution_to_add_rep = "solution1"
        solution_to_add_fitness = 10.5
        best_solution_rep = 123
        statistics_control = AdditionalStatisticsControl("more_local_optima")
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
            
class TestStr987(unittest.TestCase):

    # Returns a string representation of the cache control and statistics structure.
    def test_returns_string_representation(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code, more_local_optima', max_local_optima_count=5)
        # Act
        result = control.__str__()
        # Assert
        self.assertIsInstance(result, str)

    # The string representation contains the values of the 'keep' and 'use_cache_for_distance_calculation' properties.
    def test_contains_keep_and_use_cache_properties(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code, more_local_optima', max_local_optima_count=5)
        # Act
        result = control.__str__()
        # Assert
        self.assertIn('keep=', result)

    # If 'keep' is blank, the string representation does contain relevant 'keep' property.
    def test_contain_relevant_keep_property_when_keep_is_blank(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='', max_local_optima_count=5)
        # Act
        result = control.__str__()
        # Assert
        self.assertIn('|keep=|', result)

