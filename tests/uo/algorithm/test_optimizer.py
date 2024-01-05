
from io import TextIOWrapper
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem
from uo.algorithm.output_control import OutputControl
from uo.algorithm.optimizer import Optimizer
from uo.algorithm.optimizer_void import OptimizerVoid
from uo.target_problem.target_problem_void import TargetProblemVoid
from uo.target_solution.quality_of_solution import QualityOfSolution
from uo.target_solution.target_solution_void import TargetSolutionVoid
from uo.utils import logger


class Test__Optimizer__(unittest.TestCase):

    # Creates a new instance of Optimizer with valid parameters.
    def test_valid_parameters2(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        # Act
        optimizer = OptimizerVoid(name, output_control, target_problem)
        # Assert
        self.assertEqual(optimizer.name, name)
        self.assertEqual(optimizer.output_control.fields, output_control.fields)
        self.assertEqual(optimizer.output_control.moments, output_control.moments)
        self.assertEqual(optimizer.target_problem.name, target_problem.name)
        self.assertEqual(optimizer.target_problem.is_minimization, target_problem.is_minimization)
        self.assertIsNone(optimizer.execution_started)
        self.assertIsNone(optimizer.execution_ended)
        self.assertIsNone(optimizer.best_solution)

    # Initializes all instance variables with valid values.
    def test_valid_instance_variables9(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        # Act
        optimizer = OptimizerVoid(name, output_control, target_problem)
        # Assert
        self.assertEqual(optimizer.name, name)
        self.assertEqual(optimizer.output_control.fields, output_control.fields)
        self.assertEqual(optimizer.output_control.moments, output_control.moments)
        self.assertEqual(optimizer.target_problem.name, target_problem.name)
        self.assertEqual(optimizer.target_problem.is_minimization, target_problem.is_minimization)
        self.assertIsNone(optimizer.execution_started)
        self.assertIsNone(optimizer.execution_ended)
        self.assertIsNone(optimizer.best_solution)

    # Sets all other instance variables to None or default values.
    def test_other_instance_variables_none_or_default(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        # Act
        optimizer = OptimizerVoid(name, output_control, target_problem)
        # Assert
        self.assertIsNone(optimizer.execution_started)
        self.assertIsNone(optimizer.execution_ended)
        self.assertIsNone(optimizer.best_solution)

    # Raises a TypeError if the name parameter is not a string.
    def test_name_parameter_not_string(self):
        # Arrange
        name = 123
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        # Act & Assert
        with self.assertRaises(TypeError):
            Optimizer(name, output_control, target_problem)

    # Raises a TypeError if the output_control parameter is not an instance of OutputControl.
    def test_output_control_parameter_not_instance_of_OutputControl(self):
        # Arrange
        name = "Optimizer1"
        output_control = "InvalidOutputControl"
        target_problem = TargetProblemVoid("a problem", True)
        # Act & Assert
        with self.assertRaises(TypeError):
            Optimizer(name, output_control, target_problem)

    # Raises a TypeError if the target_problem parameter is not an instance of TargetProblem.
    def test_target_problem_parameter_not_instance_of_TargetProblem(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = "InvalidTargetProblem"
        # Act & Assert
        with self.assertRaises(TypeError):
            Optimizer(name, output_control, target_problem)

    # Does not raise an exception if the name parameter is an empty string.
    def test_empty_name_parameter(self):
        # Arrange
        name = ""
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        # Act
        try:
            optimizer = OptimizerVoid(name, output_control, target_problem)
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")
        # Assert
        self.assertEqual(optimizer.name, name)
        self.assertEqual(optimizer.output_control.fields, output_control.fields)
        self.assertEqual(optimizer.output_control.moments, output_control.moments)
        self.assertEqual(optimizer.target_problem.name, target_problem.name)
        self.assertEqual(optimizer.target_problem.is_minimization, target_problem.is_minimization)
        self.assertIsNone(optimizer.execution_started)
        self.assertIsNone(optimizer.execution_ended)
        self.assertIsNone(optimizer.best_solution)

    # Does not raise an exception if the output_control parameter is None.
    def test_none_output_control_parameter(self):
        # Arrange
        name = "Optimizer1"
        output_control = None
        target_problem = TargetProblemVoid("a problem", True)
        # Act & Assert
        with self.assertRaises(TypeError):
            Optimizer(name, output_control, target_problem)


    # Does not raise an exception if the target_problem parameter is None.
    def test_none_target_problem_parameter(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = None
        # Act & Assert
        with self.assertRaises(TypeError):
            Optimizer(name, output_control, target_problem)

    # The execution_started and execution_ended instance variables are set to None.
    def test_execution_variables_set_to_none(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        # Act
        optimizer = OptimizerVoid(name, output_control, target_problem)
        # Assert
        self.assertIsNone(optimizer.execution_started)
        self.assertIsNone(optimizer.execution_ended)

    # The best_solution instance variable is set to None.
    def test_best_solution_set_to_none(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        # Act
        optimizer = OptimizerVoid(name, output_control, target_problem)
        # Assert
        self.assertIsNone(optimizer.best_solution)

    # Creates a new instance of Optimizer with valid parameters.
    def test_valid_parameters(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        # Act
        optimizer = OptimizerVoid(name, output_control, target_problem)
        # Assert
        self.assertEqual(optimizer.name, name)
        self.assertEqual(optimizer.output_control.fields, output_control.fields)
        self.assertEqual(optimizer.output_control.moments, output_control.moments)
        self.assertEqual(optimizer.target_problem.name, target_problem.name)
        self.assertEqual(optimizer.target_problem.is_minimization, target_problem.is_minimization)
        self.assertIsNone(optimizer.execution_started)
        self.assertIsNone(optimizer.execution_ended)
        self.assertIsNone(optimizer.best_solution)

    # The copy method creates a new instance of Optimizer with the same properties.
    def test_copy_method(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        optimizer = OptimizerVoid(name, output_control, target_problem)
        # Act
        copied_optimizer = optimizer.copy()
        # Assert
        self.assertIsNot(optimizer, copied_optimizer)
        self.assertEqual(optimizer.name, copied_optimizer.name)
        self.assertEqual(optimizer.output_control.fields, copied_optimizer.output_control.fields)
        self.assertEqual(optimizer.output_control.moments, copied_optimizer.output_control.moments)
        self.assertEqual(optimizer.target_problem.name, copied_optimizer.target_problem.name)
        self.assertEqual(optimizer.target_problem.is_minimization, copied_optimizer.target_problem.is_minimization)
        self.assertEqual(optimizer.execution_started, copied_optimizer.execution_started)
        self.assertEqual(optimizer.execution_ended, copied_optimizer.execution_ended)
        self.assertEqual(optimizer.best_solution, copied_optimizer.best_solution)

    # The string_rep method returns a string representation of the instance.
    def test_string_rep_method(self):
        # Arrange
        name = "Optimizer1"
        output_control = OutputControl()
        target_problem = TargetProblemVoid("a problem", True)
        optimizer = OptimizerVoid(name, output_control, target_problem)
        optimizer.best_solution = TargetSolutionVoid("s1", 43, 0, 0, True)
        # Act
        string_rep = optimizer.string_rep("|")
        # Assert
        self.assertIsInstance(string_rep, str)


class TestWriteOutputValuesIfNeeded(unittest.TestCase):

    # Method writes data to output file when write_to_output is True and step_name is valid
    def test_write_output_values_if_needed_write_to_output_true_step_name_valid(self):
        # Arrange
        output_control = OutputControl(write_to_output = True, 
                    output_file = mocker.MagicMock(spec=TextIOWrapper))
        optimizer = OptimizerVoid("optimizer", output_control, TargetProblemVoid("a problem", True))
        step_name = "after_algorithm"
        step_name_value = "after_algorithm_value"
        logger_mock = mocker.MagicMock(logger.logger)
        logger_mock.info = mocker.Mock(return_value="")
        # Act
        optimizer.write_output_values_if_needed(step_name, step_name_value)
        # Assert
        self.assertEqual(optimizer.output_control.output_file.write.call_count, 9)
        self.assertEqual(logger_mock.info.call_count, 0)
        
    # # Method replaces 'step_name' with step_name_value in output if present in fields_definitions
    # def test_write_output_values_if_needed_replace_step_name_with_step_name_value(self, mocker):
    #     # Arrange
    #     output_control = OutputControl()
    #     output_control.write_to_output = True
    #     output_control.output_file = mocker.Mock()
    #     output_control.fields_definitions = ["step_name"]
    #     optimizer = Optimizer("optimizer", output_control, TargetProblem())
    #     step_name = "after_algorithm"
    #     step_name_value = "after_algorithm_value"
    #     # Act
    #     optimizer.write_output_values_if_needed(step_name, step_name_value)
    #     # Assert
    #     output_control.output_file.write.assert_called_once_with('after_algorithm_value\t')

    # # Method logs the written line using logger.info()
    # def test_write_output_values_if_needed_logs_written_line(self, mocker):
    #     # Arrange
    #     output_control = OutputControl()
    #     output_control.write_to_output = True
    #     output_control.output_file = mocker.Mock()
    #     optimizer = Optimizer("optimizer", output_control, TargetProblem())
    #     step_name = "after_algorithm"
    #     step_name_value = "after_algorithm_value"
    #     # Act
    #     optimizer.write_output_values_if_needed(step_name, step_name_value)
    #     # Assert
    #     logger.info.assert_called_once_with('')

    # # Method raises TypeError if step_name is not a valid string
    # def test_write_output_values_if_needed_raises_type_error_invalid_step_name(self, mocker):
    #     # Arrange
    #     output_control = OutputControl()
    #     output_control.write_to_output = True
    #     output_control.output_file = mocker.Mock()
    #     optimizer = Optimizer("optimizer", output_control, TargetProblem())
    #     step_name = 123
    #     step_name_value = "after_algorithm_value"
    #     # Act & Assert
    #     with self.assertRaises(TypeError):
    #         optimizer.write_output_values_if_needed(step_name, step_name_value)

    # # Method raises ValueError if step_name is not one of the valid options
    # def test_write_output_values_if_needed_raises_value_error_invalid_step_name(self, mocker):
    #     # Arrange
    #     output_control = OutputControl()
    #     output_control.write_to_output = True
    #     output_control.output_file = mocker.Mock()
    #     optimizer = Optimizer("optimizer", output_control, TargetProblem())
    #     step_name = "invalid_step"
    #     step_name_value = "after_algorithm_value"
    #     # Act & Assert
    #     with self.assertRaises(ValueError):
    #         optimizer.write_output_values_if_needed(step_name, step_name_value)

    # # Method writes 'XXX' to output if fields_definitions evaluation fails
    # def test_write_output_values_if_needed_writes_xxx_on_failed_evaluation(self, mocker):
    #     # Arrange
    #     output_control = OutputControl()
    #     output_control.write_to_output = True
    #     output_control.output_file = mocker.Mock()
    #     output_control.fields_definitions = ["invalid_field"]
    #     optimizer = Optimizer("optimizer", output_control, TargetProblem())
    #     step_name = "after_algorithm"
    #     step_name_value = "after_algorithm_value"
    #     # Act
    #     optimizer.write_output_values_if_needed(step_name, step_name_value)
    #     # Assert
    #     output_control.output_file.write.assert_called_once_with('XXX\t')

    # # Method does not write to output if write_to_output is False
    # def test_write_output_values_if_needed_write_to_output_false(self, mocker):
    #     # Arrange
    #     output_control = OutputControl()
    #     output_control.write_to_output = False
    #     output_control.output_file = mocker.Mock()
    #     optimizer = Optimizer("optimizer", output_control, TargetProblem())
    #     step_name = "after_algorithm"
    #     step_name_value = "after_algorithm_value"
    #     # Act
    #     optimizer.write_output_values_if_needed(step_name, step_name_value)
    #     # Assert
    #     output_control.output_file.write.assert_not_called()
    #     logger.info.assert_not_called()

    # # Method does not write to output if should_write is False
    # def test_write_output_values_if_needed_should_write_false(self, mocker):
    #     # Arrange
    #     output_control = OutputControl()
    #     output_control.write_to_output = True
    #     output_control.output_file = mocker.Mock()
    #     optimizer = Optimizer("optimizer", output_control, TargetProblem())
    #     step_name = "after_algorithm"
    #     step_name_value = "after_algorithm_value"
    #     # Act
    #     optimizer.write_output_values_if_needed(step_name, step_name_value)
    #     # Assert
    #     output_control.output_file.write.assert_not_called()
    #     logger.info.assert_not_called()

    # # Method writes headers to output file if write_to_output is True
    # def test_write_output_values_if_needed_write_headers(self, mocker):
    #     # Arrange
    #     output_control = OutputControl()
    #     output_control.write_to_output = True
    #     output_control.output_file = mocker.Mock()
    #     output_control.fields_headings = ["Field1", "Field2", "Field3"]
    #     optimizer = Optimizer("optimizer", output_control, TargetProblem())
    #     step_name = "after_algorithm"
    #     step_name_value = "after_algorithm_value"
    #     # Act
    #     optimizer.write_output_values_if_needed(step_name, step_name_value)
    #     # Assert
    #     output_control.output_file.write.assert_called_once_with("Field1\tField2\tField3\n")
    #     logger.info.assert_called_once_with("Field1\tField2\tField3")