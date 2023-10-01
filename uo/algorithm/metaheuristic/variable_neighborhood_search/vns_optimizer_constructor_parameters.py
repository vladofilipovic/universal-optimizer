""" 
..  _py_vns_optimizer:

The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer_constructor_parameters` contains class :class:`~.algorithm.metaheuristic.variable_neighborhood_search_constructor_parameters.VnsOptimizerConstructorParameters`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from dataclasses import dataclass

from uo.utils.logger import logger

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import ProblemSolutionVnsSupport

@dataclass
class VnsOptimizerConstructionParameters:
    """
    Instance of the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search_constructor_parameters.VnsOptimizerConstructionParameters` represents constructor parameters for VNS algorithm.
    """
    evaluations_max:int = None 
    iterations_max:int = None 
    seconds_max:int = None
    random_seed:int = None
    keep_all_solution_codes:bool = None
    distance_calculation_cache_is_used:bool = None
    output_control:OutputControl = None
    target_problem:TargetProblem = None
    initial_solution:TargetSolution = None
    problem_solution_vns_support:ProblemSolutionVnsSupport = None
    k_min:int = None
    k_max:int = None
    max_local_optima:int = None
    local_search_type:str = None

