import datetime
import unittest   
import unittest.mock as mocker

from uo.target_problem.target_problem import TargetProblem
from uo.target_problem.target_problem_void import TargetProblemVoid
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
        type(self.output_control_stub).write_to_output = False

        self.problem_mock = mocker.MagicMock(spec=TargetProblemVoid)
        type(self.problem_mock).name = 'some_problem'
        type(self.problem_mock).is_minimization = True
        self.problem_mock.copy = mocker.Mock(return_value=self.problem_mock)

        self.optimizer = MetaheuristicVoid(
                name=self.metaheuristicName,
                finish_control=self.finish_control_mock, 
                random_seed=self.random_seed, 
                additional_statistics_control=self.additional_statistics_control_stub, 
                output_control=self.output_control_stub,
                target_problem=self.problem_mock
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
        self.assertEqual(self.optimizer.target_problem.name, self.problem_mock.name)

    def test_problem_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.target_problem.is_minimization, self.problem_mock.is_minimization)

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
        type(output_control_stub).write_to_output = False
        problem_mock = mocker.MagicMock(spec=TargetProblemVoid)
        type(problem_mock).name = 'some_problem'
        type(problem_mock).is_minimization = True
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        optimizer = MetaheuristicVoid(
                name="aaa",
                finish_control=finish_control_mock, 
                random_seed=random_seed, 
                additional_statistics_control=additional_statistics_control_stub, 
                output_control=output_control_stub,
                target_problem=problem_mock
        )    
        # Act
        optimizer.optimize()
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
        type(output_control_stub).write_to_output = False
        problem_mock = mocker.MagicMock(spec=TargetProblemVoid)
        type(problem_mock).name = 'some_problem'
        type(problem_mock).is_minimization = True
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        optimizer = MetaheuristicVoid(
                name="aaa",
                finish_control=finish_control_mock, 
                random_seed=random_seed, 
                additional_statistics_control=additional_statistics_control_stub, 
                output_control=output_control_stub,
                target_problem=problem_mock
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
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)
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
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)
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
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)
        metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)
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
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("aaa", True)    
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = MetaheuristicVoid(123, finish_control, random_seed, additional_statistics_control, output_control, target_problem)

    # Create a new instance of Metaheuristic with invalid finish_control parameter and expect TypeError
    def test_invalid_finish_control_parameter(self):
        # Arrange
        name = "Test"
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid("bbb", False)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic(name, "finish_control", random_seed, additional_statistics_control, output_control, target_problem)

    # Create a new instance of Metaheuristic with invalid random_seed parameter and expect TypeError
    def test_invalid_random_seed(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = "abc"
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = TargetProblemVoid('bbb', False)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)

    # Create a new instance of Metaheuristic with invalid additional_statistics_control parameter and expect TypeError
    def test_invalid_additional_statistics_control(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = "abc"
        output_control = OutputControl()
        target_problem = TargetProblemVoid('bbb', False)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)

    # Create a new instance of Metaheuristic with invalid output_control parameter and expect TypeError
    def test_invalid_output_control(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = "abc"
        target_problem = TargetProblemVoid('bbb', False)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)

    # Create a new instance of Metaheuristic with invalid target_problem parameter and expect TypeError
    def test_invalid_target_problem_parameter(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 12345
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        target_problem = "invalid_target_problem"
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = Metaheuristic("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)


    # Call main_loop method with finish_control that is already finished and expect the loop to not execute
    def test_main_loop_finished(self):
        # Arrange
        finish_control = mocker.Mock(FinishControl)
        finish_control.is_finished.return_value = True
        random_seed = 12345
        additional_statistics_control = mocker.Mock(AdditionalStatisticsControl)
        output_control = mocker.Mock(OutputControl)
        target_problem = mocker.Mock(TargetProblem)
        metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)
        metaheuristic.execution_started = datetime.datetime.now()
        # Act
        metaheuristic.main_loop()
        # Assert
        metaheuristic.finish_control.is_finished.assert_called_once()

    # Call optimize method with random_seed equal to None and expect a random seed to be generated
    def test_optimize_random_seed(self):
        # Arrange
        finish_control = mocker.Mock(FinishControl)
        finish_control.is_finished.return_value = True
        random_seed = None
        additional_statistics_control = mocker.Mock(AdditionalStatisticsControl)
        output_control = mocker.Mock(OutputControl)
        target_problem = mocker.Mock(TargetProblem)
        metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)
        metaheuristic.write_output_headers_if_needed = mocker.Mock(return_value=None)
        metaheuristic.write_output_values_if_needed = mocker.Mock(return_value=None)
        # Act
        metaheuristic.optimize()
        # Assert
        assert isinstance(metaheuristic.random_seed, int)


class TestFinishControl(unittest.TestCase):

    # Returns the structure that controls finish criteria for metaheuristic execution.
    def test_returns_finish_control_structure(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        additional_statistics_control = mocker.Mock(AdditionalStatisticsControl)
        output_control = mocker.Mock(OutputControl)
        target_problem = mocker.Mock(TargetProblem)
        metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)
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
        additional_statistics_control = mocker.Mock(AdditionalStatisticsControl)
        output_control = mocker.Mock(OutputControl)
        target_problem = mocker.Mock(TargetProblem)
        metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)
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
        target_problem = mocker.Mock(TargetProblem)
        # Act & Assert
        with self.assertRaises(TypeError):
            metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)

    # The FinishControl instance returned is identical to the one set during initialization.
    def test_returns_identical_finish_control(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        additional_statistics_control = mocker.Mock(AdditionalStatisticsControl)
        output_control = mocker.Mock(OutputControl)
        target_problem = mocker.Mock(TargetProblem)
        metaheuristic = MetaheuristicVoid("Test", finish_control, random_seed, additional_statistics_control, output_control, target_problem)
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
        metaheuristic = MetaheuristicVoid("MyMetaheuristic", FinishControl(), 12345, AdditionalStatisticsControl(), 
                                        OutputControl(), TargetProblemVoid("aaa", False))    
        # Act
        seed = metaheuristic.random_seed
        # Assert
        self.assertEqual(seed, 12345)

    # Returns the correct random seed value when it is set to a non-zero integer.
    def test_returns_correct_random_seed_value(self):
        # Arrange
        metaheuristic = MetaheuristicVoid("MyMetaheuristic", FinishControl(), 54321, AdditionalStatisticsControl(), 
                                        OutputControl(), TargetProblemVoid("aaa", False))
        # Act
        seed = metaheuristic.random_seed
        # Assert
        self.assertEqual(seed, 54321)

    # Raises a TypeError when the random seed is not an integer or None.
    def test_raises_type_error_when_random_seed_not_integer_or_none(self):
        # Arrange & Act & Assert
        with self.assertRaises(TypeError):
            MetaheuristicVoid("MyMetaheuristic", FinishControl(), "abc", AdditionalStatisticsControl(), 
                                    OutputControl(), TargetProblemVoid("aaa", False))

    # Raises no errors when the random seed is set to 0.
    def test_raises_no_errors_when_random_seed_is_zero(self):
        # Arrange
        metaheuristic = MetaheuristicVoid("MyMetaheuristic", FinishControl(), 0, AdditionalStatisticsControl(), 
                                    OutputControl(), TargetProblemVoid("aaa", False))
        # Act
        seed = metaheuristic.random_seed
        # Assert
        self.assertNotEqual(seed, 0)


class TestAdditionalStatisticsControl(unittest.TestCase):

    # Returns the structure that controls keeping of the statistic during metaheuristic execution.
    def test_returns_additional_statistics_control(self):
        # Arrange
        additional_statistics_control = AdditionalStatisticsControl()
        metaheuristic = MetaheuristicVoid(name="test", finish_control=FinishControl(), random_seed=None, 
                    additional_statistics_control=additional_statistics_control, output_control=OutputControl(), 
                    target_problem=TargetProblemVoid("aaa", False),
                    solution_template = None)
        # Act
        result = metaheuristic.additional_statistics_control
        # Assert
        self.assertEqual(result, additional_statistics_control)

    # Returns an instance of AdditionalStatisticsControl.
    def test_returns_instance_of_additional_statistics_control(self):
        # Arrange
        additional_statistics_control = AdditionalStatisticsControl()
        metaheuristic = MetaheuristicVoid(name="test", finish_control=FinishControl(), random_seed=None, 
                    additional_statistics_control=additional_statistics_control, output_control=OutputControl(), 
                    target_problem=TargetProblemVoid("aaa", False))
        # Act
        result = metaheuristic.additional_statistics_control
        # Assert
        self.assertIsInstance(result, AdditionalStatisticsControl)

    # The returned instance is the same as the one passed in the constructor.
    def test_returns_same_instance_as_passed_in_constructor(self):
        # Arrange
        additional_statistics_control = AdditionalStatisticsControl()
        metaheuristic = MetaheuristicVoid(name="test", finish_control=FinishControl(), random_seed=None, 
                    additional_statistics_control=additional_statistics_control, output_control=OutputControl(), 
                    target_problem=TargetProblemVoid("aaa", False)) 
        # Act
        result = metaheuristic.additional_statistics_control
        # Assert
        self.assertIs(result, additional_statistics_control)

    # The instance returned is not modified.
    def test_returns_unmodified_instance2(self):
        # Arrange
        additional_statistics_control = AdditionalStatisticsControl()
        metaheuristic = MetaheuristicVoid(name="test", finish_control=FinishControl(), random_seed=None, 
                    additional_statistics_control=additional_statistics_control, output_control=OutputControl(), 
                    target_problem=TargetProblemVoid("aaa", False))
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
                                    additional_statistics_control=AdditionalStatisticsControl(),
                                    output_control=OutputControl(),
                                    target_problem=TargetProblemVoid("aaa", False))
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
                                    additional_statistics_control=AdditionalStatisticsControl(),
                                    output_control=OutputControl(),
                                    target_problem=TargetProblemVoid("aaa", False))
    
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
        metaheuristic = MetaheuristicVoid("example", FinishControl(), 1234, AdditionalStatisticsControl(), 
                    OutputControl(), TargetProblemVoid("aaa", False))    
        # Act
        result = metaheuristic.string_rep("|")
        # Assert
        self.assertIsInstance(result, str)

    # Uses the delimiter, indentation, indentation_symbol, group_start, and group_end parameters to format the string.
    def test_uses_formatting_parameters(self):
        # Arrange
        metaheuristic = MetaheuristicVoid("example", FinishControl(), 1234, AdditionalStatisticsControl(), 
                    OutputControl(), TargetProblemVoid("aaa", False))
        # Act
        result = metaheuristic.string_rep("|", indentation=2, indentation_symbol="-", group_start="[", group_end="]")
        # Assert
        self.assertIn("|", result)
        self.assertIn("--{", result)
        self.assertIn("random_seed=", result)
        self.assertIn("finish_control=", result)
        self.assertIn("additional_statistics_control=", result)
        self.assertIn("]", result)

    # Includes the random_seed, finish_control, and additional_statistics_control properties in the string.
    def test_includes_properties(self):
        # Arrange
        metaheuristic = MetaheuristicVoid("example", FinishControl(), 1234, AdditionalStatisticsControl(), 
                    OutputControl(), TargetProblemVoid("aaa", False))
        # Act
        result = metaheuristic.string_rep("|")
        # Assert
        self.assertIn("random_seed=", result)
        self.assertIn("finish_control=", result)
        self.assertIn("additional_statistics_control=", result)

    # delimiter parameter is an empty string.
    def test_empty_delimiter(self):
        # Arrange
        metaheuristic = MetaheuristicVoid("example", FinishControl(), 1234, AdditionalStatisticsControl(), 
                    OutputControl(), TargetProblemVoid("aaa", False))
        # Act
        result = metaheuristic.string_rep("")
        # Assert
        self.assertIsInstance(result, str)
        
        
if __name__ == '__main__':
    unittest.main()