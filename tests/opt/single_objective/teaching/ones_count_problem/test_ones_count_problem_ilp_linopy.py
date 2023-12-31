import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_ilp_linopy import OnesCountProblemIntegerLinearProgrammingSolution
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_ilp_linopy import OnesCountProblemIntegerLinearProgrammingSolver
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_ilp_linopy import OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters
from uo.target_problem.target_problem import TargetProblem
from uo.target_problem.target_problem_void import TargetProblemVoid
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.output_control import OutputControl

class TestOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(unittest.TestCase):

    # Creating an instance of the class with default parameters should not raise any exceptions
    def test_default_parameters_no_exceptions(self):
        # Arrange
        # Act
        params = OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=OutputControl(),
                                        target_problem=TargetProblemVoid("a", True))
        # Assert
        self.assertIsInstance(params, OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters)

    # Creating an instance of the class with valid OutputControl and TargetProblem parameters should not raise any exceptions
    def test_valid_parameters_no_exceptions(self):
        # Arrange
        output_control = OutputControl(write_to_output=True)
        target_problem = OnesCountProblem(dim=3)
        # Act
        params = OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=output_control, 
                                        target_problem=target_problem)
        # Assert
        self.assertIsInstance(params, OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters)

    # Creating an instance of the class with invalid OutputControl parameter should raise a TypeError
    def test_invalid_output_control_type(self):
        # Arrange
        invalid_output_control = "invalid"
        target_problem = OnesCountProblem(dim=3)
    
        # Act & Assert
        with self.assertRaises(TypeError):
            params = OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(
                output_control=invalid_output_control, target_problem=target_problem)

    # Creating an instance of the class with invalid TargetProblem parameter should raise a TypeError
    def test_invalid_target_problem_type(self):
        # Arrange
        output_control = OutputControl(write_to_output=True)
        invalid_target_problem = "invalid"
    
        # Act & Assert
        with self.assertRaises(TypeError):
            params = OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=output_control, target_problem=invalid_target_problem)