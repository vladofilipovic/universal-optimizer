
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

