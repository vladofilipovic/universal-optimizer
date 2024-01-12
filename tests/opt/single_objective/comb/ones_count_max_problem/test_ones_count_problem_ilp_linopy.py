import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_ilp_linopy import OnesCountMaxProblemIntegerLinearProgrammingSolution
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_ilp_linopy import OnesCountMaxProblemIntegerLinearProgrammingSolver
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_ilp_linopy import OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters
from uo.target_problem.target_problem import TargetProblem
from uo.target_problem.target_problem_void import TargetProblemVoid
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.output_control import OutputControl

class TestOnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(unittest.TestCase):

    # Creating an instance of the class with default parameters should not raise any exceptions
    def test_default_parameters_no_exceptions(self):
        # Arrange
        # Act
        params = OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=OutputControl(),
                                        target_problem=TargetProblemVoid("a", True))
        # Assert
        self.assertIsInstance(params, OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters)

    # Creating an instance of the class with valid OutputControl and TargetProblem parameters should not raise any exceptions
    def test_valid_parameters_no_exceptions(self):
        # Arrange
        output_control = OutputControl(write_to_output=True)
        target_problem = OnesCountMaxProblem(dim=3)
        # Act
        params = OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=output_control, 
                                        target_problem=target_problem)
        # Assert
        self.assertIsInstance(params, OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters)

    # Creating an instance of the class with invalid OutputControl parameter should raise a TypeError
    def test_invalid_output_control_type(self):
        # Arrange
        invalid_output_control = "invalid"
        target_problem = OnesCountMaxProblem(dim=3)
    
        # Act & Assert
        with self.assertRaises(TypeError):
            params = OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(
                output_control=invalid_output_control, target_problem=target_problem)

    # Creating an instance of the class with invalid TargetProblem parameter should raise a TypeError
    def test_invalid_target_problem_type(self):
        # Arrange
        output_control = OutputControl(write_to_output=True)
        invalid_target_problem = "invalid"
    
        # Act & Assert
        with self.assertRaises(TypeError):
            params = OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=output_control, target_problem=invalid_target_problem)