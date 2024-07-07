import datetime
import unittest   
import unittest.mock as mocker
from uo.algorithm.metaheuristic.single_solution_metaheuristic_void import SingleSolutionMetaheuristicVoid

from uo.problem.problem import Problem
from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic 
from uo.algorithm.metaheuristic.single_solution_metaheuristic import SingleSolutionMetaheuristic
from uo.solution.solution import Solution
from uo.solution.solution_void_representation_int import SolutionVoidInt

class TestSingleSolutionMetaheuristic(unittest.TestCase):

    # Creating a new instance of SingleSolutionMetaheuristic with valid parameters should initialize all properties correctly.
    def test_valid_parameters_initialization(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)
        solution_template = SolutionVoidInt(43, 43, 43, True)
        # Act
        metaheuristic = SingleSolutionMetaheuristicVoid(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution_template)
        # Assert
        self.assertEqual(metaheuristic.finish_control.criteria, finish_control.criteria)
        self.assertEqual(metaheuristic.finish_control.evaluations_max, finish_control.evaluations_max)
        self.assertEqual(metaheuristic.finish_control.iterations_max, finish_control.iterations_max)
        self.assertEqual(metaheuristic.finish_control.seconds_max, finish_control.seconds_max)
        self.assertEqual(metaheuristic.random_seed, random_seed)
        self.assertEqual(metaheuristic.problem.name, problem.name)
        self.assertEqual(metaheuristic.problem.is_minimization, problem.is_minimization)
        self.assertEqual(metaheuristic.solution_template.random_seed, solution_template.random_seed)
        self.assertEqual(metaheuristic.solution_template.fitness_value, solution_template.fitness_value)
        self.assertEqual(metaheuristic.solution_template.objective_value, solution_template.objective_value)
        self.assertEqual(metaheuristic.solution_template.is_feasible, solution_template.is_feasible)

    # Copying a SingleSolutionMetaheuristic instance should create a new instance with the same properties.
    def test_copy(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)
        solution_template = SolutionVoidInt(43, 43, 43, True)
        metaheuristic = SingleSolutionMetaheuristicVoid(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution_template)
        # Act
        copied_metaheuristic = metaheuristic.copy()
        # Assert
        self.assertIsNot(metaheuristic, copied_metaheuristic)
        self.assertEqual(metaheuristic.finish_control.criteria, copied_metaheuristic.finish_control.criteria)
        self.assertEqual(metaheuristic.finish_control.evaluations_max, 
                        copied_metaheuristic.finish_control.evaluations_max)
        self.assertEqual(metaheuristic.finish_control.iterations_max, 
                        copied_metaheuristic.finish_control.iterations_max)
        self.assertEqual(metaheuristic.finish_control.seconds_max, 
                        copied_metaheuristic.finish_control.seconds_max)
        self.assertEqual(metaheuristic.random_seed, copied_metaheuristic.random_seed)
        self.assertEqual(metaheuristic.problem.name, copied_metaheuristic.problem.name)
        self.assertEqual(metaheuristic.problem.is_minimization, 
                        copied_metaheuristic.problem.is_minimization)
        self.assertEqual(metaheuristic.solution_template.random_seed, copied_metaheuristic.solution_template.random_seed)
        self.assertEqual(metaheuristic.solution_template.fitness_value, 
                        copied_metaheuristic.solution_template.fitness_value)
        self.assertEqual(metaheuristic.solution_template.objective_value, 
                        copied_metaheuristic.solution_template.objective_value)
        self.assertEqual(metaheuristic.solution_template.is_feasible, copied_metaheuristic.solution_template.is_feasible)

    # String representation of a SingleSolutionMetaheuristic instance should return a string with all properties and their values.
    def test_string_representation(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)
        solution_template = SolutionVoidInt(43, 43, 43, True)
        metaheuristic = SingleSolutionMetaheuristicVoid(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution_template)
        # Act
        string_rep = str(metaheuristic)
        # Assert
        self.assertIn("finish_control=", string_rep)
        self.assertIn("random_seed=12345", string_rep)
        self.assertIn("additional_statistics_control=", string_rep)
        self.assertIn("problem=", string_rep)
        self.assertIn("current_solution=", string_rep)

    # Formatted representation of a SingleSolutionMetaheuristic instance should return a string with all properties and their values formatted according to the given specification.
    def test_formatted_representation(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)
        solution_template = SolutionVoidInt(43, 43, 43, True)
        metaheuristic = SingleSolutionMetaheuristicVoid(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution_template)
        spec = "|"
        # Act
        formatted_rep = metaheuristic.__format__(spec)
        # Assert
        self.assertIn("name=Metaheuristic", formatted_rep)
        self.assertIn("finish_control=", formatted_rep)
        self.assertIn("random_seed=12345", formatted_rep)
        self.assertIn("additional_statistics_control=", formatted_rep)
        self.assertIn("problem=", formatted_rep)
        self.assertIn("current_solution=", formatted_rep)

    # Creating a new instance of SingleSolutionMetaheuristic with invalid parameters should raise a TypeError.
    def test_invalid_parameters_initialization(self):
        # Arrange
        name = 12345
        finish_control = "FinishControl"
        random_seed = "12345"
        additional_statistics_control = "AdditionalStatisticsControl"
        output_control = "OutputControl"
        problem = "Problem"
        solution_template = "Solution"
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristic(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution_template,
                                additional_statistics_control=additional_statistics_control,
                                output_control=output_control
                        )

    # Creating a new instance of SingleSolutionMetaheuristic with solution_template=None should set current_solution to None.
    def test_solution_template_not_solution(self):
        # Arrange Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid(
                name = "Metaheuristic", 
                finish_control=FinishControl(), 
                random_seed=12345, 
                problem=ProblemVoidMinSO("aaa", True), 
                solution_template="invalid solution")
    # Setting current_solution to an invalid value should raise a TypeError.
    def test_set_invalid_current_solution(self):
        # Arrange  
        invalid_solution = "InvalidSolution"
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid("Metaheuristic", FinishControl(), 12345, 
                    AdditionalStatisticsControl(), OutputControl(), ProblemVoidMinSO("aaa", True), 
                    invalid_solution)

    # SingleSolutionMetaheuristic should be able to handle problems with different types of solutions.
    def test_different_solution_types(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)
        solution_template = SolutionVoidInt(43, 43, 43, True)
        # Act
        metaheuristic = SingleSolutionMetaheuristicVoid(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution_template
                        )
        # Assert
        self.assertIsInstance(metaheuristic.solution_template, Solution)


class TestCurrentSolution(unittest.TestCase):


    # Getting the current solution returns the value of __current_solution.
    def test_get_current_solution_returns_value(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)
        solution_template = SolutionVoidInt(43, 43, 43, True)
        metaheuristic = SingleSolutionMetaheuristicVoid(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution_template
                        )
        # Act
        current_solution = metaheuristic.solution_template
        # Assert
        self.assertEqual(current_solution.random_seed, solution_template.random_seed)
        self.assertEqual(current_solution.fitness_value, solution_template.fitness_value)
        self.assertEqual(current_solution.objective_value, solution_template.objective_value)
        self.assertEqual(current_solution.is_feasible, solution_template.is_feasible)

    # Setting the current solution to None sets the value of __current_solution to None.
    def test_set_solution_template_to_not_Target_solution(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)
        solution_template = "invalid solution"
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution_template
                        )

    # Creating an object with solution that is not an instance of Solution as the current solution raises a TypeError.
    def test_create_with_invalid_current_solution_raises_type_error(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)
        invalid_solution = "invalid"    
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=invalid_solution
                        )

    # Creating an object with solution that is not an instance of Solution as the current solution raises a TypeError.
    def test_create_with_invalid_current_solution_raises_type_error2(self):
        # Arrange
        name = "Metaheuristic"
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)
        solution = ProblemVoidMinSO("xxx", True)    
        # Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid(name=name, 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution
                        )


class Test__Str__2(unittest.TestCase):

    # Should return a string representation of the SingleSolutionMetaheuristic instance
    def test_return_string_representation(self):
        # Arrange
        metaheuristic = SingleSolutionMetaheuristicVoid(
            name="MyMetaheuristic",
            finish_control=FinishControl(),
            random_seed=123,
            problem=ProblemVoidMinSO("aaa", True),
            solution_template=SolutionVoidInt(43, 43, 43, True)
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
            problem=ProblemVoidMinSO("aaa", True),
            solution_template=SolutionVoidInt(43, 43, 43, True)
        )
        # Act
        result = str(metaheuristic)    
        # Assert
        self.assertIn("name=MyMetaheuristic", result)

    # Should include the string representation of the current solution
    def test_include_current_solution_representation(self):
        # Arrange
        current_solution = SolutionVoidInt(43, 0, 0, False)
        metaheuristic = SingleSolutionMetaheuristicVoid(
            name="MyMetaheuristic",
            finish_control=FinishControl(),
            random_seed=123,
            problem=ProblemVoidMinSO("aaa", True),
            solution_template=current_solution
        )
        # Act
        result = str(metaheuristic)
        # Assert
        self.assertIn("current_solution=", result)

    # Should raise TypeError if the initial solution is None
    def test_raise_typeerror_if_solution_template_is_not_solution(self):
        # Arrange & Act & Assert
        with self.assertRaises(TypeError):
            SingleSolutionMetaheuristicVoid(
                name="MyMetaheuristic",
                finish_control=FinishControl(),
                random_seed=123,
                problem=ProblemVoidMinSO("aaa", True),
                solution_template="invalid solution"
            )
