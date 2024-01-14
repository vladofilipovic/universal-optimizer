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
        control = AdditionalStatisticsControl(True, keep, max_local_optima_count)
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
            

class Test__DetermineKeepHelper__(unittest.TestCase):

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
            

class TestAddToAllSolutionCodesIfRequired(unittest.TestCase):

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
        control = AdditionalStatisticsControl(True, keep='all_solution_code')
        representation = "solution1"
        control.add_to_all_solution_codes (representation)
        # Act
        control.add_to_all_solution_codes(representation)
        # Assert
        self.assertEqual(len(control.all_solution_codes), 1)
        

class TestAddToMoreLocalOptimaIfRequired(unittest.TestCase):

    # Add a new solution to the local optima structure when it is empty
    def test_add_to_more_local_optima_empty_structure(self):
        # Arrange
        control = AdditionalStatisticsControl(True, 'more_local_optima')
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
        statistics_control = AdditionalStatisticsControl(True, 'more_local_optima')
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
        statistics_control = AdditionalStatisticsControl(True, 'more_local_optima')
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
        statistics_control = AdditionalStatisticsControl(True, 'all_solution_code')
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
        statistics_control = AdditionalStatisticsControl(True, 'more_local_optima')
        solution_to_add_rep = 123
        solution_to_add_fitness = 0.8
        best_solution_rep = "best_solution"
        # Act & Assert
        with self.assertRaises(TypeError):
            statistics_control.add_to_more_local_optima(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)


class TestMaxLocalOptima(unittest.TestCase):

    # Returns the value of the private attribute '__max_local_optima' when called.
    def test_returns_max_local_optima_value2(self):
        # Arrange
        control = AdditionalStatisticsControl(True, 'more_local_optima', max_local_optima_count=10)    
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
