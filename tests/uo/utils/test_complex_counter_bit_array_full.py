
import unittest
import unittest.mock as mocker

from bitstring import BitArray

from uo.utils.complex_counter_bit_array_full import ComplexCounterBitArrayFull

class TestComplexCounterBitArrayFull(unittest.TestCase):

    # can create a new instance of ComplexCounterBitArrayFull with a given number of counters
    def test_create_instance_with_given_number_of_counters(self):
        # Arrange
        number_of_counters = 6
        # Act
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Assert
        self.assertEqual(cc.current_state().bin, '000000')

    # can get the current state of the complex counter
    def test_get_current_state(self):
        # Arrange
        number_of_counters = 6
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        state = cc.current_state()
        # Assert
        self.assertIsInstance(state, BitArray)

    # can reset the complex counter to its initial position
    def test_reset_complex_counter(self):
        # Arrange
        number_of_counters = 6
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        result = cc.reset()
        # Assert
        self.assertTrue(result)
        self.assertEqual(cc.current_state().bin, '000000')

    # can progress the complex counter
    def test_progress_complex_counter(self):
        # Arrange
        number_of_counters = 6
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        result = cc.progress()
        # Assert
        self.assertTrue(result)
        self.assertEqual(cc.current_state().bin, '100000')

    # can check if the complex counter can progress
    def test_can_progress_complex_counter(self):
        # Arrange
        number_of_counters = 6
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        result = cc.can_progress()
        # Assert
        self.assertTrue(result)

    # raises TypeError if number_of_counters is not an integer
    def test_raises_type_error_if_number_of_counters_not_integer(self):
        # Arrange
        number_of_counters = '6'
        # Act & Assert
        with self.assertRaises(TypeError):
            ComplexCounterBitArrayFull(number_of_counters)

    # can create a new instance of ComplexCounterBitArrayFull with zero counters
    def test_create_instance_with_zero_counters(self):
        # Arrange
        number_of_counters = 0
        # Act
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Assert
        self.assertEqual(cc.current_state().bin, '')


    # can progress the complex counter with zero counters
    def test_progress_complex_counter_with_zero_counters(self):
        # Arrange
        number_of_counters = 0
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        result = cc.progress()
        # Assert
        self.assertFalse(result)

    # can check if the complex counter can progress with zero counters
    def test_can_progress_complex_counter_with_zero_counters(self):
        # Arrange
        number_of_counters = 0
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        result = cc.can_progress()
        # Assert
        self.assertFalse(result)