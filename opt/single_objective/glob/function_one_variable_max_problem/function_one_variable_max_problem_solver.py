""" 
The :mod:`opt.single_objective.glob.function_one_variable_max_problem_solver` contains programming code that optimize :ref:`Problem_Function_One_Variable_Max` with various optimization techniques.
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

from uo.problem.problem import Problem
from uo.solution.solution import Solution

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

from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem import \
        FunctionOneVariableMaxProblemMax

from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem_binary_int_solution \
        import FunctionOneVariableMaxProblemBinaryIntSolution
from opt.single_objective.glob.function_one_variable_max_problem.\
        function_one_variable_max_problem_binary_int_solution_vns_support import \
        FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport

@dataclass
class FunctionOneVariableMaxProblemSolverConstructionParameters:
        """
        Instance of the class :class:`FunctionOneVariableMaxProblemSolverConstructionParameters` represents constructor parameters for max ones problem solver.
        """
        method: str = None
        finish_control: FinishControl = None
        output_control: OutputControl = None
        problem: Problem = None
        solution_template: Solution = None
        vns_problem_solution_support: ProblemSolutionVnsSupport = None
        vns_random_seed: int = None
        vns_additional_statistics_control: AdditionalStatisticsControl = None
        vns_k_min: int = None
        vns_k_max: int = None
        vns_local_search_type: str = None

class FunctionOneVariableMaxProblemSolver:
        """
        Instance of the class :class:`FunctionOneVariableMaxProblemSolver` any of the developed solvers max ones problem.
        """
        def __init__(self, method:str=None,
                finish_control:FinishControl = None,
                output_control:OutputControl = None,
                problem:Problem = None,
                solution_template:Solution = None,
                vns_problem_solution_support:ProblemSolutionVnsSupport = None,
                vns_random_seed:int = None,
                vns_additional_statistics_control:AdditionalStatisticsControl = None,
                vns_k_min:int = None,
                vns_k_max:int = None,
                vns_local_search_type:str = None,
        )->None:
                """
                Create new `FunctionOneVariableMaxProblemSolver` instance

                :param str method: method used for solving the Max Ones Problem 
                :param FinishControl finish_control: controls finish criteria
                :param output_control:OutputControl = controls output
                :param Problem problem: problem that is solved
                :param Solution solution_template: initial solution
                :param ProblemSolutionVnsSupport vns_problem_solution_support: Specific VNS support
                :param int vns_random_seed: random seed
                :param AdditionalStatisticsControl vns_additional_statistics_control: additional statistics control
                :param int vns_k_min: VNS parameter k_min
                :param int vns_k_max: VNS parameter k_max
                :param str vns_local_search_type: type of the local search        
                """
                if not isinstance(method, str):
                        raise TypeError('Parameter \'method\' must be \'str\'.')
                self.__optimizer:Optimizer = None
                if method == 'variable_neighborhood_search':
                        if not isinstance(finish_control, FinishControl):
                                raise TypeError('Parameter \'finish_control\' must be \'FinishControl\'.')
                        if not isinstance(output_control, OutputControl):
                                raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
                        if not isinstance(problem, Problem):
                                raise TypeError('Parameter \'problem\' must be \'Problem\'.')
                        if not isinstance(solution_template, Solution):
                                raise TypeError('Parameter \'solution_template\' must be \'Solution\'.')
                        if not isinstance(vns_problem_solution_support, ProblemSolutionVnsSupport):
                                raise TypeError('Parameter \'vns_problem_solution_support\' must be \'ProblemSolutionVnsSupport\'.')
                        if not isinstance(vns_random_seed, int):
                                raise TypeError('Parameter \'vns_random_seed\' must be \'int\'.')
                        if not isinstance(vns_additional_statistics_control, AdditionalStatisticsControl):
                                raise TypeError('Parameter \'vns_additional_statistics_control\' must be \'AdditionalStatisticsControl\'.')
                        if not isinstance(vns_k_min, int):
                                raise TypeError('Parameter \'vns_k_min\' must be \'int\'.')
                        if not isinstance(vns_k_max, int):
                                raise TypeError('Parameter \'vns_k_max\' must be \'int\'.')
                        if not isinstance(vns_local_search_type, str):
                                raise TypeError('Parameter \'vns_local_search_type\' must be \'str\'.')
                        self.__optimizer = VnsOptimizer(
                                finish_control= finish_control,
                                output_control= output_control,
                                problem= problem,
                                solution_template= solution_template,
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
        def from_construction_tuple(cls, construction_params:FunctionOneVariableMaxProblemSolverConstructionParameters=None):
                """
                Additional constructor. Create new `FunctionOneVariableMaxProblemSolver` instance from construction parameters

                :param `FunctionOneVariableMaxProblemSolverConstructionParameters` construction_params: parameters for construction 
                """
                return cls(
                        method = construction_params.method,
                        finish_control = construction_params.finish_control,
                        output_control = construction_params.output_control,
                        problem = construction_params.problem,
                        solution_template = construction_params.solution_template,
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
                Additional constructor. Create new `OnesCountMaxProblemSolver` instance when solving method is `Variable Neighborhood Search`

                :param VnsOptimizerConstructionParameters vns_construction_params: construction parameters 
                """
                params:FunctionOneVariableMaxProblemSolverConstructionParameters = \
                        FunctionOneVariableMaxProblemSolverConstructionParameters()
                params.method:str = 'variable_neighborhood_search'
                params.finish_control:FinishControl = vns_construction_params.finish_control
                params.output_control:OutputControl = vns_construction_params.output_control
                params.problem:Problem = vns_construction_params.problem
                params.solution_template:Solution = vns_construction_params.solution_template
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

