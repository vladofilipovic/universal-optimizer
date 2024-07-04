
import unittest
import unittest.mock as mocker


from uo.utils.complex_counter_uniform_ascending import ComplexCounterUniformAscending


class TestComplexCounterUniformAscending(unittest.TestCase):

    # Create a new instance of ComplexCounterUniformAscending with valid integer parameters.
    def test_create_instance_with_valid_parameters(self):
        # Arrange
        number_of_counters = 4
        counter_size = 6
        # Act
        cc = ComplexCounterUniformAscending(number_of_counters, counter_size)
        # Assert
        self.assertEqual(cc.current_state(), [0, 1, 2, 3])

    # Call current_state() method to get the current state of the complex counter.
    def test_get_current_state(self):
        # Arrange
        cc = ComplexCounterUniformAscending(4, 6)
        # Act
        state = cc.current_state()
        # Assert
        self.assertEqual(state, [0, 1, 2, 3])

    # Call reset() method to reset the complex counter to its initial position.
    def test_reset_complex_counter(self):
        # Arrange
        cc = ComplexCounterUniformAscending(4, 6)
        cc.progress()
        # Act
        result = cc.reset()
        # Assert
        self.assertTrue(result)
        self.assertEqual(cc.current_state(), [0, 1, 2, 3])

    # Call progress() method to make progress to the complex counter.
    def test_make_progress(self):
        # Arrange
        cc = ComplexCounterUniformAscending(4, 6)
        # Act
        result = cc.progress()
        # Assert
        self.assertTrue(result)
        self.assertEqual(cc.current_state(), [0, 1, 2, 4])

    # Call progress() method to make progress to the complex counter.
    def test_make_progressX2(self):
        # Arrange
        cc = ComplexCounterUniformAscending(4, 6)
        # Act
        cc.progress()
        result = cc.progress()
        # Assert
        self.assertTrue(result)
        self.assertEqual(cc.current_state(), [0, 1, 2, 5])

    # Call progress() method to make progress to the complex counter.
    def test_make_progressX3(self):
        # Arrange
        cc = ComplexCounterUniformAscending(4, 6)
        # Act
        cc.progress()
        cc.progress()
        result = cc.progress()
        # Assert
        self.assertTrue(result)
        self.assertEqual(cc.current_state(), [0, 1, 3, 0])

    # Call progress() method to make progress to the complex counter.
    def test_make_progressX4(self):
        # Arrange
        cc = ComplexCounterUniformAscending(4, 6)
        # Act
        cc.progress()
        cc.progress()
        cc.progress()
        result = cc.progress()
        # Assert
        self.assertTrue(result)
        self.assertEqual(cc.current_state(), [0, 1, 3, 1])

    # Call copy() method to create a new instance of ComplexCounterUniformAscending with the same properties.
    def test_copy_complex_counter(self):
        # Arrange 
        cc = ComplexCounterUniformAscending(4, 6)
        # Act
        cc_copy = cc.copy()
        # Assert
        self.assertEqual(cc.current_state(), cc_copy.current_state())

    # Create a new instance of ComplexCounterUniformAscending with number_of_counters=0.
    def test_create_instance_with_zero_number_of_counters(self):
        # Arrange
        number_of_counters = 0
        counter_size = 6
        # Act & Assert
        with self.assertRaisesRegex(ValueError, 'number_of_counters'):
            ComplexCounterUniformAscending(number_of_counters, counter_size)

    # Create a new instance of ComplexCounterUniformAscending with counter_size=0.
    def test_create_instance_with_zero_counter_size(self):
        # Arrange
        number_of_counters = 4
        counter_size = 0
        # Act & Assert
        with self.assertRaisesRegex(ValueError, 'counter_size'):
            ComplexCounterUniformAscending(number_of_counters, counter_size)

    # Create a new instance of ComplexCounterUniformAscending with number_of_counters=-1.
    def test_create_instance_with_negative_number_of_counters(self):
        # Arrange
        number_of_counters = -1
        counter_size = 6
        # Act & Assert
        with self.assertRaisesRegex(ValueError, 'number_of_counters'):
            ComplexCounterUniformAscending(number_of_counters, counter_size)

    # Create a new instance of ComplexCounterUniformAscending with counter_size=-1.
    def test_create_instance_with_negative_counter_size(self):
        # Arrange
        number_of_counters = 4
        counter_size = -1
        # Act & Assert
        with self.assertRaisesRegex(ValueError, 'counter_size'):
            ComplexCounterUniformAscending(number_of_counters, counter_size)

    # Call progress() method when the complex counter has reached its maximum state.
    def test_progress_when_max_state_reached(self):
        # Arrange
        cc = ComplexCounterUniformAscending(2, 2)
        cc.progress()
        cc.progress()
        cc.progress()
        cc.progress()
        # Act
        result = cc.progress()
        # Assert
        self.assertFalse(result)
        self.assertEqual(cc.current_state(), [1, 1])

    # Create a new instance of ComplexCounterUniformAscending with number_of_counters=1.
    def test_create_instance_with_one_number_of_counters(self):
        # Arrange
        number_of_counters = 1
        counter_size = 6
        # Act
        cc = ComplexCounterUniformAscending(number_of_counters, counter_size)
        # Assert
        self.assertEqual(cc.current_state(), [0])

    # Create a new instance of ComplexCounterUniformAscending with number_of_counters=10 and counter_size=10.
    def test_create_instance_with_valid_parameters_1(self):
        # Arrange
        number_of_counters = 10
        counter_size = 10
        # Act
        cc = ComplexCounterUniformAscending(number_of_counters, counter_size)
        # Assert
        self.assertEqual(cc.current_state(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Create a new instance of ComplexCounterUniformAscending with number_of_counters=2 and counter_size=10.
    def test_create_instance_with_valid_parameters_2(self):
        # Arrange
        number_of_counters = 2
        counter_size = 10
        # Act
        cc = ComplexCounterUniformAscending(number_of_counters, counter_size)
        # Assert
        self.assertEqual(cc.current_state(), [0, 1])

    # Create a new instance of ComplexCounterUniformAscending with number_of_counters=10 and counter_size=2.
    def test_create_instance_with_valid_parameters_3(self):
        # Arrange
        number_of_counters = 10
        counter_size = 2
        # Act & Assert
        with self.assertRaisesRegex(ValueError, 'Parameter \'counter_size\' must be greater or equal to parameter \'number_of_counters\'.'):
            ComplexCounterUniformAscending(number_of_counters, counter_size)
