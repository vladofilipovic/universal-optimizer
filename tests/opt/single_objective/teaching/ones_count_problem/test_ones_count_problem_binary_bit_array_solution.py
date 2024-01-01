
import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from bitstring import BitArray

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution import OnesCountProblemBinaryBitArraySolution
from uo.target_problem.target_problem import TargetProblem
from uo.target_problem.target_problem_void import TargetProblemVoid
from uo.target_solution.target_solution import TargetSolution


class TestOnesCountProblemBinaryBitArraySolution(unittest.TestCase):

    # Initialize a new instance of OnesCountProblemBinaryBitArraySolution with default parameters and verify that all properties are set correctly.
    def test_initialize_instance_with_default_parameters(self):
        # Arrange
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act

        # Assert
        self.assertEqual(solution.name, "OnesCountProblemBinaryBitArraySolution")
        self.assertIsNone(solution.fitness_value)
        self.assertIsNone(solution.fitness_values)
        self.assertIsNone(solution.objective_value)
        self.assertIsNone(solution.objective_values)
        self.assertFalse(solution.is_feasible)
        self.assertFalse(TargetSolution.evaluation_cache_cs.is_caching)
        self.assertEqual(TargetSolution.evaluation_cache_cs.max_cache_size, 0)
        self.assertFalse(TargetSolution.representation_distance_cache_cs.is_caching)
        self.assertEqual(TargetSolution.representation_distance_cache_cs.max_cache_size, 0)

    # Call the init_random() method with a TargetProblem instance as an argument and verify that the representation property is set to a BitArray with the correct length.
    def test_init_random_method_with_target_problem(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        problem.dimension = 10
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        solution.init_random(problem)

        # Assert
        self.assertIsInstance(solution.representation, BitArray)
        self.assertEqual(len(solution.representation), problem.dimension)

    # Call the init_from() method with a BitArray instance and a TargetProblem instance as arguments and verify that the representation property is set to the correct BitArray.
    def test_init_from_method_with_bitarray_and_target_problem(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        problem.dimension = 10
        representation = BitArray(bin="1010101010")
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        solution.init_from(representation, problem)

        # Assert
        self.assertEqual(solution.representation, representation)

    # Call the calculate_quality_directly() method with a BitArray instance and a TargetProblem instance as arguments and verify that the returned QualityOfSolution instance has the correct values.
    def test_calculate_quality_directly_method_with_bitarray_and_target_problem(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        representation = BitArray(bin="1010101010")
        solution = OnesCountProblemBinaryBitArraySolution()
        solution.representation = representation

        # Act
        quality = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertEqual(quality.objective_value, representation.count(True))
        self.assertIsNone(quality.fitness_values)
        self.assertEqual(quality.fitness_value, representation.count(True))
        self.assertIsNone(quality.objective_values)
        self.assertTrue(quality.is_feasible)

    # Call the native_representation() method with a string representation of a BitArray instance as an argument and verify that the returned BitArray instance has the correct value.
    def test_native_representation_method_with_string_representation(self):
        # Arrange
        representation_str = "1010101010"
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        native_representation = solution.native_representation(representation_str)

        # Assert
        self.assertEqual(native_representation.bin, representation_str)

    # Call the representation_distance_directly() method with two string representations of BitArray instances as arguments and verify that the returned distance is correct.
    def test_representation_distance_directly_method_with_string_representations(self):
        # Arrange
        solution_code_1 = "1010101010"
        solution_code_2 = "1111000011"
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)

        # Assert
        self.assertEqual(distance, 5)

    # Call the calculate_quality_directly() method with a BitArray instance that has all bits set to False and verify that the returned QualityOfSolution instance has the correct values.
    def test_calculate_quality_directly_method_with_all_bits_false(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        representation = BitArray(bin="0000000000")
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        quality = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertEqual(quality.objective_value, 0)
        self.assertIsNone(quality.fitness_values)
        self.assertEqual(quality.fitness_value, 0)
        self.assertIsNone(quality.objective_values)
        self.assertTrue(quality.is_feasible)

    # Initialize a new instance of OnesCountProblemBinaryBitArraySolution with default parameters and verify that all properties are set correctly.
    def test_initialize_instance_with_default_parameters(self):
        # Arrange
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act

        # Assert
        self.assertEqual(solution.name, "OnesCountProblemBinaryBitArraySolution")
        self.assertIsNone(solution.fitness_value)
        self.assertIsNone(solution.fitness_values)
        self.assertIsNone(solution.objective_value)
        self.assertIsNone(solution.objective_values)
        self.assertFalse(solution.is_feasible)
        self.assertFalse(TargetSolution.evaluation_cache_cs.is_caching)
        self.assertEqual(TargetSolution.evaluation_cache_cs.max_cache_size, 0)
        self.assertFalse(TargetSolution.representation_distance_cache_cs.is_caching)
        self.assertEqual(TargetSolution.representation_distance_cache_cs.max_cache_size, 0)

    # Call the init_random() method with a TargetProblem instance as an argument and verify that the representation property is set to a BitArray with the correct length.
    def test_init_random_method_with_target_problem(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        problem.dimension = 10
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        solution.init_random(problem)

        # Assert
        self.assertIsInstance(solution.representation, BitArray)
        self.assertEqual(len(solution.representation), problem.dimension)

    # Call the init_from() method with a BitArray instance and a TargetProblem instance as arguments and verify that the representation property is set to the correct BitArray.
    def test_init_from_method_with_bitarray_and_target_problem(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        problem.dimension = 10
        representation = BitArray(bin="1010101010")
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        solution.init_from(representation, problem)

        # Assert
        self.assertEqual(solution.representation, representation)

    # Call the calculate_quality_directly() method with a BitArray instance and a TargetProblem instance as arguments and verify that the returned QualityOfSolution instance has the correct values.
    def test_calculate_quality_directly_method_with_bitarray_and_target_problem(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        representation = BitArray(bin="1010101010")
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        quality = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertEqual(quality.objective_value, representation.count(True))
        self.assertIsNone(quality.fitness_values)
        self.assertEqual(quality.fitness_value, representation.count(True))
        self.assertIsNone(quality.objective_values)
        self.assertTrue(quality.is_feasible)

    # Call the native_representation() method with a string representation of a BitArray instance as an argument and verify that the returned BitArray instance has the correct value.
    def test_native_representation_method_with_string_representation(self):
        # Arrange
        representation_str = "1010101010"
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        native_representation = solution.native_representation(representation_str)

        # Assert
        self.assertEqual(native_representation.bin, representation_str)

    # Call the representation_distance_directly() method with two string representations of BitArray instances as arguments and verify that the returned distance is correct.
    def test_representation_distance_directly_method_with_string_representations(self):
        # Arrange
        solution_code_1 = "1010101010"
        solution_code_2 = "1111000011"
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)

        # Assert
        self.assertEqual(distance, 5)


    # Call the calculate_quality_directly() method with a BitArray instance that has all bits set to False and verify that the returned QualityOfSolution instance has the correct values.
    def test_calculate_quality_directly_method_with_all_bits_false(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        representation = BitArray(bin="0000000000")
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        quality = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertEqual(quality.objective_value, 0)
        self.assertIsNone(quality.fitness_values)
        self.assertEqual(quality.fitness_value, 0)
        self.assertIsNone(quality.objective_values)
        self.assertTrue(quality.is_feasible)

    # Call the calculate_quality_directly() method with a BitArray instance that has all bits set to True and verify that the returned QualityOfSolution instance has the correct values.
    def test_calculate_quality_directly_method_with_all_bits_true(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        representation = BitArray(bin="1111111")
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        quality = solution.calculate_quality_directly(representation, problem)

        # Assert
        self.assertEqual(quality.objective_value, 7)
        self.assertIsNone(quality.fitness_values)
        self.assertEqual(quality.fitness_value, 7)
        self.assertIsNone(quality.objective_values)
        self.assertTrue(quality.is_feasible)


    # Call the copy() method and verify that the returned OnesCountProblemBinaryBitArraySolution instance is a deep copy of the original instance.
    def test_copy_method_returns_deep_copy(self):
        # Arrange
        solution = OnesCountProblemBinaryBitArraySolution()
    
        # Act
        copy_solution = solution.copy()
    
        # Assert
        self.assertIsNot(solution, copy_solution)
        self.assertEqual(solution.name, copy_solution.name)
        self.assertEqual(solution.fitness_value, copy_solution.fitness_value)
        self.assertEqual(solution.fitness_values, copy_solution.fitness_values)
        self.assertEqual(solution.objective_value, copy_solution.objective_value)
        self.assertEqual(solution.objective_values, copy_solution.objective_values)
        self.assertEqual(solution.is_feasible, copy_solution.is_feasible)

    # Call the representation_distance_directly() method with two string representations of BitArray instances that have different lengths and verify that the method raises a ValueError.
    def test_representation_distance_directly_raises_value_error(self):
        # Arrange
        solution = OnesCountProblemBinaryBitArraySolution()
        representation_1 = "101010"
        representation_2 = "10101010"
    
        # Act & Assert
        with self.assertRaises(ValueError):
            solution.representation_distance_directly(representation_1, representation_2)

    # Call the argument() method with a BitArray instance as an argument and verify that the returned string representation is correct.
    def test_argument_method_returns_correct_string_representation(self):
        # Arrange
        solution = OnesCountProblemBinaryBitArraySolution()
        representation = BitArray(bin="101010")
    
        # Act
        argument = solution.argument(representation)
    
        # Assert
        self.assertEqual(argument, "101010")


class TestArgument(unittest.TestCase):

    # Returns a string representation of the internal BitArray representation.
    def test_returns_string_representation(self):
        # Arrange
        representation = BitArray(bin='101010')
        solution = OnesCountProblemBinaryBitArraySolution()
    
        # Act
        argument = solution.argument(representation)
    
        # Assert
        self.assertEqual(argument, '101010')

    # Returns a binary string representation of the internal BitArray representation.
    def test_returns_binary_string_representation(self):
        # Arrange
        representation = BitArray(bin='101010')
        solution = OnesCountProblemBinaryBitArraySolution()
    
        # Act
        argument = solution.argument(representation)
    
        # Assert
        self.assertIsInstance(argument, str)
        self.assertTrue(all(bit in ['0', '1'] for bit in argument))

    # Returns an empty string when the internal BitArray representation is empty.
    def test_returns_empty_string_for_empty_representation(self):
        # Arrange
        representation = BitArray()
        solution = OnesCountProblemBinaryBitArraySolution()
    
        # Act
        argument = solution.argument(representation)
    
        # Assert
        self.assertEqual(argument, '')

    # Returns a string representation of the internal BitArray representation with leading zeros when all bits are False.
    def test_returns_string_representation_with_leading_zeros_for_all_false_bits(self):
        # Arrange
        representation = BitArray(bin='000000')
        solution = OnesCountProblemBinaryBitArraySolution()
    
        # Act
        argument = solution.argument(representation)
    
        # Assert
        self.assertEqual(argument, '000000')


class TestInitRandom(unittest.TestCase):

    # Initializes a solution with a BitArray representation of the correct dimension
    def test_initializes_solution_with_correct_dimension(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        problem.dimension = 10
        solution = OnesCountProblemBinaryBitArraySolution()
    
        # Act
        solution.init_random(problem)
    
        # Assert
        self.assertEqual(len(solution.representation), problem.dimension)

    # Sets each element of the BitArray representation to True or False with a 50% probability
    def test_sets_elements_to_true_or_false_with_probability_50_percent(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        problem.dimension = 10
        solution = OnesCountProblemBinaryBitArraySolution()
        
        # Act
        solution.init_random(problem)
    
        # Assert
        for element in solution.representation:
            self.assertTrue(element in [True, False])

    # Initializes a solution with a BitArray representation of dimension 0
    def test_initializes_solution_with_dimension_0(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        problem.dimension = 0
        solution = OnesCountProblemBinaryBitArraySolution()
    
        # Act
        solution.init_random(problem)
    
        # Assert
        self.assertEqual(len(solution.representation), 0)

    # Initializes a solution with a BitArray representation of negative dimension
    def test_initializes_solution_with_negative_dimension(self):
        # Arrange
        problem = TargetProblemVoid('problem name', is_minimization=True)
        problem.dimension = -1
        solution = OnesCountProblemBinaryBitArraySolution()
    
        # Act & Assert
        with self.assertRaises(ValueError):
            solution.init_random(problem)
    
class TestInitFrom(unittest.TestCase):

    # Sets the internal representation of the solution to the given BitArray representation
    def test_sets_internal_representation(self):
        # Arrange
        representation = BitArray(bin='101010')
        problem = TargetProblemVoid('problem name', is_minimization=True)
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act
        solution.init_from(representation, problem)

        # Assert
        self.assertEqual(solution.representation, representation)

    # Raises a TypeError if the given representation is not a BitArray
    def test_raises_type_error_for_invalid_representation(self):
        # Arrange
        representation = '101010'
        problem = TargetProblemVoid('problem name', is_minimization=True)
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act & Assert
        with self.assertRaises(TypeError):
            solution.init_from(representation, problem)
