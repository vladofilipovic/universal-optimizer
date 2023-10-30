""" 
The :mod:`opt.single_objective.teaching.max_function_1_variable_problem_solver` contains programming code that optimize :ref:`Max Function 1 Variable Problem` with various optimization techniques.
"""
import sys


from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from dataclasses import dataclass

from random import randrange
from random import seed
from datetime import datetime

from bitstring import BitArray

import xarray as xr
from linopy import Model

from uo.utils.files import ensure_dir 
from uo.utils.logger import logger

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.optimizer import Optimizer
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer
from uo.algorithm.exact.total_enumeration.problem_solution_te_support import ProblemSolutionTeSupport

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import \
    ProblemSolutionVnsSupport

from opt.single_objective.teaching.max_function_1_variable_problem.max_function_1_variable_problem import \
        MaxFunctionOneVariableProblem

from opt.single_objective.teaching.max_function_1_variable_problem.max_function_1_variable_problem_binary_int_solution \
        import MaxFunctionOneVariableProblemBinaryIntSolution
from opt.single_objective.teaching.max_function_1_variable_problem.\
        max_function_1_variable_problem_binary_int_solution_vns_support import \
        MaxFunctionOneVariableProblemBinaryIntSolutionVnsSupport

@dataclass
class MaxFunctionOneVariableProblemSolverConstructionParameters:
    """
    Instance of the class :class:`MaxFunctionOneVariableProblemSolverConstructionParameters` represents constructor parameters for max ones problem solver.
    """
    method: str = None
    finish_control: FinishControl = None
    output_control: OutputControl = None
    target_problem: TargetProblem = None
    initial_solution: TargetSolution = None
    vns_problem_solution_support: ProblemSolutionVnsSupport = None
    vns_random_seed: int = None
    vns_additional_statistics_control: AdditionalStatisticsControl = None
    vns_k_min: int = None
    vns_k_max: int = None
    vns_local_search_type: str = None

class MaxFunctionOneVariableProblemSolver:
    """
    Instance of the class :class:`MaxFunctionOneVariableProblemSolver` any of the developed solvers max ones problem.
    """
    def __init__(self, method:str=None,
            finish_control:FinishControl = None,
            output_control:OutputControl = None,
            target_problem:TargetProblem = None,
            initial_solution:TargetSolution = None,
            vns_problem_solution_support:ProblemSolutionVnsSupport = None,
            vns_random_seed:int = None,
            vns_additional_statistics_control:AdditionalStatisticsControl = None,
            vns_k_min:int = None,
            vns_k_max:int = None,
            vns_local_search_type:str = None,
    )->None:
        """
        Create new `MaxFunctionOneVariableProblemSolver` instance

        :param str method: method used for solving the Max Ones Problem 
        :param FinishControl finish_control: controls finish criteria
        :param output_control:OutputControl = controls output
        :param TargetProblem target_problem: problem that is solved
        :param TargetSolution initial_solution: initial solution
        :param ProblemSolutionVnsSupport vns_problem_solution_support: Specific VNS support
        :param int vns_random_seed: random seed
        :param AdditionalStatisticsControl vns_additional_statistics_control: additional statistics control
        :param int vns_k_min: VNS parameter k_min
        :param int vns_k_max: VNS parameter k_max
        :param str vns_local_search_type: type of the local search        
        """
        self.__optimizer:Optimizer = None
        if method == 'variable_neighborhood_search':
            self.__optimizer = VnsOptimizer(
                    finish_control= finish_control,
                    output_control= output_control,
                    target_problem= target_problem,
                    initial_solution= initial_solution,
                    problem_solution_vns_support= vns_problem_solution_support,
                    random_seed= vns_random_seed, 
                    additional_statistics_control= vns_additional_statistics_control,
                    k_min= vns_k_min,
                    k_max= vns_k_max,
                    local_search_type= vns_local_search_type)
        else:
            raise ValueError("Invalid optimization method {} - should be: '{}'.".format(method,
                    'variable_neighborhood_search'))

    @classmethod
    def from_construction_tuple(cls, construction_params:MaxFunctionOneVariableProblemSolverConstructionParameters=None):
        """
        Additional constructor. Create new `MaxFunctionOneVariableProblemSolver` instance from construction parameters

        :param `MaxFunctionOneVariableProblemSolverConstructionParameters` construction_params: parameters for construction 
        """
        return cls(
            method = construction_params.method,
            finish_control = construction_params.finish_control,
            output_control = construction_params.output_control,
            target_problem = construction_params.target_problem,
            initial_solution = construction_params.initial_solution,
            vns_problem_solution_support = construction_params.vns_problem_solution_support,
            vns_random_seed = construction_params.vns_random_seed, 
            vns_additional_statistics_control = construction_params.vns_additional_statistics_control,
            vns_k_min = construction_params.vns_k_min,
            vns_k_max = construction_params.vns_k_max,
            vns_local_search_type = construction_params.vns_local_search_type,
        )

    @classmethod
    def from_variable_neighborhood_search(cls, vns_construction_params:VnsOptimizerConstructionParameters=None):
        """
        Additional constructor. Create new `MaxOnesProblemSolver` instance when solving method is `Variable Neighborhood Search`

        :param VnsOptimizerConstructionParameters vns_construction_params: construction parameters 
        """
        params:MaxFunctionOneVariableProblemSolverConstructionParameters = \
                MaxFunctionOneVariableProblemSolverConstructionParameters()
        params.method:str = 'variable_neighborhood_search'
        params.finish_control:FinishControl = vns_construction_params.finish_control
        params.output_control:OutputControl = vns_construction_params.output_control
        params.target_problem:TargetProblem = vns_construction_params.target_problem
        params.initial_solution:TargetSolution = vns_construction_params.initial_solution
        params.vns_problem_solution_support:ProblemSolutionVnsSupport = \
                vns_construction_params.problem_solution_vns_support
        params.vns_random_seed:int = vns_construction_params.random_seed
        params.vns_additional_statistics_control:AdditionalStatisticsControl = \
                vns_construction_params.additional_statistics_control
        params.vns_k_min:int = vns_construction_params.k_min
        params.vns_k_max:int = vns_construction_params.k_max
        params.vns_local_search_type:str = vns_construction_params.local_search_type        
        return cls.from_construction_tuple(params)

    @property
    def opt(self)->Optimizer:
        """
        Property getter for the optimizer used for solving

        :return: optimizer
        :rtype: `Optimizer`
        """
        return self.__optimizer

