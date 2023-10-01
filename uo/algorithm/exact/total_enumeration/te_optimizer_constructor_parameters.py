""" 
The :mod:`~uo.algorithm.exact.total_enumerations` module describes the class :class:`~uo.algorithm.exact.total_enumeration.TotalEnumerationConstructorParameters`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

from dataclasses import dataclass

from uo.utils.logger import logger

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.output_control import OutputControl
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.exact.total_enumeration.problem_solution_te_support import ProblemSolutionTeSupport

@dataclass
class TeOptimizerConstructionParameters:
    """
    Instance of the class :class:`~uo.algorithm.exact.total_enumerations.TotalEnumerationConstructorParameters` represents constructor parameters for total enumeration algorithm.
    """
    output_control:OutputControl = None
    target_problem:TargetProblem = None
    initial_solution:TargetSolution = None
    problem_solution_te_support:ProblemSolutionTeSupport = None



