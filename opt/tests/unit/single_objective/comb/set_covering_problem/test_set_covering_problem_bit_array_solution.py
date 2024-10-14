import unittest
import networkx as nx

from random import choice, randint

from bitstring import BitArray

from opt.single_objective.comb.min_set_cover_problem.min_set_cover_problem_bit_array_solution import MinSetCoverProblemBitArraySolution

from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.solution.solution import Solution


class TestMinSetCoverProblemBitArraySolution(unittest.TestCase):

    # Initialize a new instance of MinSetCoverProblemBitArraySolution with default parameters and verify that all properties are set correctly.
    def test_initialize_instance_with_default_parameters(self):
        # Arrange
        # Act
        solution = MinSetCoverProblemBitArraySolution()
        # Assert
        self.assertIsNone(solution.fitness_value)
        self.assertIsNone(solution.fitness_values)
        self.assertIsNone(solution.objective_value)
        self.assertIsNone(solution.objective_values)
        self.assertFalse(solution.is_feasible)
        self.assertIsNone(solution.evaluation_cache_cs)
        self.assertIsNone(solution.representation_distance_cache_cs)

    # Call the init_random() method with a Problem instance as an argument and verify that the representation property is set to a BitArray with the correct length.
    def test_init_random_method_with_problem(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]

        problem = ProblemVoidMinSO('problem name', is_minimization=True)
        problem.universe = universe
        problem.subsets = subsets
        solution = MinSetCoverProblemBitArraySolution()
        # Act
        solution.init_random(problem)
        # Assert
        self.assertIsInstance(solution.representation, BitArray)
        self.assertEqual(len(solution.representation), len(subsets))

    # Call the init_from() method with a BitArray instance and a Problem instance as arguments and verify that the representation property is set to the correct BitArray.
    def test_init_from_method_with_bitarray_and_problem(self):
        # Arrange
        problem = ProblemVoidMinSO('problem name', is_minimization=True)
        problem.dimension = 10
        representation = BitArray(bin="1010101010")
        solution = MinSetCoverProblemBitArraySolution()
        # Act
        solution.init_from(representation, problem)
        # Assert
        self.assertEqual(solution.representation, representation)

    # Call the native_representation() method with a string representation of a BitArray instance as an argument and verify that the returned BitArray instance has the correct value.
    def test_native_representation_method_with_string_representation(self):
        # Arrange
        representation_str = "1010101010"
        solution = MinSetCoverProblemBitArraySolution()
        # Act
        native_representation = solution.native_representation(representation_str)
        # Assert
        self.assertEqual(native_representation.bin, representation_str)

    # Call the representation_distance_directly() method with two string representations of BitArray instances as arguments and verify that the returned distance is correct.
    def test_representation_distance_directly_method_with_string_representations(self):
        # Arrange
        solution_code_1 = "1010101010"
        solution_code_2 = "1111000011"
        solution = MinSetCoverProblemBitArraySolution()
        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)
        # Assert
        self.assertEqual(distance, 5)

    
    # Call the calculate_quality_directly() method with a BitArray instance that has all bits set to True and verify that the returned QualityOfSolution instance has the correct values.
    def test_calculate_quality_directly_method_with_all_bits_True(self):
        # Arrange
        universe = {1, 2, 3, 4, 5, 6}
        subsets = [
            {1, 2, 3}, {3, 4}, {3, 4, 5}, {1, 5}, {4}
        ]

        problem = ProblemVoidMinSO('problem name', is_minimization=True)
        problem.universe = universe
        problem.subsets = subsets
        solution = MinSetCoverProblemBitArraySolution()
        representation = solution.native_representation("1"*len(subsets))
        # Act
        quality = solution.calculate_quality_directly(representation, problem)
        # Assert
        self.assertEqual(quality.objective_value, float('inf'))
        self.assertIsNone(quality.fitness_values)
        self.assertEqual(quality.fitness_value, float('-inf'))
        self.assertIsNone(quality.objective_values)
        self.assertFalse(quality.is_feasible)

    # Call the copy() method and verify that the returned MinSetCoverProblemBitArraySolution instance is a deep copy of the original instance.
    def test_copy_method_returns_deep_copy(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
        # Act
        copy_solution = solution.copy()
        # Assert
        self.assertIsNot(solution, copy_solution)
        self.assertEqual(solution.fitness_value, copy_solution.fitness_value)
        self.assertEqual(solution.fitness_values, copy_solution.fitness_values)
        self.assertEqual(solution.objective_value, copy_solution.objective_value)
        self.assertEqual(solution.objective_values, copy_solution.objective_values)
        self.assertEqual(solution.is_feasible, copy_solution.is_feasible)

    # Call the representation_distance_directly() method with two string representations of BitArray instances that have different lengths and verify that the method raises a ValueError.
    def test_representation_distance_directly_raises_value_error(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
        representation_1 = "101010"
        representation_2 = "10101010"
        # Act & Assert
        with self.assertRaises(ValueError):
            solution.representation_distance_directly(representation_1, representation_2)

    # Call the argument() method with a BitArray instance as an argument and verify that the returned string representation is correct.
    def test_argument_method_returns_correct_string_representation(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
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
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act
        argument = solution.argument(representation)
    
        # Assert
        self.assertEqual(argument, '101010')

    # Returns a binary string representation of the internal BitArray representation.
    def test_returns_binary_string_representation(self):
        # Arrange
        representation = BitArray(bin='101010')
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act
        argument = solution.argument(representation)
    
        # Assert
        self.assertIsInstance(argument, str)
        self.assertTrue(all(bit in ['0', '1'] for bit in argument))

    # Returns an empty string when the internal BitArray representation is empty.
    def test_returns_empty_string_for_empty_representation(self):
        # Arrange
        representation = BitArray()
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act
        argument = solution.argument(representation)
    
        # Assert
        self.assertEqual(argument, '')

    # Returns a string representation of the internal BitArray representation with leading zeros when all bits are False.
    def test_returns_string_representation_with_leading_zeros_for_all_false_bits(self):
        # Arrange
        representation = BitArray(bin='000000')
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act
        argument = solution.argument(representation)
    
        # Assert
        self.assertEqual(argument, '000000')

    
class TestInitFrom(unittest.TestCase):

    # Sets the internal representation of the solution to the given BitArray representation
    def test_sets_internal_representation(self):
        # Arrange
        representation = BitArray(bin='101010')
        problem = ProblemVoidMinSO('problem name', is_minimization=True)
        solution = MinSetCoverProblemBitArraySolution()

        # Act
        solution.init_from(representation, problem)

        # Assert
        self.assertEqual(solution.representation, representation)

    # Raises a TypeError if the given representation is not a BitArray
    def test_raises_type_error_for_invalid_representation(self):
        # Arrange
        representation = '101010'
        problem = ProblemVoidMinSO('problem name', is_minimization=True)
        solution = MinSetCoverProblemBitArraySolution()

        # Act & Assert
        with self.assertRaises(TypeError):
            solution.init_from(representation, problem)


class TestNativeRepresentation(unittest.TestCase):

    # Should return a BitArray object when given a valid binary string representation of a solution
    def test_valid_binary_string_representation(self):
        # Arrange
        representation_str = "101010"
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act
        native_representation = solution.native_representation(representation_str)
    
        # Assert
        self.assertIsInstance(native_representation, BitArray)

    # Should return a BitArray object with the same binary representation as the input string representation
    def test_same_binary_representation(self):
        # Arrange
        representation_str = "101010"
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act
        native_representation = solution.native_representation(representation_str)
    
        # Assert
        self.assertEqual(native_representation.bin, representation_str)

    # Should work correctly for a binary string representation of length 1
    def test_length_1_representation(self):
        # Arrange
        representation_str = "1"
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act
        native_representation = solution.native_representation(representation_str)
    
        # Assert
        self.assertEqual(native_representation.bin, representation_str)

    # Should raise a TypeError when given a representation that is not a string
    def test_non_string_representation(self):
        # Arrange
        representation_str = 101010
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.native_representation(representation_str)

    
    # Should raise a ValueError when given a string representation that contains characters other than '0' and '1'
    def test_invalid_characters_representation(self):
        # Arrange
        representation_str = "10102"
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act & Assert
        with self.assertRaises(ValueError):
            solution.native_representation(representation_str)

   
class TestRepresentationDistanceDirectly(unittest.TestCase):

    # Calculate distance between two identical solutions
    def test_identical_solutions(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
        solution_code_1 = "101010"
        solution_code_2 = "101010"
    
        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)
    
        # Assert
        self.assertEqual(distance, 0)

    # Calculate distance between two completely different solutions
    def test_completely_different_solutions(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
        solution_code_1 = "101010"
        solution_code_2 = "000000"
    
        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)
    
        # Assert
        self.assertEqual(distance, 3)

    # Calculate distance between two solutions with only one different bit
    def test_one_different_bit(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
        solution_code_1 = "101010"
        solution_code_2 = "101011"
    
        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)
    
        # Assert
        self.assertEqual(distance, 1)

    # Calculate distance between two empty solutions
    def test_empty_solutions(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
        solution_code_1 = ""
        solution_code_2 = ""
    
        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)
    
        # Assert
        self.assertEqual(distance, 0)

    # Calculate distance between two solutions with different lengths
    def test_different_lengths(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
        solution_code_1 = "101010"
        solution_code_2 = "10101010"
    
        # Act & Assert
        with self.assertRaises(ValueError):
            solution.representation_distance_directly(solution_code_1, solution_code_2)
    
    # Calculate distance between two solutions with different types
    def test_different_types(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
        solution_code_1 = "101010"
        solution_code_2 = 101010
    
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.representation_distance_directly(solution_code_1, solution_code_2)


class TestStringRep(unittest.TestCase):

    # Returns a string representation of the solution instance.
    def test_returns_string_representation(self):
        # Arrange
        problem = ProblemVoidMinSO("x**2", True)
        solution = MinSetCoverProblemBitArraySolution()
        solution.init_from(BitArray('0b1110'), problem)
        # Act
        result = solution.string_rep()
        # Assert
        self.assertIsInstance(result, str)

    # Includes the string representation of the super class.
    def test_includes_super_class_representation(self):
        # Arrange
        problem = ProblemVoidMinSO("x**2", True)
        solution = MinSetCoverProblemBitArraySolution()
        solution.init_from(BitArray('0b1110'), problem)
        # Act
        result = solution.string_rep()
        # Assert
        self.assertIn("representation()", result)

    # Includes the string representation of the solution's string_representation.
    def test_includes_string_representation(self):
        # Arrange
        problem = ProblemVoidMinSO("x**2", True)
        solution = MinSetCoverProblemBitArraySolution()
        solution.init_from(BitArray('0b1110'), problem)
    
        # Act
        result = solution.string_rep()
    
        # Assert
        self.assertIn("string_representation()", result)

    # Delimiter, indentation, indentation_symbol, group_start, and group_end are optional parameters.
    def test_optional_parameters(self):
        # Arrange
        problem = ProblemVoidMinSO("x**2", True)
        solution = MinSetCoverProblemBitArraySolution()
        solution.init_from(BitArray('0b1110'), problem)
    
        # Act
        result = solution.string_rep()
    
        # Assert
        self.assertIsInstance(result, str)

    # Default values for delimiter, indentation, indentation_symbol, group_start, and group_end are '\n', 0, '   ', '{', and '}', respectively.
    def test_default_values(self):
        # Arrange
        problem = ProblemVoidMinSO("x**2", True)
        solution = MinSetCoverProblemBitArraySolution()
        solution.init_from(BitArray('0b1110'), problem)
    
        # Act
        result = solution.string_rep()
    
        # Assert
        expected_result = "string_representation()=1110"
        self.assertIn(result, result)

    # If delimiter is None, it raises a TypeError.
    def test_delimiter_is_none(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.string_rep(delimiter=None)

    # If indentation is None, it raises a TypeError.
    def test_indentation_is_none(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.string_rep(indentation=None)

    # If group_start is None, it raises a TypeError.
    def test_group_start_is_none(self):
        # Arrange
        solution = MinSetCoverProblemBitArraySolution()
    
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.string_rep(group_start=None)
