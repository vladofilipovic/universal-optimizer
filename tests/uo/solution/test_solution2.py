import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.problem.problem import Problem
from uo.problem.problem_void import ProblemVoid

from uo.solution.quality_of_solution import QualityOfSolution
from uo.solution.solution import Solution 
from uo.solution.solution_void import SolutionVoid

class TestSolution2(unittest.TestCase):

    # Setting and getting the fitness_value attribute should work as expected.
    def test_set_get_fitness_value_attribute(self):
        # Arrange
        fitness_value = 0.5
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act
        solution.fitness_value = fitness_value
        # Assert
        self.assertEqual(solution.fitness_value, fitness_value)

    # Setting and getting the fitness_values attribute should work as expected.
    def test_set_get_fitness_values_attribute(self):
        # Arrange
        fitness_values = [0.2, 0.3, 0.4]
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act
        solution.fitness_values = fitness_values
        # Assert
        self.assertEqual(solution.fitness_values, fitness_values)

    # Setting and getting the objective_value attribute should work as expected.
    def test_set_get_objective_value_attribute(self):
        # Arrange
        objective_value = 100
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act
        solution.objective_value = objective_value
        # Assert
        self.assertEqual(solution.objective_value, objective_value)

    # Setting and getting the objective_values attribute should work as expected.
    def test_set_get_objective_values_attribute(self):
        # Arrange
        objective_values = [50, 75, 100]
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act
        solution.objective_values = objective_values
        # Assert
        self.assertEqual(solution.objective_values, objective_values)

    # Creating a Solution instance with invalid parameters should raise a TypeError.
    def test_create_instance_with_invalid_parameters(self):
        # Arrange
        name = "solution"
        random_seed = "123"  # Invalid type
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        # Act & Assert
        with self.assertRaises(TypeError):
            SolutionVoid(name, random_seed, fitness_value, objective_value, is_feasible, 
                    evaluation_cache_is_used, evaluation_cache_max_size, 
                    distance_calculation_cache_is_used, distance_calculation_cache_max_size)

    # Setting the fitness_value attribute with an invalid type should raise a TypeError.
    def test_set_fitness_value_with_invalid_type(self):
        # Arrange
        fitness_value = "0.5"  # Invalid type
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.fitness_value = fitness_value

    # Setting the fitness_values attribute with an invalid type should raise a TypeError.
    def test_set_fitness_values_with_invalid_type(self):
        # Arrange
        fitness_values = "0.2, 0.3, 0.4"  # Invalid type
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.fitness_values = fitness_values

    # Setting the objective_value attribute with an invalid type should raise a TypeError.
    def test_set_objective_value_with_invalid_type(self):
        # Arrange
        objective_value = "100"  # Invalid type
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.objective_value = objective_value

    # Setting the objective_values attribute with an invalid type should raise a TypeError.
    def test_set_objective_values_with_invalid_type(self):
        # Arrange
        objective_values = "50, 75, 100"  # Invalid type
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.objective_values = objective_values

    # Setting the is_feasible attribute with an invalid type should raise a TypeError.
    def test_set_is_feasible_with_invalid_type(self):
        # Arrange
        is_feasible = "True"  # Invalid type
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act & Assert
        with self.assertRaisesRegex(TypeError, "Parameter 'is_feasible'"):
            solution.is_feasible = is_feasible

    # Setting and getting the is_feasible attribute should work as expected.
    def test_set_and_get_is_feasible(self):
        # Arrange
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act
        solution.is_feasible = True
        is_feasible = solution.is_feasible
        # Assert
        self.assertTrue(is_feasible)

    # The copy() method should create a deep copy of the Solution instance.
    def test_copy_method(self):
        # Arrange
        solution = SolutionVoid(None, 0.5, 100, True, True, 100, True, 200)
        # Act
        copied_solution = solution.copy()
        # Assert
        self.assertIsNot(solution, copied_solution)
        self.assertEqual(solution.random_seed, copied_solution.random_seed)
        self.assertEqual(solution.fitness_value, copied_solution.fitness_value)
        self.assertEqual(solution.fitness_values, copied_solution.fitness_values)
        self.assertEqual(solution.objective_value, copied_solution.objective_value)
        self.assertEqual(solution.objective_values, copied_solution.objective_values)
        self.assertEqual(solution.is_feasible, copied_solution.is_feasible)
        self.assertEqual(solution.representation, copied_solution.representation)
        self.assertEqual(solution.evaluation_cache_cs, copied_solution.evaluation_cache_cs)
        self.assertEqual(solution.representation_distance_cache_cs, copied_solution.representation_distance_cache_cs)

    # The copy_from() method should copy all attributes from another Solution instance to the current instance.
    def test_copy_from_method(self):
        # Arrange
        original_solution = SolutionVoid(None, 0.5, 100, True, True, 100, True, 200)
        original_solution.fitness_values = [1, 2, 4]
        original_solution.objective_values = [5, 6, 7]
        solution = SolutionVoid(None, None, None, False, False, 0, False, 0)
        # Act
        solution.copy_from(original_solution)
        # Assert
        self.assertEqual(solution.random_seed, original_solution.random_seed)
        self.assertEqual(solution.fitness_value, original_solution.fitness_value)
        self.assertEqual(solution.fitness_values, original_solution.fitness_values)
        self.assertEqual(solution.objective_value, original_solution.objective_value)
        self.assertEqual(solution.objective_values, original_solution.objective_values)
        self.assertEqual(solution.is_feasible, original_solution.is_feasible)
        self.assertEqual(solution.representation, original_solution.representation)

    # The string_representation() method should return a string representation of the Solution instance.
    def test_string_representation(self):
        # Arrange
        random_seed = 123
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        solution = SolutionVoid(random_seed, fitness_value, objective_value, is_feasible, 
                    evaluation_cache_is_used, evaluation_cache_max_size, 
                    distance_calculation_cache_is_used, distance_calculation_cache_max_size)
        # Act
        result = solution.string_representation()
        # Assert
        self.assertIsInstance(result, str)


    # The string_rep() method should return a string representation of the Solution instance with the specified delimiter, indentation, and grouping symbols.
    def test_string_rep(self):
        # Arrange
        random_seed = 123
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        solution = SolutionVoid(random_seed, fitness_value, objective_value, is_feasible, 
                    evaluation_cache_is_used, evaluation_cache_max_size, 
                    distance_calculation_cache_is_used, distance_calculation_cache_max_size)
        # Act
        result = solution.string_rep('|', indentation=1, indentation_symbol='-', group_start='[', group_end=']')
        # Assert
        expected_string_rep = "|-fitness_value=0.5|"
        self.assertIn(expected_string_rep, result)
        expected_string_rep = "|-objective_value=100|"
        self.assertIn(expected_string_rep, result)
        expected_string_rep = "|-is_feasible=True|"
        self.assertIn(expected_string_rep, result)
        expected_string_rep = "|-representation()=None|"
        self.assertIn(expected_string_rep, result)
