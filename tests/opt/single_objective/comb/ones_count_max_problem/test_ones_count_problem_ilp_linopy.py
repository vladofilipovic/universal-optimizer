import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_ilp_linopy import OnesCountMaxProblemIntegerLinearProgrammingSolution
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_ilp_linopy import OnesCountMaxProblemIntegerLinearProgrammingSolver
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_ilp_linopy import OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters
from uo.problem.problem import Problem
from uo.problem.problem_void import ProblemVoid
from uo.solution.solution import Solution
from uo.algorithm.output_control import OutputControl

class TestOnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(unittest.TestCase):

    # Creating an instance of the class with default parameters should not raise any exceptions
    def test_default_parameters_no_exceptions(self):
        # Arrange
        # Act
        params = OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=OutputControl(),
                                        problem=ProblemVoid("a", True))
        # Assert
        self.assertIsInstance(params, OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters)

    # Creating an instance of the class with valid OutputControl and Problem parameters should not raise any exceptions
    def test_valid_parameters_no_exceptions(self):
        # Arrange
        output_control = OutputControl(write_to_output=True)
        problem = OnesCountMaxProblem(dim=3)
        # Act
        params = OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=output_control, 
                                        problem=problem)
        # Assert
        self.assertIsInstance(params, OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters)

    # Creating an instance of the class with invalid OutputControl parameter should raise a TypeError
    def test_invalid_output_control_type(self):
        # Arrange
        invalid_output_control = "invalid"
        problem = OnesCountMaxProblem(dim=3)
    
        # Act & Assert
        with self.assertRaises(TypeError):
            params = OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(
                output_control=invalid_output_control, problem=problem)

    # Creating an instance of the class with invalid Problem parameter should raise a TypeError
    def test_invalid_problem_type(self):
        # Arrange
        output_control = OutputControl(write_to_output=True)
        invalid_problem = "invalid"
    
        # Act & Assert
        with self.assertRaises(TypeError):
            params = OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=output_control, problem=invalid_problem)