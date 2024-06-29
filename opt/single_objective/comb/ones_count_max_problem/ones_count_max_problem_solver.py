""" 
The :mod:`opt.single_objective.comb.ones_count_max_problem.solver` contains programming code that optimize :ref:`Problem_Ones_Count_Max` with various optimization techniques.
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

from uo.algorithm.exact.total_enumeration.te_operations_support_rep_bit_array import\
        TeOperationsSupportRepresentationBitArray
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer
from uo.algorithm.exact.total_enumeration.te_operations_support import TeOperationsSupport


from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support import VnsShakingSupport
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_rep_bit_array import \
        VnsShakingSupportRepresentationBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_rep_int import \
        VnsShakingSupportRepresentationInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support import VnsLocalSearchSupport
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_rep_bit_array import \
        VnsLocalSearchSupportRepresentationBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_rep_int import \
        VnsLocalSearchSupportRepresentationInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support import GaCrossoverSupport
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support_rep_bit_array import \
        GaCrossoverSupportRepresentationBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support import GaMutationSupport
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support_rep_bit_array import \
        GaMutationSupportRepresentationBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizerConstructionParameters
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizer


from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_ilp_linopy import \
        OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_ilp_linopy import \
        OnesCountMaxProblemIntegerLinearProgrammingSolver

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_int_solution import \
        OnesCountMaxProblemIntSolution
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_bit_array_solution import \
        OnesCountMaxProblemBitArraySolution

@dataclass
class MaxOneProblemSolverConstructionParameters:
        """
        Instance of the class :class:`MaxOneProblemSolverConstructionParameters` represents constructor parameters for max ones problem solver.
        """
        method: str = None
        finish_control: FinishControl = None
        output_control: OutputControl = None
        problem: Problem = None
        solution_template: Solution = None
        vns_shaking_support: VnsShakingSupport = None
        vns_ls_support: VnsLocalSearchSupport = None
        vns_random_seed: int = None
        vns_additional_statistics_control: AdditionalStatisticsControl = None
        vns_k_min: int = None
        vns_k_max: int = None
        vns_local_search_type: str = None
        te_problem_solution_support:TeOperationsSupport = None

class OnesCountMaxProblemSolver:
    """
    Instance of the class :class:`OnesCountMaxProblemSolver` any of the developed solvers Ones Count Problem.
    """
    def __init__(self, method:str=None,
            finish_control:FinishControl = None,
            output_control:OutputControl = None,
            problem:Problem = None,
            solution_template:Solution = None,
            vns_shaking_support:VnsShakingSupport = None,
            vns_ls_support:VnsLocalSearchSupport = None,
            vns_random_seed:int = None,
            vns_additional_statistics_control:AdditionalStatisticsControl = None,
            vns_k_min:int = None,
            vns_k_max:int = None,
            vns_local_search_type:str = None,
            te_operations_support:TeOperationsSupport = None
    )->None:
        """
        Create new `OnesCountMaxProblemSolver` instance

        :param str method: method used for solving the Max Ones Problem 
        :param FinishControl finish_control: controls finish criteria
        :param output_control:OutputControl = controls output
        :param Problem problem: problem that is solved
        :param Solution solution_template: initial solution
        :param VnsShakingSupport vns_shaking_support: Specific VNS support for shaking
        :param VnsLocalSearchSupport vns_ls_support: Specific VNS support for local_search
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
            if not isinstance(vns_shaking_support, VnsShakingSupport):
                    raise TypeError('Parameter \'vns_shaking_support\' must be \'VnsShakingSupport\'.')
            if not isinstance(vns_ls_support, VnsLocalSearchSupport):
                    raise TypeError('Parameter \'vns_ls_support\' must be \'VnsLocalSearchSupport\'.')
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
                    vns_shaking_support= vns_shaking_support,
                    vns_ls_support= vns_ls_support,
                    random_seed= vns_random_seed, 
                    additional_statistics_control= vns_additional_statistics_control,
                    k_min= vns_k_min,
                    k_max= vns_k_max,
                    local_search_type= vns_local_search_type)
        elif method == 'genetic_algorithm':
            if not isinstance(finish_control, FinishControl):
                    raise TypeError('Parameter \'finish_control\' must be \'FinishControl\'.')
            if not isinstance(output_control, OutputControl):
                    raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
            if not isinstance(problem, Problem):
                    raise TypeError('Parameter \'problem\' must be \'Problem\'.')
            if not isinstance(solution_template, Solution):
                    raise TypeError('Parameter \'solution_template\' must be \'Solution\'.')
        elif method == 'total_enumeration':
            if not isinstance(output_control, OutputControl):
                    raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
            if not isinstance(problem, Problem):
                    raise TypeError('Parameter \'problem\' must be \'Problem\'.')
            if not isinstance(solution_template, Solution):
                    raise TypeError('Parameter \'solution_template\' must be \'Solution\'.')
            if not isinstance(te_operations_support, TeOperationsSupport):
                    raise TypeError('Parameter \'te_problem_solution_support\' must be \'TeOperationsSupport\'.')
            self.__optimizer = TeOptimizer(
                    output_control = output_control,
                    problem= problem,
                    solution_template= solution_template,
                    te_operations_support=te_operations_support
            )
        elif method == 'integer_linear_programming':
            if not isinstance(output_control, OutputControl):
                    raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
            if not isinstance(problem, Problem):
                    raise TypeError('Parameter \'problem\' must be \'Problem\'.')
            self.__optimizer:Optimizer = OnesCountMaxProblemIntegerLinearProgrammingSolver(
                output_control = output_control,
                problem = problem
            )
        else:
            raise ValueError("Invalid optimization method {} - should be one of: '{}', '{}', '{}'.".format(method,
                    'variable_neighborhood_search', 'total_enumeration', 'integer_linear_programming'))


    @classmethod
    def from_construction_tuple(cls, construction_params:MaxOneProblemSolverConstructionParameters=None):
        """
        Additional constructor. Create new `OnesCountMaxProblemSolver` instance from construction parameters

        :param `MaxOneProblemSolverConstructionParameters` construction_params: parameters for construction 
        """
        return cls(
            method = construction_params.method,
            finish_control = construction_params.finish_control,
            output_control = construction_params.output_control,
            problem = construction_params.problem,
            solution_template = construction_params.solution_template,
            vns_shaking_support = construction_params.vns_shaking_support,
            vns_ls_support = construction_params.vns_ls_support,
            vns_random_seed = construction_params.vns_random_seed, 
            vns_additional_statistics_control = construction_params.vns_additional_statistics_control,
            vns_k_min = construction_params.vns_k_min,
            vns_k_max = construction_params.vns_k_max,
            vns_local_search_type = construction_params.vns_local_search_type,
            te_problem_solution_support= construction_params.te_problem_solution_support
        )

    @classmethod
    def from_variable_neighborhood_search(cls, vns_construction_params:VnsOptimizerConstructionParameters=None):
        """
        Additional constructor. Create new `OnesCountMaxProblemSolver` instance when solving method is `Variable Neighborhood Search`

        :param VnsOptimizerConstructionParameters vns_construction_params: construction parameters 
        """
        params:MaxOneProblemSolverConstructionParameters = MaxOneProblemSolverConstructionParameters()
        params.method = 'variable_neighborhood_search'
        params.finish_control = vns_construction_params.finish_control
        params.output_control = vns_construction_params.output_control
        params.problem= vns_construction_params.problem
        params.solution_template = vns_construction_params.solution_template
        params.vns_shaking_support = vns_construction_params.vns_shaking_support
        params.vns_ls_support = vns_construction_params.vns_ls_support
        params.vns_random_seed = vns_construction_params.random_seed
        params.vns_additional_statistics_control = vns_construction_params.additional_statistics_control
        params.vns_k_min = vns_construction_params.k_min
        params.vns_k_max = vns_construction_params.k_max
        params.vns_local_search_type = vns_construction_params.local_search_type        
        return cls.from_construction_tuple(params)

    @classmethod
    def from_genetic_algorithm(cls, ga_construction_params:VnsOptimizerConstructionParameters=None):
        """
        Additional constructor. Create new `OnesCountMaxProblemSolver` instance when solving method is `Variable Neighborhood Search`

        :param VnsOptimizerConstructionParameters vns_construction_params: construction parameters 
        """
        params:MaxOneProblemSolverConstructionParameters = MaxOneProblemSolverConstructionParameters()
        params.method = 'variable_neighborhood_search'
        params.finish_control = vns_construction_params.finish_control
        params.output_control = vns_construction_params.output_control
        params.problem= vns_construction_params.problem
        params.solution_template = vns_construction_params.solution_template
        params.vns_shaking_support = vns_construction_params.vns_shaking_support
        params.vns_ls_support = vns_construction_params.vns_ls_support
        params.vns_random_seed = vns_construction_params.random_seed
        params.vns_additional_statistics_control = vns_construction_params.additional_statistics_control
        params.vns_k_min = vns_construction_params.k_min
        params.vns_k_max = vns_construction_params.k_max
        params.vns_local_search_type = vns_construction_params.local_search_type        
        return cls.from_construction_tuple(params)


    @classmethod
    def from_total_enumeration(cls, te_construction_params:TeOptimizerConstructionParameters=None):
        """
        Additional constructor. Create new `OnesCountMaxProblemSolver` instance when solving method is `Total Enumeration`

        :param TeOptimizerConstructionParameters te_construction_params: construction parameters 
        """
        params:MaxOneProblemSolverConstructionParameters = MaxOneProblemSolverConstructionParameters()
        params.method = 'total_enumeration'
        params.output_control = te_construction_params.output_control
        params.problem = te_construction_params.problem
        params.solution_template= te_construction_params.solution_template
        params.te_problem_solution_support= te_construction_params.te_operations_support
        return cls.from_construction_tuple(params)

    @classmethod
    def from_integer_linear_programming(cls, ilp_construction_params:\
            OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters=None):
        """
        Additional constructor. Create new `OnesCountMaxProblemSolver` instance when solving method is `Integer Linear Programming`

        :param `OnesCountMaxProblemIntegerLinearProgrammingSolverConstructionParameters` ilp_construction_params: construction parameters 
        """
        params:MaxOneProblemSolverConstructionParameters = MaxOneProblemSolverConstructionParameters()
        params.method = 'integer_linear_programming'
        params.output_control = ilp_construction_params.output_control
        params.problem = ilp_construction_params.problem
        return cls.from_construction_tuple(params)

    @property
    def opt(self)->Optimizer:
        """
        Property getter for the optimizer used for solving

        :return: optimizer
        :rtype: `Optimizer`
        """
        return self.__optimizer

