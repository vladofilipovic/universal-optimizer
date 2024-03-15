
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.problem.problem import Problem
from uo.problem.problem_void import ProblemVoid

from uo.solution.quality_of_solution import QualityOfSolution
from uo.solution.solution import Solution 
from uo.solution.solution_void import SolutionVoid


class TestSolution(unittest.TestCase):

    # Solution can be instantiated with valid parameters
    def test_instantiation_with_valid_parameters(self):
        # Arrange
        if hasattr(Solution, 'evaluation_cache_cs'):
            del Solution.evaluation_cache_cs
        if hasattr(Solution, 'representation_distance_cache_cs'):
            del Solution.representation_distance_cache_cs
        random_seed = 123
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        # Act
        solution = SolutionVoid(random_seed, fitness_value, objective_value, 
                    is_feasible, evaluation_cache_is_used, evaluation_cache_max_size, 
                    distance_calculation_cache_is_used, distance_calculation_cache_max_size)
        # Assert
        self.assertEqual(solution.random_seed, random_seed)
        self.assertEqual(solution.fitness_value, fitness_value)
        self.assertEqual(solution.objective_value, objective_value)
        self.assertEqual(solution.is_feasible, is_feasible)
        self.assertIsNone(solution.representation)
        self.assertTrue(solution.evaluation_cache_cs.is_caching)
        self.assertEqual(solution.evaluation_cache_cs.max_cache_size, evaluation_cache_max_size)
        self.assertTrue(solution.representation_distance_cache_cs.is_caching)
        self.assertEqual(solution.representation_distance_cache_cs.max_cache_size, distance_calculation_cache_max_size)

    # The random_seed, fitness_value, fitness_values, objective_value, objective_values, is_feasible, representation, evaluation_cache_cs, and representation_distance_cache_cs attributes can be accessed and modified
    def test_attribute_access_and_modification(self):
        # Arrange
        random_seed = 123
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        solution = SolutionVoid(random_seed, fitness_value, objective_value, 
                    is_feasible, evaluation_cache_is_used, evaluation_cache_max_size, 
                    distance_calculation_cache_is_used, distance_calculation_cache_max_size)
        # Act
        solution.fitness_value = 0.7
        solution.fitness_values = [0.6, 0.7, 0.8]
        solution.objective_value = 200
        solution.objective_values = [150, 175, 200]
        solution.is_feasible = False
        solution.representation = "representation"
        # Assert
        self.assertEqual(solution.fitness_value, 0.7)
        self.assertEqual(solution.fitness_values, [0.6, 0.7, 0.8])
        self.assertEqual(solution.objective_value, 200)
        self.assertEqual(solution.objective_values, [150, 175, 200])
        self.assertFalse(solution.is_feasible)
        self.assertEqual(solution.representation, "representation")

    # The copy, copy_from, argument, string_representation, init_random, native_representation, init_from, calculate_quality_directly, calculate_quality, representation_distance_directly, representation_distance, string_rep, __str__, __repr__, and __format__ methods can be called and return expected results
    def test_method_calls_and_results(self):
        # Arrange
        random_seed = 123
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        problem = ProblemVoid("a", True)
        solution = SolutionVoid(random_seed, fitness_value, objective_value, 
                    is_feasible, evaluation_cache_is_used, evaluation_cache_max_size, 
                    distance_calculation_cache_is_used, distance_calculation_cache_max_size)
        # Act and Assert
        self.assertIsNotNone(solution.copy())
        self.assertIsNotNone(solution.argument(solution.representation))
        self.assertIsInstance(solution.string_representation(), str)
        self.assertIsNotNone(solution.native_representation("representation"))
        self.assertIsNotNone(solution.calculate_quality_directly(solution.representation, 
                    problem))
        self.assertIsNotNone(solution.calculate_quality(problem))
        self.assertIsNotNone(solution.representation_distance_directly(solution.representation, 
                    solution.representation))
        self.assertIsNotNone(solution.representation_distance(solution.representation, 
                    solution.representation))
        self.assertIsInstance(solution.string_rep("|"), str)
        self.assertIsInstance(str(solution), str)
        self.assertIsInstance(repr(solution), str)
        self.assertIsInstance(format(solution, ""), str)

    # Solution raises TypeError if any parameter is of the wrong type
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
            Solution(random_seed, fitness_value, fitness_values, objective_value, objective_values, is_feasible, evaluation_cache_is_used, evaluation_cache_max_size, distance_calculation_cache_is_used, distance_calculation_cache_max_size)

    # Solution sets random_seed to a random integer if it is None or 0
    def test_random_seed_set_to_random_integer(self):
        # Arrange
        random_seed = None
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        # Act
        solution = SolutionVoid(random_seed, fitness_value, objective_value, 
                    is_feasible, evaluation_cache_is_used, evaluation_cache_max_size, 
                    distance_calculation_cache_is_used, distance_calculation_cache_max_size)
        # Assert
        self.assertIsInstance(solution.random_seed, int)
        self.assertNotEqual(solution.random_seed, 0)

    # Solution sets fitness_value, fitness_values, objective_value, and objective_values to None if they are not provided
    def test_default_values_for_fitness_and_objective(self):
        # Arrange
        random_seed = None
        fitness_value = 10
        objective_value = 12
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        # Act
        solution = SolutionVoid(random_seed, fitness_value, objective_value, 
                    is_feasible, evaluation_cache_is_used, evaluation_cache_max_size, 
                    distance_calculation_cache_is_used, distance_calculation_cache_max_size)
        # Assert
        solution.fitness_value = None
        solution.fitness_values = None
        solution.objective_value = None
        solution.objective_values = None
        self.assertIsNone(solution.fitness_value)
        self.assertIsNone(solution.fitness_values)
        self.assertIsNone(solution.objective_value)
        self.assertIsNone(solution.objective_values)

    # Solution sets representation to None by default
    def test_default_representation_value(self):
        # Arrange
        random_seed = None
        fitness_value = 10
        objective_value = 12
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        # Act
        solution = SolutionVoid(random_seed, fitness_value, objective_value, 
                    is_feasible, evaluation_cache_is_used, evaluation_cache_max_size, 
                    distance_calculation_cache_is_used, distance_calculation_cache_max_size)
        # Assert
        self.assertIsNone(solution.representation)

    # Solution sets evaluation_cache_cs and representation_distance_cache_cs to default values if they are not provided
    def test_default_values_for_caches(self):
        # Arrange
        if hasattr(Solution, 'evaluation_cache_cs'):
            del Solution.evaluation_cache_cs
        if hasattr(Solution, 'representation_distance_cache_cs'):
            del Solution.representation_distance_cache_cs
        random_seed = 123
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        # Act
        solution = SolutionVoid(random_seed, fitness_value, objective_value, is_feasible)
        # Assert
        self.assertFalse(solution.evaluation_cache_cs.is_caching)
        self.assertEqual(solution.evaluation_cache_cs.max_cache_size, 0)
        self.assertFalse(solution.representation_distance_cache_cs.is_caching)
        self.assertEqual(solution.representation_distance_cache_cs.max_cache_size, 0)

    # Solution calculates quality of solution and caches it if evaluation_cache_is_used is True
    def test_calculate_quality_with_caching(self):
        # Arrange
        if hasattr(Solution, 'evaluation_cache_cs'):
            del Solution.evaluation_cache_cs
        if hasattr(Solution, 'representation_distance_cache_cs'):
            del Solution.representation_distance_cache_cs
        random_seed = 123
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        solution = SolutionVoid(random_seed, fitness_value, objective_value, is_feasible, 
                    evaluation_cache_is_used, evaluation_cache_max_size, distance_calculation_cache_is_used, 
                    distance_calculation_cache_max_size)
        problem_mock = mocker.Mock()
        # Act
        solution.calculate_quality(problem_mock)
        qos_c = solution.evaluation_cache_cs.cache[solution.string_representation()]
        qos_d = solution.calculate_quality_directly(solution.representation, problem_mock)
        # Assert
        self.assertEqual(qos_c.is_feasible, qos_d.is_feasible)
        self.assertEqual(qos_c.fitness_value, qos_d.fitness_value)
        self.assertEqual(qos_c.objective_value, qos_d.objective_value)

    # Solution caches representation distance if distance_calculation_cache_is_used is True
    def test_representation_distance_with_caching(self):
        # Arrange
        if hasattr(Solution, 'evaluation_cache_cs'):
            del Solution.evaluation_cache_cs
        if hasattr(Solution, 'representation_distance_cache_cs'):
            del Solution.representation_distance_cache_cs
        random_seed = 123
        fitness_value = 0.5
        objective_value = 100
        is_feasible = True
        evaluation_cache_is_used = True
        evaluation_cache_max_size = 100
        distance_calculation_cache_is_used = True
        distance_calculation_cache_max_size = 200
        solution = SolutionVoid(random_seed, fitness_value, objective_value, is_feasible, 
                    evaluation_cache_is_used, evaluation_cache_max_size, distance_calculation_cache_is_used, 
                    distance_calculation_cache_max_size)
        representation_1_mock = mocker.Mock()
        representation_2_mock = mocker.Mock()
        # Act
        solution.representation_distance(representation_1_mock, representation_2_mock)
        dis_c = solution.representation_distance_cache_cs.cache[(representation_1_mock, representation_2_mock)]
        dis_d = solution.representation_distance_directly(representation_1_mock, representation_2_mock)
        # Assert
        self.assertEqual(dis_c, dis_d)

    # Solution can be deep copied
    def test_deep_copy(self):
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
                    evaluation_cache_is_used, evaluation_cache_max_size, distance_calculation_cache_is_used, 
                    distance_calculation_cache_max_size)
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
        self.assertEqual(solution.evaluation_cache_cs.is_caching, copied_solution.evaluation_cache_cs.is_caching)
        self.assertEqual(solution.evaluation_cache_cs.max_cache_size, copied_solution.evaluation_cache_cs.max_cache_size)
        self.assertEqual(solution.representation_distance_cache_cs.is_caching, copied_solution.representation_distance_cache_cs.is_caching)
        self.assertEqual(solution.representation_distance_cache_cs.max_cache_size, copied_solution.representation_distance_cache_cs.max_cache_size)

    # Solution can be evaluated with a Problem object
    def test_evaluate_with_problem(self):
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
                    evaluation_cache_is_used, evaluation_cache_max_size, distance_calculation_cache_is_used, 
                    distance_calculation_cache_max_size)
        problem_mock = mocker.Mock()
        # Act
        solution.evaluate(problem_mock)
        # Assert
        self.assertEqual(solution.objective_value, 
                    solution.calculate_quality_directly(solution.representation, problem_mock).objective_value)
        self.assertEqual(solution.fitness_value, 
                    solution.calculate_quality_directly(solution.representation, problem_mock).fitness_value)
        self.assertEqual(solution.is_feasible, 
                    solution.calculate_quality_directly(solution.representation, problem_mock).is_feasible)

    # Solution can be represented as a string with a specified delimiter, indentation, and grouping symbols
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
                    evaluation_cache_is_used, evaluation_cache_max_size, distance_calculation_cache_is_used, 
                    distance_calculation_cache_max_size)
        # Act
        string_rep = solution.string_rep('|')
        # Assert
        expected_string_rep = "|fitness_value=0.5|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|objective_value=100|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|is_feasible=True|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|representation()=None|"
        self.assertIn(expected_string_rep, string_rep)

    # Solution can be represented as a string with a specified delimiter, indentation, and grouping symbols
    def test_string_conversion(self):
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
                    evaluation_cache_is_used, evaluation_cache_max_size, distance_calculation_cache_is_used, 
                    distance_calculation_cache_max_size)
        # Act
        string_rep = str(solution)
        # Assert
        expected_string_rep = "|fitness_value=0.5|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|objective_value=100|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|is_feasible=True|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|representation()=None|"
        self.assertIn(expected_string_rep, string_rep)

    # Solution can be represented as a string with a specified delimiter, indentation, and grouping symbols
    def test_format_to_string(self):
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
                    evaluation_cache_is_used, evaluation_cache_max_size, distance_calculation_cache_is_used, 
                    distance_calculation_cache_max_size)
        # Act
        string_rep = format(solution)
        # Assert
        expected_string_rep = "|fitness_value=0.5|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|objective_value=100|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|is_feasible=True|"
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = "|representation()=None|"
        self.assertIn(expected_string_rep, string_rep)

    # initializes the solution with a valid representation and problem
    def test_initialization_with_valid_representation_and_problem(self):
        # Arrange
        representation = 42
        problem = ProblemVoid("a", True)
        solution = SolutionVoid(None, 20, 20, True )
        # Act
        solution.init_from(representation, problem)
        # Assert
        self.assertEqual(solution._Solution__representation, representation)

    # sets the representation of the solution to the given representation
    def test_sets_representation_to_given_representation2(self):
        # Arrange
        representation = 42
        problem = ProblemVoid("a", True)
        solution = SolutionVoid(None, 20, 20, True )
        # Act
        solution.init_from(representation, problem)
        # Assert
        self.assertEqual(solution._Solution__representation, representation)

    # raises TypeError if the given representation is not of type R_co
    def test_raises_TypeError_if_representation_not_of_type_R_co(self):
        # Arrange
        representation = "invalid representation"
        problem = ProblemVoid("a", True)
        solution = SolutionVoid(None, 20, 20, True )
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.init_from(representation, problem)

    # raises TypeError if the given problem is not of type Problem
    def test_raises_TypeError_if_problem_not_of_type_Problem(self):
        # Arrange
        representation = "example_representation"
        problem = "example_problem"
        solution = SolutionVoid(None, 0, 0, True)
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.init_from(representation, problem)
