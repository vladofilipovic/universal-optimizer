import datetime
import unittest   
import unittest.mock as mocker
from uo.algorithm.metaheuristic.single_solution_metaheuristic_void import SingleSolutionMetaheuristicVoid

from uo.target_problem.target_problem import TargetProblem
from uo.target_problem.target_problem_void import TargetProblemVoid
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic 
from uo.algorithm.metaheuristic.single_solution_metaheuristic import SingleSolutionMetaheuristic
from uo.target_solution.target_solution import TargetSolution
from uo.target_solution.target_solution_void import TargetSolutionVoid

class TestSingleSolutionMetaheuristic(unittest.TestCase):

    # Creating a new instance of SingleSolutionMetaheuristic with valid parameters should initialize all properties correctly.
    def test_valid_parameters_initialization(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        initial_solution = TargetSolutionVoid("", 43, 43, 43, True)
        # Act
        metaheuristic = SingleSolutionMetaheuristicVoid(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, initial_solution)
        # Assert
        self.assertEqual(metaheuristic.name, name)
        self.assertEqual(metaheuristic.finish_control.criteria, finish_control.criteria)
        self.assertEqual(metaheuristic.finish_control.evaluations_max, finish_control.evaluations_max)
        self.assertEqual(metaheuristic.finish_control.iterations_max, finish_control.iterations_max)
        self.assertEqual(metaheuristic.finish_control.seconds_max, finish_control.seconds_max)
        self.assertEqual(metaheuristic.random_seed, random_seed)
        self.assertEqual(metaheuristic.additional_statistics_control.keep, additional_statistics_control.keep)
        self.assertEqual(metaheuristic.additional_statistics_control.max_local_optima, 
                        additional_statistics_control.max_local_optima)
        self.assertEqual(metaheuristic.output_control.fields, output_control.fields)
        self.assertEqual(metaheuristic.output_control.moments, output_control.moments)
        self.assertEqual(metaheuristic.target_problem.name, target_problem.name)
        self.assertEqual(metaheuristic.target_problem.is_minimization, target_problem.is_minimization)
        self.assertEqual(metaheuristic.current_solution.name, initial_solution.name)
        self.assertEqual(metaheuristic.current_solution.random_seed, initial_solution.random_seed)
        self.assertEqual(metaheuristic.current_solution.fitness_value, initial_solution.fitness_value)
        self.assertEqual(metaheuristic.current_solution.objective_value, initial_solution.objective_value)
        self.assertEqual(metaheuristic.current_solution.is_feasible, initial_solution.is_feasible)

    # Copying a SingleSolutionMetaheuristic instance should create a new instance with the same properties.
    def test_copy(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        initial_solution = TargetSolutionVoid("", 43, 43, 43, True)
        metaheuristic = SingleSolutionMetaheuristicVoid(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, initial_solution)
        # Act
        copied_metaheuristic = metaheuristic.copy()
        # Assert
        self.assertIsNot(metaheuristic, copied_metaheuristic)
        self.assertEqual(metaheuristic.name, copied_metaheuristic.name)
        self.assertEqual(metaheuristic.finish_control.criteria, copied_metaheuristic.finish_control.criteria)
        self.assertEqual(metaheuristic.finish_control.evaluations_max, 
                        copied_metaheuristic.finish_control.evaluations_max)
        self.assertEqual(metaheuristic.finish_control.iterations_max, 
                        copied_metaheuristic.finish_control.iterations_max)
        self.assertEqual(metaheuristic.finish_control.seconds_max, 
                        copied_metaheuristic.finish_control.seconds_max)
        self.assertEqual(metaheuristic.random_seed, copied_metaheuristic.random_seed)
        self.assertEqual(metaheuristic.additional_statistics_control.keep, 
                        copied_metaheuristic.additional_statistics_control.keep)
        self.assertEqual(metaheuristic.additional_statistics_control.max_local_optima, 
                        copied_metaheuristic.additional_statistics_control.max_local_optima)
        self.assertEqual(metaheuristic.output_control.fields, copied_metaheuristic.output_control.fields)
        self.assertEqual(metaheuristic.output_control.moments, copied_metaheuristic.output_control.moments)
        self.assertEqual(metaheuristic.target_problem.name, copied_metaheuristic.target_problem.name)
        self.assertEqual(metaheuristic.target_problem.is_minimization, 
                        copied_metaheuristic.target_problem.is_minimization)
        self.assertEqual(metaheuristic.current_solution.name, copied_metaheuristic.current_solution.name)
        self.assertEqual(metaheuristic.current_solution.random_seed, copied_metaheuristic.current_solution.random_seed)
        self.assertEqual(metaheuristic.current_solution.fitness_value, 
                        copied_metaheuristic.current_solution.fitness_value)
        self.assertEqual(metaheuristic.current_solution.objective_value, 
                        copied_metaheuristic.current_solution.objective_value)
        self.assertEqual(metaheuristic.current_solution.is_feasible, copied_metaheuristic.current_solution.is_feasible)

    # String representation of a SingleSolutionMetaheuristic instance should return a string with all properties and their values.
    def test_string_representation(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        initial_solution = TargetSolutionVoid("", 43, 43, 43, True)
        metaheuristic = SingleSolutionMetaheuristicVoid(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, initial_solution)
        # Act
        string_rep = str(metaheuristic)
        # Assert
        self.assertIn("name=", string_rep)
        self.assertIn("finish_control=", string_rep)
        self.assertIn("random_seed=12345", string_rep)
        self.assertIn("additional_statistics_control=", string_rep)
        self.assertIn("target_problem=", string_rep)
        self.assertIn("current_solution=", string_rep)

    # Formatted representation of a SingleSolutionMetaheuristic instance should return a string with all properties and their values formatted according to the given specification.
    def test_formatted_representation(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        initial_solution = TargetSolutionVoid("", 43, 43, 43, True)
        metaheuristic = SingleSolutionMetaheuristicVoid(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, initial_solution)
        spec = "|"
        # Act
        formatted_rep = metaheuristic.__format__(spec)
        # Assert
        self.assertIn("name=Metaheuristic", formatted_rep)
        self.assertIn("finish_control=", formatted_rep)
        self.assertIn("random_seed=12345", formatted_rep)
        self.assertIn("additional_statistics_control=", formatted_rep)
        self.assertIn("target_problem=", formatted_rep)
        self.assertIn("current_solution=", formatted_rep)

    # Creating a new instance of SingleSolutionMetaheuristic with invalid parameters should raise a TypeError.
    def test_invalid_parameters_initialization(self):
        # Arrange
        name = 12345
        finish_control = "FinishControl"
        random_seed = "12345"
        additional_statistics_control = "AdditionalStatisticsControl"
        output_control = "OutputControl"
        target_problem = "TargetProblem"
        initial_solution = "TargetSolution"
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristic(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, initial_solution)

    # Creating a new instance of SingleSolutionMetaheuristic with initial_solution=None should set current_solution to None.
    def test_initial_solution_none(self):
        # Arrange Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid("Metaheuristic", FinishControl(), 12345, 
                    AdditionalStatisticsControl(), OutputControl(), TargetProblemVoid("aaa", True), None)
        
    # Setting current_solution to an invalid value should raise a TypeError.
    def test_set_invalid_current_solution(self):
        # Arrange  
        invalid_solution = "InvalidSolution"
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid("Metaheuristic", FinishControl(), 12345, 
                    AdditionalStatisticsControl(), OutputControl(), TargetProblemVoid("aaa", True), 
                    invalid_solution)

    # SingleSolutionMetaheuristic should be able to handle problems with different types of solutions.
    def test_different_solution_types(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        initial_solution = TargetSolutionVoid("", 43, 43, 43, True)
        # Act
        metaheuristic = SingleSolutionMetaheuristicVoid(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, initial_solution)
        # Assert
        self.assertIsInstance(metaheuristic.current_solution, TargetSolution)


class TestCurrentSolution(unittest.TestCase):


    # Getting the current solution returns the value of __current_solution.
    def test_get_current_solution_returns_value(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        initial_solution = TargetSolutionVoid("", 43, 43, 43, True)
        metaheuristic = SingleSolutionMetaheuristicVoid(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, initial_solution)
        # Act
        current_solution = metaheuristic.current_solution
        # Assert
        self.assertEqual(current_solution.name, initial_solution.name)
        self.assertEqual(current_solution.random_seed, initial_solution.random_seed)
        self.assertEqual(current_solution.fitness_value, initial_solution.fitness_value)
        self.assertEqual(current_solution.objective_value, initial_solution.objective_value)
        self.assertEqual(current_solution.is_feasible, initial_solution.is_feasible)

    # Setting the current solution to None sets the value of __current_solution to None.
    def test_set_current_solution_to_none_sets_value_to_none(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        initial_solution = None
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, initial_solution)

    # Creating an object with solution that is not an instance of TargetSolution as the current solution raises a TypeError.
    def test_create_with_invalid_current_solution_raises_type_error(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        invalid_solution = "invalid"    
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, invalid_solution)

    # Creating an object with solution that is not an instance of TargetSolution as the current solution raises a TypeError.
    def test_create_with_invalid_current_solution_raises_type_error2(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        solution = TargetProblemVoid("xxx", True)    
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid(name, finish_control, random_seed, additional_statistics_control, 
                    output_control, target_problem, solution)


class Test__Str__2(unittest.TestCase):

    # Should return a string representation of the SingleSolutionMetaheuristic instance
    def test_return_string_representation(self):
        # Arrange
        metaheuristic = SingleSolutionMetaheuristicVoid(
            name="MyMetaheuristic",
            finish_control=FinishControl(),
            random_seed=123,
            additional_statistics_control=AdditionalStatisticsControl(),
            output_control=OutputControl(),
            target_problem=TargetProblemVoid("aaa", True),
            initial_solution=TargetSolutionVoid("", 43, 43, 43, True)
        )
        # Act
        result = str(metaheuristic)   
        # Assert
        self.assertIsInstance(result, str)

    # Should include the string representation of the Metaheuristic instance
    def test_include_metaheuristic_representation(self):
        # Arrange
        metaheuristic = SingleSolutionMetaheuristicVoid(
            name="MyMetaheuristic",
            finish_control=FinishControl(),
            random_seed=123,
            additional_statistics_control=AdditionalStatisticsControl(),
            output_control=OutputControl(),
            target_problem=TargetProblemVoid("aaa", True),
            initial_solution=TargetSolutionVoid("", 43, 43, 43, True)
        )
        # Act
        result = str(metaheuristic)    
        # Assert
        self.assertIn("name=MyMetaheuristic", result)

    # Should include the string representation of the current solution
    def test_include_current_solution_representation(self):
        # Arrange
        current_solution = TargetSolutionVoid("aaa", 43, 0, 0, False)
        metaheuristic = SingleSolutionMetaheuristicVoid(
            name="MyMetaheuristic",
            finish_control=FinishControl(),
            random_seed=123,
            additional_statistics_control=AdditionalStatisticsControl(),
            output_control=OutputControl(),
            target_problem=TargetProblemVoid("aaa", True),
            initial_solution=current_solution
        )
        # Act
        result = str(metaheuristic)
        # Assert
        self.assertIn("current_solution=" + str(current_solution), result)

    # Should raise TypeError if the initial solution is None
    def test_raise_typeerror_if_initial_solution_is_none(self):
        # Arrange & Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = SingleSolutionMetaheuristicVoid(
                name="MyMetaheuristic",
                finish_control=FinishControl(),
                random_seed=123,
                additional_statistics_control=AdditionalStatisticsControl(),
                output_control=OutputControl(),
                target_problem=TargetProblemVoid("aaa", True),
                initial_solution=None
            )
