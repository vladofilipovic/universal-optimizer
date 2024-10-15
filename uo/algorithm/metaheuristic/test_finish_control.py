import unittest   
import unittest.mock as mocker

from uo.algorithm.metaheuristic.finish_control import FinishControl

class TestFinishControl(unittest.TestCase):

    # Creating a new instance of FinishControl with valid parameters should set the specified criteria and properties correctly.
    def test_valid_parameters(self):
        # Arrange
        criteria = 'evaluations & iterations & seconds'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        # Act
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        # Assert
        self.assertEqual(finish_control.criteria, criteria)
        self.assertEqual(finish_control.evaluations_max, evaluations_max)
        self.assertEqual(finish_control.iterations_max, iterations_max)
        self.assertEqual(finish_control.seconds_max, seconds_max)

    # Copying an instance of FinishControl should create a new instance with the same properties.
    def test_copy(self):
        # Arrange
        criteria = 'evaluations & iterations & seconds'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        # Act
        copied_finish_control = finish_control.copy()
        # Assert
        self.assertIsNot(finish_control, copied_finish_control)
        self.assertEqual(finish_control.criteria, copied_finish_control.criteria)
        self.assertEqual(finish_control.evaluations_max, copied_finish_control.evaluations_max)
        self.assertEqual(finish_control.iterations_max, copied_finish_control.iterations_max)
        self.assertEqual(finish_control.seconds_max, copied_finish_control.seconds_max)

    # Calling is_finished() with values within the specified criteria should return False.
    def test_is_finished_within_criteria(self):
        # Arrange
        criteria = 'evaluations & iterations & seconds'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        evaluation = 50
        iteration = 100
        elapsed_seconds = 150.0
        # Act
        result = finish_control.is_finished(evaluation, iteration, elapsed_seconds)
        # Assert
        self.assertFalse(result)

    # Calling is_finished() with values outside the specified criteria should return True.
    def test_is_finished_outside_criteria(self):
        # Arrange
        criteria = 'evaluations & iterations & seconds'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        evaluation = 150
        iteration = 250
        elapsed_seconds = 350.0
        # Act
        result = finish_control.is_finished(evaluation, iteration, elapsed_seconds)
        # Assert
        self.assertTrue(result)

    # Getting the string representation of an instance of FinishControl should return a string with the correct format.
    def test_string_representation(self):
        # Arrange
        criteria = 'evaluations_max & iterations_max & seconds_max'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        expected_string = "|criteria=evaluations & iterations & seconds|evaluations_max=100|iterations_max=200|seconds_max=300.0"

        # Act
        result = str(finish_control)

        # Assert
        self.assertEqual(result, expected_string)

    # Creating a new instance of FinishControl with invalid parameters should raise the correct TypeError or ValueError.
    def test_invalid_parameters(self):
        # Arrange
        criteria = 'evaluations_max & iterations_max & seconds_max'
        evaluations_max = '100'
        iterations_max = 200
        seconds_max = 300.0

        # Act & Assert
        with self.assertRaises(TypeError):
            FinishControl(criteria, evaluations_max, iterations_max, seconds_max)

    # Creating a new instance of FinishControl with no criteria specified should raise a ValueError.
    def test_no_criteria_specified(self):
        # Arrange
        criteria = None
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        # Act & Assert
        with self.assertRaises(TypeError):
            FinishControl(criteria, evaluations_max, iterations_max, seconds_max)

    # Copying an instance of FinishControl and modifying the properties of the copy should not modify the original instance.
    def test_copy_instance(self):
        # Arrange
        criteria = 'evaluations & iterations & seconds'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        # Act
        copied_control = finish_control.copy()
        copied_control.criteria = 'evaluations & iterations'
        # Assert
        self.assertNotEqual(finish_control.criteria, copied_control.criteria)

    # Getting the string representation of an instance of FinishControl with custom indentation and delimiter should return a string with the correct format.
    def test_string_representation(self):
        # Arrange
        criteria = 'evaluations & iterations & seconds'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        # Act
        string_rep = finish_control.string_rep('|', indentation=2, indentation_symbol='-', group_start='[', group_end=']')
        # Assert
        expected_string_rep = '|--[' \
                             '|--criteria=evaluations & iterations & seconds|--evaluations_max=100' \
                             '|--iterations_max=200|--seconds_max=300.0|--]'
        self.assertEqual(string_rep, expected_string_rep)

    # Changing the criteria property of an instance of FinishControl should update the check_* properties accordingly.
    def test_change_criteria(self):
        # Arrange
        criteria = 'evaluations & iterations & seconds '
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        # Act
        finish_control.criteria = 'evaluations & seconds'
        # Assert
        self.assertTrue(finish_control.check_evaluations)
        self.assertFalse(finish_control.check_iterations)
        self.assertTrue(finish_control.check_seconds)

    # Creating a new instance of FinishControl with a criteria that contains an invalid value should raise a ValueError.
    def test_invalid_criteria(self):
        # Arrange
        criteria = 'evaluations_max & invalid_value'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0

        # Act & Assert
        with self.assertRaises(ValueError):
            finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)

    # Creating a new instance of FinishControl with a criteria that contains duplicate values should set the corresponding check_* property to True only once.
    def test_duplicate_criteria(self):
        # Arrange
        criteria = 'evaluations & evaluations & seconds'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        # Act
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        # Assert
        self.assertTrue(finish_control.check_evaluations)
        self.assertFalse(finish_control.check_iterations)
        self.assertTrue(finish_control.check_seconds)

    # Creating a new instance of FinishControl with a criteria that contains only one value should set the corresponding check_* property to True and the others to False.
    def test_single_criteria(self):
        # Arrange
        criteria = 'evaluations'
        evaluations_max = 100
        iterations_max = 200
        seconds_max = 300.0
        # Act
        finish_control = FinishControl(criteria, evaluations_max, iterations_max, seconds_max)
        # Assert
        self.assertTrue(finish_control.check_evaluations)
        self.assertFalse(finish_control.check_iterations)
        self.assertFalse(finish_control.check_seconds)
