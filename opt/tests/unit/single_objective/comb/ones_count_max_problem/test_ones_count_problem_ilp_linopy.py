import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_ilp_linopy import MaxOnesCountProblemIntegerLinearProgrammingSolution
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_ilp_linopy import MaxOnesCountProblemIntegerLinearProgrammingSolver
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_ilp_linopy import MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters
from uo.problem.problem import Problem
from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.solution.solution import Solution
from uo.algorithm.output_control import OutputControl

class TestMaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(unittest.TestCase):

    # Creating an instance of the class with default parameters should not raise any exceptions
    def test_default_parameters_no_exceptions(self):
        # Arrange
        # Act
        params = MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=None,
                                        problem=ProblemVoidMinSO("a", True))
        # Assert
        self.assertIsInstance(params, MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters)

    # Creating an instance of the class with valid OutputControl and Problem parameters should not raise any exceptions
    def test_valid_parameters_no_exceptions(self):
        # Arrange
        problem = MaxOnesCountProblem(dim=3)
        # Act
        params = MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=None, 
                                        problem=problem)
        # Assert
        self.assertIsInstance(params, MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters)

    # Creating an instance of the class with invalid OutputControl parameter should raise a TypeError
    def test_invalid_output_control_type(self):
        # Arrange
        invalid_output_control = "invalid"
        problem = MaxOnesCountProblem(dim=3)
    
        # Act & Assert
        with self.assertRaises(TypeError):
            params = MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(
                output_control=invalid_output_control, problem=problem)

    # Creating an instance of the class with invalid Problem parameter should raise a TypeError
    def test_invalid_problem_type(self):
        # Arrange
        output_control = OutputControl()
        invalid_problem = "invalid"
    
        # Act & Assert
        with self.assertRaises(TypeError):
            params = MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control=output_control, problem=invalid_problem)