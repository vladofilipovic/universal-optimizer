
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem
from uo.algorithm.output_control import OutputControl
from uo.algorithm.optimizer import Optimizer
from uo.algorithm.algorithm_void import AlgorithmVoid
from uo.target_problem.target_problem_void import TargetProblemVoid
from uo.target_solution.quality_of_solution import QualityOfSolution
from uo.target_solution.target_solution_void import TargetSolutionVoid