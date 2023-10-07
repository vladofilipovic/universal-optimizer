""" 
..  _py_vns_optimizer:

The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer_constructor_parameters` contains class :class:`~.algorithm.metaheuristic.variable_neighborhood_search_constructor_parameters.VnsOptimizerConstructorParameters`.
"""

from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import \
        ProblemSolutionVnsSupport
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.output_control import OutputControl
from uo.target_solution.target_solution import TargetSolution
from uo.target_problem.target_problem import TargetProblem
from uo.utils.logger import logger
from dataclasses import dataclass
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)


@dataclass
class VnsOptimizerConstructionParameters:
        """
        Instance of the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search_constructor_parameters.
        VnsOptimizerConstructionParameters` represents constructor parameters for VNS algorithm.
        """
        finish_control: FinishControl = None
        output_control: OutputControl = None
        target_problem: TargetProblem = None
        initial_solution: TargetSolution = None
        problem_solution_vns_support: ProblemSolutionVnsSupport = None
        random_seed: int = None
        additional_statistics_control: AdditionalStatisticsControl = None
        k_min: int = None
        k_max: int = None
        local_search_type: str = None
