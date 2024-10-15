import datetime
import unittest   
import unittest.mock as mocker

from uo.problem.problem import Problem
from uo.problem.problem_void_min_so import ProblemVoidMinSO

from uo.solution.solution import Solution
from uo.solution.solution_void_representation_int import SolutionVoidInt

from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic 
from uo.algorithm.metaheuristic.metaheuristic_void import MetaheuristicVoid

class TestMetaheuristicProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestMetaheuristicProperties\n")

    def setUp(self):
        self.metaheuristicName = 'Name of the metaheuristic'

        self.evaluations_max = 42
        self.iterations_max = 42
        self.seconds_max = 42
        self.finish_control_mock =  mocker.MagicMock(spec=FinishControl)
        type(self.finish_control_mock).evaluations_max = self.evaluations_max
        type(self.finish_control_mock).iterations_max = self.iterations_max
        type(self.finish_control_mock).seconds_max = self.seconds_max
        self.finish_control_mock.copy = mocker.Mock(return_value=self.finish_control_mock)

        self.random_seed = 42

        self.additional_statistics_control_stub = mocker.MagicMock(spec=AdditionalStatisticsControl)
        
        self.output_control_stub = mocker.MagicMock(spec=OutputControl)
  
        self.problem_mock = mocker.MagicMock(spec=ProblemVoidMinSO)
        type(self.problem_mock).name = 'some_problem'
        type(self.problem_mock).is_minimization = True
        self.problem_mock.copy = mocker.Mock(return_value=self.problem_mock)

        self.solution_mock = mocker.MagicMock(spec=SolutionVoidInt)
        type(self.solution_mock).name = 'some_solution'

        self.optimizer = MetaheuristicVoid(
                name=self.metaheuristicName,
                finish_control=self.finish_control_mock, 
                random_seed=self.random_seed, 
                additional_statistics_control=self.additional_statistics_control_stub, 
                output_control=self.output_control_stub,
                problem=self.problem_mock,
                solution_template=self.solution_mock
        )
    
    def test_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.name, self.metaheuristicName)

    def test_evaluations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.finish_control.evaluations_max, self.finish_control_mock.evaluations_max)

    def test_iterations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.finish_control.iterations_max, self.finish_control_mock.iterations_max)

    def test_seconds_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.finish_control.seconds_max, self.finish_control_mock.seconds_max)

    def test_random_seed_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.random_seed, self.random_seed)

    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.problem.name, self.problem_mock.name)

    def test_problem_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.problem.is_minimization, self.problem_mock.is_minimization)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestMetaheuristicProperties")


class TestMetaheuristic2(unittest.TestCase):

    # Create a new instance of Metaheuristic with valid parameters and call main_loop method to execute the algorithm
    def test_optimize_method(self):
        # Arrange
        evaluations_max = 42
        iterations_max = 1
        seconds_max = 42
        finish_control_mock =  mocker.MagicMock(spec=FinishControl)
        type(finish_control_mock).criteria = "iterations"
        type(finish_control_mock).evaluations_max = evaluations_max
        type(finish_control_mock).iterations_max = iterations_max
        type(finish_control_mock).seconds_max = seconds_max
        finish_control_mock.copy = mocker.Mock(return_value=finish_control_mock)
        random_seed = 42
        additional_statistics_control_stub = mocker.MagicMock(spec=AdditionalStatisticsControl)
        output_control_stub = mocker.MagicMock(spec=OutputControl)
        problem_mock = mocker.MagicMock(spec=ProblemVoidMinSO)
        type(problem_mock).name = 'some_problem'
        type(problem_mock).is_minimization = True
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        solution_mock =  mocker.MagicMock(spec=Solution)
        optimizer = MetaheuristicVoid(
                name="aaa",
                finish_control=finish_control_mock, 
                random_seed=random_seed, 
                additional_statistics_control=additional_statistics_control_stub, 
                output_control=output_control_stub,
                problem=problem_mock,
                solution_template=solution_mock
        )    
        # Act
        bs = optimizer.optimize()
        # Assert
        # Add assertions here to verify the expected behavior
        self.assertIsNotNone(optimizer.execution_started)
        self.assertIsNotNone(optimizer.execution_ended)
        self.assertLessEqual(optimizer.execution_started, optimizer.execution_ended)


    # Create a new instance of Metaheuristic with valid parameters and call main_loop method to execute the algorithm
    def test_main_loop_method(self):
        # Arrange
        evaluations_max = 42
        iterations_max = 2
        seconds_max = 42
        finish_control_mock =  mocker.MagicMock(spec=FinishControl)
        type(finish_control_mock).criteria = "iterations"
        type(finish_control_mock).evaluations_max = evaluations_max
        type(finish_control_mock).iterations_max = iterations_max
        type(finish_control_mock).seconds_max = seconds_max
        finish_control_mock.copy = mocker.Mock(return_value=finish_control_mock)
        random_seed = 42
        additional_statistics_control_stub = mocker.MagicMock(spec=AdditionalStatisticsControl)
        output_control_stub = mocker.MagicMock(spec=OutputControl)
        problem_mock = mocker.MagicMock(spec=ProblemVoidMinSO)
        type(problem_mock).name = 'some_problem'
        type(problem_mock).is_minimization = True
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        solution_mock =  mocker.MagicMock(spec=Solution)
        optimizer = MetaheuristicVoid(
                name="aaa",
                finish_control=finish_control_mock, 
                random_seed=random_seed, 
                additional_statistics_control=additional_statistics_control_stub, 
                output_control=output_control_stub,
                problem=problem_mock,
                solution_template=solution_mock
        )    
        optimizer.execution_started = datetime.datetime.now()
        # Act
        optimizer.main_loop() 
        # Assert
        # Add assertions here to verify the expected behavior
        self.assertIsNotNone(optimizer.evaluation)
        self.assertIsNotNone(optimizer.iteration)

    # Create a new instance of Metaheuristic with valid parameters and call string_rep method to get string representation of the instance
    def test_string_rep_method(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        output_control = OutputControl()
        problem = ProblemVoidMinSO("aaa", True)
        solution = SolutionVoidInt()
        metaheuristic = MetaheuristicVoid(name="Test", 
                            finish_control=finish_control, 
                            random_seed=random_seed,  
                            output_control=output_control, 
                            problem=problem, 
                            solution_template=solution)
        # Act
        result = metaheuristic.string_rep('|')
        # Assert
        # Add assertions here to verify the expected behavior
        self.assertIn("evaluation=", result)

    # Create a new instance of Metaheuristic with valid parameters and call elapsed_seconds method to get elapsed time
    def test_elapsed_seconds_method(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        output_control = OutputControl()
        problem = ProblemVoidMinSO()
        solution = SolutionVoidInt()
        metaheuristic = MetaheuristicVoid(name="Test", 
                            finish_control=finish_control, 
                            random_seed=random_seed,  
                            output_control=output_control, 
                            problem=problem, 
                            solution_template=solution)
        metaheuristic.execution_started = datetime.datetime.now()
        # Act
        result = metaheuristic.elapsed_seconds()
        # Assert
        # Add assertions here to verify the expected behavior
        self.assertGreaterEqual(result, 0)

    # Create a new instance of Metaheuristic with valid parameters and call copy method to get a new instance with the same properties
    def test_copy_method(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        output_control = OutputControl()
        problem = ProblemVoidMinSO()
        solution = SolutionVoidInt()
        metaheuristic = MetaheuristicVoid(name="Test", 
                            finish_control=finish_control, 
                            random_seed=random_seed,  
                            output_control=output_control, 
                            problem=problem, 
                            solution_template=solution)
        # Act
        copy_metaheuristic = metaheuristic.copy()
        # Assert
        # Add assertions here to verify the expected behavior
        self.assertEqual(metaheuristic.name, copy_metaheuristic.name)

    # Create a new instance of Metaheuristic with invalid name parameter and expect TypeError
    def test_invalid_name_parameter(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        problem = ProblemVoidMinSO("aaa", True)  
        solution_stub = mocker.Mock(Solution)  
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = MetaheuristicVoid(name=123, 
                            finish_control=finish_control, 
                            random_seed=random_seed,  
                            problem=problem, 
                            solution_template=solution_stub)

    # Create a new instance of Metaheuristic with invalid finish_control parameter and expect TypeError
    def test_invalid_finish_control_parameter(self):
        # Arrange
        name = "Test"
        random_seed = 12345
        problem = ProblemVoidMinSO("bbb", False)
        solution_stub = mocker.Mock(Solution)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic(name=name, 
                            finish_control="finish_control", 
                            random_seed=random_seed,  
                            problem=problem, 
                            solution_template=solution_stub)

    # Create a new instance of Metaheuristic with invalid random_seed parameter and expect TypeError
    def test_invalid_random_seed(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = "abc"
        problem = ProblemVoidMinSO('bbb', False)
        solution_stub = mocker.Mock(Solution)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic(name="Test", 
                            finish_control=finish_control, 
                            random_seed=random_seed,
                            problem=problem, 
                            solution_template=solution_stub)

    # Create a new instance of Metaheuristic with invalid additional_statistics_control parameter and expect TypeError
    def test_invalid_additional_statistics_control(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = "abc"
        problem = ProblemVoidMinSO('bbb', False)
        solution_stub = mocker.Mock(Solution)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic(name="Test", 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                additional_statistics_control=additional_statistics_control, 
                                porblem=problem, 
                                solution_template=solution_stub)

    # Create a new instance of Metaheuristic with invalid output_control parameter and expect TypeError
    def test_invalid_output_control(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        output_control = "abc"
        problem = ProblemVoidMinSO('bbb', False)
        solution_stub = mocker.Mock(Solution)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic(name="Test", 
                                finish_control=finish_control, 
                                random_seed=random_seed,  
                                output_control=output_control, 
                                problem=problem, 
                                solution_template=solution_stub)

    # Create a new instance of Metaheuristic with invalid problem parameter and expect TypeError
    def test_invalid_problem_parameter(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        problem = "invalid_problem"
        solution_stub = mocker.Mock(Solution)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic(name="Test", 
                                finish_control=finish_control, 
                                random_seed=random_seed, 
                                problem=problem, 
                                solution_template=solution_stub)

    # Call main_loop method with finish_control that is already finished and expect the loop to not execute
    def test_main_loop_finished(self):
        # Arrange
        finish_mock = mocker.Mock(FinishControl)
        finish_mock.is_finished.return_value = True
        random_seed = 12345
        output_control_stub = mocker.Mock(OutputControl)
        problem_stub = mocker.Mock(Problem)
        solution_stub = mocker.Mock(Solution)
        metaheuristic = MetaheuristicVoid(name="Test", 
                                finish_control=finish_mock, 
                                random_seed=random_seed, 
                                output_control=output_control_stub, 
                                problem=problem_stub, 
                                solution_template=solution_stub)
        metaheuristic.execution_started = datetime.datetime.now()
        # Act
        metaheuristic.main_loop()
        # Assert
        metaheuristic.finish_control.is_finished.assert_called_once()

    # Call optimize method with random_seed equal to None and expect a random seed to be generated
    def test_optimize_random_seed(self):
        # Arrange
        finish_mock = mocker.Mock(FinishControl)
        finish_mock.is_finished.return_value = True
        random_seed = None
        problem_stub = mocker.Mock(Problem)
        solution_stub = mocker.Mock(Solution)
        metaheuristic = MetaheuristicVoid(name="Test", 
                            finish_control=finish_mock, 
                            random_seed=random_seed,  
                            problem= problem_stub, 
                            solution_template=solution_stub)
        metaheuristic.write_output_headers_if_needed = mocker.Mock(return_value=None)
        metaheuristic.write_output_values_if_needed = mocker.Mock(return_value=None)
        # Act
        bs = metaheuristic.optimize()
        # Assert
        assert isinstance(metaheuristic.random_seed, int)


class TestFinishControl(unittest.TestCase):

    # Returns the structure that controls finish criteria for metaheuristic execution.
    def test_returns_finish_control_structure(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        problem_stub = mocker.Mock(Problem)
        solution_stub = mocker.Mock(Solution)
        metaheuristic = MetaheuristicVoid(name="Test", 
                            finish_control=finish_control, 
                            random_seed=random_seed, 
                            problem=problem_stub, 
                            solution_template=solution_stub)
        # Act
        result = metaheuristic.finish_control
        # Assert
        self.assertEqual(result.criteria, finish_control.criteria)
        self.assertEqual(result.evaluations_max, finish_control.evaluations_max)
        self.assertEqual(result.iterations_max, finish_control.iterations_max)
        self.assertEqual(result.seconds_max, finish_control.seconds_max)

    # Returns the same instance of FinishControl every time it is called.
    def test_returns_same_instance_of_finish_control(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        problem_stub = mocker.Mock(Problem)
        solution_stub = mocker.Mock(Solution)
        metaheuristic = MetaheuristicVoid(name="Test", 
                            finish_control=finish_control, 
                            random_seed=random_seed, 
                            problem=problem_stub, 
                            solution_template=solution_stub)
        # Act
        result1 = metaheuristic.finish_control
        result2 = metaheuristic.finish_control    
        # Assert
        self.assertEqual(result1.criteria, result2.criteria)
        self.assertEqual(result1.evaluations_max, result2.evaluations_max)
        self.assertEqual(result1.iterations_max, result2.iterations_max)
        self.assertEqual(result1.seconds_max, result2.seconds_max)

    # Raises a TypeError if the FinishControl instance is not of type FinishControl.
    def test_raises_type_error_if_finish_control_not_of_type_finish_control(self):
        # Arrange
        finish_control = "not a FinishControl instance"
        random_seed = None
        additional_statistics_control = mocker.Mock(AdditionalStatisticsControl)
        output_control = mocker.Mock(OutputControl)
        problem_stub = mocker.Mock(Problem)
        solution_stub = mocker.Mock(Solution)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, 
                                            output_control, problem_stub, solution_stub)

    # The FinishControl instance returned is identical to the one set during initialization.
    def test_returns_identical_finish_control(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        problem_stub = mocker.Mock(Problem)
        solution_stub = mocker.Mock(Solution)
        metaheuristic = MetaheuristicVoid(name="Test", 
                            finish_control=finish_control, 
                            random_seed=random_seed, 
                            problem=problem_stub, 
                            solution_template=solution_stub)
        # Act
        result = metaheuristic.finish_control
        # Assert
        self.assertIsInstance(result, FinishControl)
        self.assertEqual(result.criteria, finish_control.criteria)
        self.assertEqual(result.evaluations_max, finish_control.evaluations_max)
        self.assertEqual(result.iterations_max, finish_control.iterations_max)
        self.assertEqual(result.seconds_max, finish_control.seconds_max)



class TestRandomSeed(unittest.TestCase):

    # Returns the random seed used during metaheuristic execution.
    def test_returns_random_seed(self):
        # Arrange
        metaheuristic = MetaheuristicVoid(name="MyMetaheuristic", 
                                finish_control=FinishControl(), 
                                random_seed=12345, 
                                problem=ProblemVoidMinSO(), 
                                solution_template=SolutionVoidInt())    
        # Act
        seed = metaheuristic.random_seed
        # Assert
        self.assertEqual(seed, 12345)

    # Returns the correct random seed value when it is set to a non-zero integer.
    def test_returns_correct_random_seed_value(self):
        # Arrange
        metaheuristic = MetaheuristicVoid(finish_control=FinishControl(), 
                                random_seed=54321, 
                                problem=ProblemVoidMinSO(), 
                                solution_template=SolutionVoidInt())
        # Act
        seed = metaheuristic.random_seed
        # Assert
        self.assertEqual(seed, 54321)

    # Raises a TypeError when the random seed is not an integer or None.
    def test_raises_type_error_when_random_seed_not_integer_or_none(self):
        # Arrange & Act & Assert
        with self.assertRaises(TypeError):
            MetaheuristicVoid(finish_control=FinishControl(), 
                                random_seed="abc", 
                                problem=ProblemVoidMinSO(), 
                                solution_template=SolutionVoidInt())

    # Raises no errors when the random seed is set to 0.
    def test_raises_no_errors_when_random_seed_is_zero(self):
        # Arrange
        metaheuristic = MetaheuristicVoid(finish_control=FinishControl(), 
                                random_seed=0, 
                                problem=ProblemVoidMinSO(), 
                                solution_template=SolutionVoidInt())
        # Act
        seed = metaheuristic.random_seed
        # Assert
        self.assertNotEqual(seed, 0)


class TestAdditionalStatisticsControl(unittest.TestCase):

    # Returns the structure that controls keeping of the statistic during metaheuristic execution.
    def test_returns_additional_statistics_control(self):
        # Arrange
        additional_statistics_control = AdditionalStatisticsControl()
        metaheuristic = MetaheuristicVoid(name="test", 
                            finish_control=FinishControl(), 
                            random_seed=None, 
                            additional_statistics_control=additional_statistics_control, 
                            problem=ProblemVoidMinSO(),
                            solution_template = SolutionVoidInt())
        # Act
        result = metaheuristic.additional_statistics_control
        # Assert
        self.assertEqual(result, additional_statistics_control)

    # Returns an instance of AdditionalStatisticsControl.
    def test_returns_instance_of_additional_statistics_control(self):
        # Arrange
        additional_statistics_control = AdditionalStatisticsControl()
        metaheuristic = MetaheuristicVoid(name="test", 
                            finish_control=FinishControl(), 
                            random_seed=None, 
                            additional_statistics_control=additional_statistics_control,  
                            problem=ProblemVoidMinSO(),
                            solution_template=SolutionVoidInt())
        # Act
        result = metaheuristic.additional_statistics_control
        # Assert
        self.assertIsInstance(result, AdditionalStatisticsControl)

    # The returned instance is the same as the one passed in the constructor.
    def test_returns_same_instance_as_passed_in_constructor(self):
        # Arrange
        additional_statistics_control = AdditionalStatisticsControl()
        metaheuristic = MetaheuristicVoid(name="test", 
                            finish_control=FinishControl(), 
                            random_seed=None, 
                            additional_statistics_control=additional_statistics_control,  
                            problem=ProblemVoidMinSO(),
                            solution_template = SolutionVoidInt()) 
        # Act
        result = metaheuristic.additional_statistics_control
        # Assert
        self.assertIs(result, additional_statistics_control)

    # The instance returned is not modified.
    def test_returns_unmodified_instance2(self):
        # Arrange
        additional_statistics_control = AdditionalStatisticsControl()
        metaheuristic = MetaheuristicVoid(name="test", 
                            finish_control=FinishControl(), 
                            random_seed=None, 
                            additional_statistics_control=additional_statistics_control,  
                            problem=ProblemVoidMinSO(),
                            solution_template = SolutionVoidInt())
        # Act
        result = metaheuristic.additional_statistics_control
        # Assert
        self.assertEqual(result, additional_statistics_control)

class TestMainLoopIteration(unittest.TestCase):

    # Executes one iteration of the main loop of the metaheuristic algorithm
    def test_executes_one_iteration(self):
        # Arrange
        metaheuristic = MetaheuristicVoid(name="Example Metaheuristic",
                                    finish_control=FinishControl(),
                                    random_seed=123,
                                    problem=ProblemVoidMinSO(),
                                    solution_template=SolutionVoidInt())
        # Act
        metaheuristic.main_loop_iteration()
        # Assert
        # Check that the evaluation counter is updated
        self.assertEqual(metaheuristic.evaluation, 0)
        # Check that the iteration counter is updated
        self.assertEqual(metaheuristic.iteration, 0)

    # When the finish control structure indicates that the algorithm is finished, the method should exit without executing any iteration
    def test_finish_control_indicates_algorithm_finished(self):
        # Arrange
        finish_control = FinishControl()
        finish_control.is_finished = mocker.MagicMock(return_value=True)    
        metaheuristic = MetaheuristicVoid(name="Example Metaheuristic",
                                    finish_control=finish_control,
                                    random_seed=123,
                                    problem=ProblemVoidMinSO("aaa", False),
                                    solution_template=SolutionVoidInt())
    
        # Act
        metaheuristic.main_loop_iteration()
        # Assert
        # Add assertions here
        # Check that the evaluation counter is not updated
        self.assertEqual(metaheuristic.evaluation, 0)
        # Check that the iteration counter is not updated
        self.assertEqual(metaheuristic.iteration, 0)



class TestStringRep(unittest.TestCase):

    # Returns a string representation of the Metaheuristic instance.
    def test_returns_string_representation(self):
        # Arrange
        metaheuristic = MetaheuristicVoid(name="example", 
                            finish_control=FinishControl(), 
                            random_seed=1234, 
                            problem=ProblemVoidMinSO("aaa"), 
                            solution_template=SolutionVoidInt())    
        # Act
        result = metaheuristic.string_rep("|")
        # Assert
        self.assertIsInstance(result, str)

    # Uses the delimiter, indentation, indentation_symbol, group_start, and group_end parameters to format the string.
    def test_uses_formatting_parameters(self):
        # Arrange
        metaheuristic = MetaheuristicVoid(name="example", 
                            finish_control=FinishControl(), 
                            random_seed=1234, 
                            problem=ProblemVoidMinSO(), 
                            solution_template=SolutionVoidInt())
        # Act
        result = metaheuristic.string_rep("|", indentation=2, indentation_symbol="-", group_start="[", group_end="]")
        # Assert
        self.assertIn("|", result)
        self.assertIn("--{", result)
        self.assertIn("random_seed=", result)
        self.assertIn("finish_control=", result)
        self.assertIn("additional_statistics_control=", result)
        self.assertIn("]", result)

    # delimiter parameter is an empty string.
    def test_empty_delimiter(self):
        # Arrange
        metaheuristic = MetaheuristicVoid(name="example", 
                            finish_control=FinishControl(), 
                            random_seed=1234, 
                            problem=ProblemVoidMinSO("aaa", False), 
                            solution_template=SolutionVoidInt())
        # Act
        result = metaheuristic.string_rep("")
        # Assert
        self.assertIsInstance(result, str)
        
        
if __name__ == '__main__':
    unittest.main()