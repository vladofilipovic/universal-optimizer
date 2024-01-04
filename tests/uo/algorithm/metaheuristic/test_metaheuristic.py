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


if __name__ == '__main__':
    unittest.main()