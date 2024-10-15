
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
        # Act & Assert
        with self.assertRaisesRegex(ValueError, 'number_of_counters'):
            ComplexCounterBitArrayFull(number_of_counters)

    # can progress the complex counter with one counters
    def test_progress_complex_counter_with_one_counter(self):
        # Arrange
        number_of_counters = 1
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        cc.progress()
        result = cc.progress()
        # Assert
        self.assertFalse(result)

    # can check if the complex counter can progress X 2 with two counters
    def test_can_progress_x_2_complex_counter_with_two_counters(self):
        # Arrange
        number_of_counters = 2
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        cc.progress()
        cc.progress()
        result = cc.can_progress()
        # Assert
        self.assertTrue(result)
        
    # can check if the complex counter can progress X 4 with two counters
    def test_can_progress_x_4_complex_counter_with_two_counters(self):
        # Arrange
        number_of_counters = 2
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        cc.progress()
        cc.progress()
        cc.progress()
        cc.progress()
        result = cc.can_progress()
        # Assert
        self.assertFalse(result)


class TestComplexCounterBitArrayFull2(unittest.TestCase):

    # can create a new instance of ComplexCounterBitArrayFull with a given number of counters
    def test_create_instance_with_given_number_of_counters(self):
        # Arrange
        number_of_counters = 3
        # Act
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Assert
        self.assertIsInstance(cc, ComplexCounterBitArrayFull)
        self.assertEqual(cc.current_state().bin, '000')

    # can get the current state of the complex counter
    def test_get_current_state(self):
        # Arrange
        number_of_counters = 3
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        current_state = cc.current_state()
        # Assert
        self.assertIsInstance(current_state, BitArray)
        self.assertEqual(current_state.bin, '000')

    # can reset the complex counter to its initial position
    def test_reset_complex_counter(self):
        # Arrange
        number_of_counters = 3
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        result = cc.reset()
        # Assert
        self.assertTrue(result)
        self.assertEqual(cc.current_state().bin, '000')

    # can progress the complex counter by one step
    def test_progress_complex_counter(self):
        # Arrange
        number_of_counters = 3
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        result = cc.progress()
        # Assert
        self.assertTrue(result)
        self.assertEqual(cc.current_state().bin, '100')

    # can check if the complex counter can progress
    def test_can_progress_complex_counter(self):
        # Arrange
        number_of_counters = 3
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        result = cc.can_progress()
        # Assert
        self.assertTrue(result)

    # raises TypeError if number_of_counters is not an integer
    def test_raises_type_error_if_number_of_counters_not_integer(self):
        # Arrange
        number_of_counters = '3'
        # Act & Assert
        with self.assertRaises(TypeError):
            ComplexCounterBitArrayFull(number_of_counters)

    # returns False when progress is called on a complex counter that has already reached its maximum value
    def test_returns_false_when_progress_called_on_counter_with_max_value(self):
        # Arrange
        number_of_counters = 3
        cc = ComplexCounterBitArrayFull(number_of_counters)
        for _ in range(8): 
            cc.progress()  
        # Act
        result = cc.progress()
        # Assert
        self.assertFalse(result)
        self.assertEqual(cc.current_state().bin, '111')

    # returns False when reset is called on a complex counter with no counters
    def test_returns_false_when_reset_called_on_counter_with_no_counters(self):
        # Arrange
        number_of_counters = 0    
        # Act & Assert
        with self.assertRaisesRegex(ValueError, 'Parameter \'number_of_counters\''):
            ComplexCounterBitArrayFull(number_of_counters)

    # can create a new instance of ComplexCounterBitArrayFull with a large number of counters
    def test_create_instance_with_large_number_of_counters(self):
        # Arrange
        number_of_counters = 1000    
        # Act
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Assert
        self.assertIsInstance(cc, ComplexCounterBitArrayFull)
        self.assertEqual(cc.current_state().bin,  '0' * number_of_counters)

    # can copy the current complex counter to a new instance
    def test_copy_complex_counter(self):
        # Arrange
        number_of_counters = 3
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Act
        cc_copy = cc.copy()
        # Assert
        self.assertIsInstance(cc_copy, ComplexCounterBitArrayFull)
        self.assertEqual(cc_copy.current_state().bin, cc.current_state().bin)

    # can create a new instance of ComplexCounterBitArrayFull with a single counter
    def test_create_instance_with_single_counter(self):
        # Arrange
        number_of_counters = 1
        # Act
        cc = ComplexCounterBitArrayFull(number_of_counters)
        # Assert
        self.assertIsInstance(cc, ComplexCounterBitArrayFull)
        self.assertEqual(cc.current_state().bin, '0')

    # can create a new instance of ComplexCounterBitArrayFull with a counter of size 2
    def test_create_instance_with_counter_size_2(self):
        # Arrange
        number_of_counters = 2
        # Act
        cc = ComplexCounterBitArrayFull(number_of_counters)
        cc.progress()
        # Assert
        self.assertIsInstance(cc, ComplexCounterBitArrayFull)
        self.assertEqual(cc.current_state().bin, '10')

    # can create a new instance of ComplexCounterBitArrayFull with a counter of size 3
    def test_create_instance_with_counter_size_3(self):
        # Arrange
        number_of_counters = 3
        # Act
        cc = ComplexCounterBitArrayFull(number_of_counters)
        cc.progress()
        # Assert
        self.assertIsInstance(cc, ComplexCounterBitArrayFull)
        self.assertEqual(cc.current_state().bin, '100')