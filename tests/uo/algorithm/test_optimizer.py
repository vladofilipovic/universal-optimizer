
import unittest   
import unittest.mock as mocker

from datetime import datetime
from io import TextIOWrapper
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
        optimizer.execution_started = datetime.now()
        optimizer.best_solution = TargetSolutionVoid(43, 0, 0, True)
        # Act
        string_rep = optimizer.string_rep("|")
        # Assert
        self.assertIsInstance(string_rep, str)
