import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem
from uo.target_problem.target_problem_void import TargetProblemVoid

from uo.target_solution.quality_of_solution import QualityOfSolution
from uo.target_solution.target_solution import TargetSolution 
from uo.target_solution.target_solution_void_object_str import TargetSolutionVoidObjectStr


class TestTargetSolutionVoidObjectStr(unittest.TestCase):

    # TargetSolution can be instantiated with valid parameters
    def test_instantiation_with_valid_parameters(self):
        # Arrange
        # Act
        target_solution = TargetSolutionVoidObjectStr()
        # Assert
        self.assertIsInstance(target_solution, TargetSolution)
        self.assertIsInstance(target_solution, TargetSolutionVoidObjectStr)

    # The name, random_seed, fitness_value, fitness_values, objective_value, objective_values, is_feasible, representation, evaluation_cache_cs, and representation_distance_cache_cs attributes can be accessed and modified
    def test_attribute_access_and_modification(self):
        # Arrange
        target_solution = TargetSolutionVoidObjectStr()
        # Act
        target_solution.fitness_value = 0.7
        target_solution.fitness_values = [0.6, 0.7, 0.8]
        target_solution.objective_value = 200
        target_solution.objective_values = [150, 175, 200]
        target_solution.is_feasible = False
        target_solution.representation = "representation"
        # Assert
        self.assertEqual(target_solution.fitness_value, 0.7)
        self.assertEqual(target_solution.fitness_values, [0.6, 0.7, 0.8])
        self.assertEqual(target_solution.objective_value, 200)
        self.assertEqual(target_solution.objective_values, [150, 175, 200])
        self.assertFalse(target_solution.is_feasible)
        self.assertEqual(target_solution.representation, "representation")

    # The copy, copy_from, argument, string_representation, init_random, native_representation, init_from, calculate_quality_directly, calculate_quality, representation_distance_directly, representation_distance, string_rep, __str__, __repr__, and __format__ methods can be called and return expected results
    def test_method_calls_and_results(self):
        # Arrange
        target_problem = TargetProblemVoid("a", True)
        target_solution = TargetSolutionVoidObjectStr()
        # Act and Assert
        self.assertIsNotNone(target_solution.copy())
        self.assertIsNotNone(target_solution.argument(target_solution.representation))
        self.assertIsNotNone(target_solution.native_representation("representation"))
        self.assertIsNotNone(target_solution.calculate_quality_directly(target_solution.representation, 
                    target_problem))
        self.assertIsNotNone(target_solution.calculate_quality(target_problem))
        self.assertIsNotNone(target_solution.representation_distance_directly(target_solution.representation, 
                    target_solution.representation))
        self.assertIsNotNone(target_solution.representation_distance(target_solution.representation, 
                    target_solution.representation))
        self.assertIsInstance(target_solution.string_rep("|"), str)

    # TargetSolution raises TypeError if any parameter is of the wrong type
    def test_type_error_raised(self):
        # Arrange
        random_seed = "seed"
        fitness_value = "fitness"
        fitness_values = [0.3, 0.4, 0.5]
        objective_value = "objective"
        objective_values = [50, 75, 100]
        is_feasible = "feasible"
        evaluation_cache_is_used = "cache"
        evaluation_cache_max_size = "max_size"
        distance_calculation_cache_is_used = "cache"
        distance_calculation_cache_max_size = "max_size"
        # Act and Assert
        with self.assertRaises(TypeError):
            TargetSolution(random_seed, fitness_value, fitness_values, objective_value, objective_values, is_feasible, evaluation_cache_is_used, evaluation_cache_max_size, distance_calculation_cache_is_used, distance_calculation_cache_max_size)

    # TargetSolution sets random_seed to a random integer if it is None or 0
    def test_random_seed_set_to_random_integer(self):
        # Arrange
        # Act
        target_solution = TargetSolutionVoidObjectStr()
        # Assert
        self.assertIsInstance(target_solution.random_seed, int)
        self.assertNotEqual(target_solution.random_seed, 0)

    # TargetSolution sets fitness_value, fitness_values, objective_value, and objective_values to None if they are not provided
    def test_default_values_for_fitness_and_objective(self):
        # Arrange
        # Act
        target_solution = TargetSolutionVoidObjectStr()
        # Assert
        target_solution.fitness_value = None
        target_solution.fitness_values = None
        target_solution.objective_value = None
        target_solution.objective_values = None
        self.assertIsNone(target_solution.fitness_value)
        self.assertIsNone(target_solution.fitness_values)
        self.assertIsNone(target_solution.objective_value)
        self.assertIsNone(target_solution.objective_values)

    # TargetSolution sets representation to None by default
    def test_default_representation_value(self):
        # Arrange
        # Act
        target_solution = TargetSolutionVoidObjectStr()
        # Assert
        self.assertIsNone(target_solution.representation)

    # TargetSolution sets evaluation_cache_cs and representation_distance_cache_cs to default values if they are not provided
    def test_default_values_for_caches(self):
        # Arrange
        if hasattr(TargetSolution, 'evaluation_cache_cs'):
            del TargetSolution.evaluation_cache_cs
        if hasattr(TargetSolution, 'representation_distance_cache_cs'):
            del TargetSolution.representation_distance_cache_cs
        # Act
        target_solution = TargetSolutionVoidObjectStr()
        # Assert
        self.assertFalse(target_solution.evaluation_cache_cs.is_caching)
        self.assertEqual(target_solution.evaluation_cache_cs.max_cache_size, 0)
        self.assertFalse(target_solution.representation_distance_cache_cs.is_caching)
        self.assertEqual(target_solution.representation_distance_cache_cs.max_cache_size, 0)

    # TargetSolution can be deep copied
    def test_deep_copy(self):
        # Arrange
        target_solution = TargetSolutionVoidObjectStr()
        target_solution.fitness_value = 23
        target_solution.objective_value = 23
        # Act
        copied_solution = target_solution.copy()
        # Assert
        self.assertIsNot(target_solution, copied_solution)
        self.assertEqual(target_solution.random_seed, copied_solution.random_seed)
        self.assertEqual(target_solution.fitness_value, copied_solution.fitness_value)
        self.assertEqual(target_solution.fitness_values, copied_solution.fitness_values)
        self.assertEqual(target_solution.objective_value, copied_solution.objective_value)
        self.assertEqual(target_solution.objective_values, copied_solution.objective_values)
        self.assertEqual(target_solution.is_feasible, copied_solution.is_feasible)
        self.assertEqual(target_solution.representation, copied_solution.representation)
        self.assertEqual(target_solution.evaluation_cache_cs.is_caching, copied_solution.evaluation_cache_cs.is_caching)
        self.assertEqual(target_solution.evaluation_cache_cs.max_cache_size, copied_solution.evaluation_cache_cs.max_cache_size)
        self.assertEqual(target_solution.representation_distance_cache_cs.is_caching, copied_solution.representation_distance_cache_cs.is_caching)
        self.assertEqual(target_solution.representation_distance_cache_cs.max_cache_size, copied_solution.representation_distance_cache_cs.max_cache_size)

    # TargetSolution can be evaluated with a TargetProblem object
    def test_evaluate_with_target_problem(self):
        # Arrange
        target_solution = TargetSolutionVoidObjectStr()
        target_problem_mock = mocker.Mock()
        # Act
        target_solution.evaluate(target_problem_mock)
        # Assert
        self.assertEqual(target_solution.objective_value, 
                    target_solution.calculate_quality_directly(target_solution.representation, target_problem_mock).objective_value)
        self.assertEqual(target_solution.fitness_value, 
                    target_solution.calculate_quality_directly(target_solution.representation, target_problem_mock).fitness_value)
        self.assertEqual(target_solution.is_feasible, 
                    target_solution.calculate_quality_directly(target_solution.representation, target_problem_mock).is_feasible)

    # TargetSolution can be represented as a string with a specified delimiter, indentation, and grouping symbols
    def test_string_representation(self):
        # Arrange
        target_solution = TargetSolutionVoidObjectStr()
        target_solution.fitness_value = 0.5
        target_solution.objective_value = 100
        target_solution.is_feasible =  True
        # Act
        string_rep = target_solution.string_rep('|')
        # Assert
        expected_string_rep = "|fitness_value=0.5|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|objective_value=100|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|is_feasible=True|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|representation()=None|"
        self.assertIn(expected_string_rep, string_rep)

    # TargetSolution can be represented as a string with a specified delimiter, indentation, and grouping symbols
    def test_string_conversion(self):
        # Arrange
        target_solution = TargetSolutionVoidObjectStr()
        target_solution.fitness_value = 0.5
        target_solution.objective_value = 100
        target_solution.is_feasible =  True
        # Act
        string_rep = str(target_solution)
        # Assert
        expected_string_rep = "|fitness_value=0.5|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|objective_value=100|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|is_feasible=True|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|representation()=None|"
        self.assertIn(expected_string_rep, string_rep)

    # TargetSolution can be represented as a string with a specified delimiter, indentation, and grouping symbols
    def test_format_to_string(self):
        # Arrange
        target_solution = TargetSolutionVoidObjectStr()
        target_solution.fitness_value = 0.5
        target_solution.objective_value = 100
        target_solution.is_feasible =  True
        # Act
        string_rep = format(target_solution)
        # Assert
        expected_string_rep = "fitness_value=0.5"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "objective_value=100"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "is_feasible=True"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "representation()=None"
        self.assertIn(expected_string_rep, string_rep)

    # initializes the solution with a valid representation and problem
    def test_initialization_with_valid_representation_and_problem(self):
        # Arrange
        representation = 42
        problem = TargetProblemVoid("a", True)
        solution = TargetSolutionVoidObjectStr()
        # Act
        solution.init_from(representation, problem)
        # Assert
        self.assertEqual(solution._TargetSolution__representation, representation)

    # sets the representation of the solution to the given representation
    def test_sets_representation_to_given_representation2(self):
        # Arrange
        representation = 42
        problem = TargetProblemVoid("a", True)
        solution = TargetSolutionVoidObjectStr()
        # Act
        solution.init_from(representation, problem)
        # Assert
        self.assertEqual(solution._TargetSolution__representation, representation)

    # raises TypeError if the given problem is not of type TargetProblem
    def test_raises_TypeError_if_problem_not_of_type_TargetProblem(self):
        # Arrange
        representation = "example_representation"
        problem = "example_problem"
        solution = TargetSolutionVoidObjectStr()
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.init_from(representation, problem)
