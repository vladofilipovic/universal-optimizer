""" 
..  _py_vns_optimizer:

The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.variable_neighborhood_search` contains class :class:`~.uo.metaheuristic.variable_neighborhood_search.variable_neighborhood_search.VnsOptimizer`, that represents implements algorithm :ref:`VNS<Algorithm_Variable_Neighborhood_Search>`.
"""

from pathlib import Path

from uo.solution.quality_of_solution import QualityOfSolution
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy

from random import choice
from random import random

from bitstring import Bits, BitArray, BitStream, pack

from typing import Optional, TypeVar, Generic
from typing import Generic
from typing import NamedTuple

from dataclasses import dataclass

from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.single_solution_metaheuristic import SingleSolutionMetaheuristic
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import \
        ProblemSolutionVnsSupport

@dataclass
class VnsOptimizerConstructionParameters:
        """
        Instance of the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search_constructor_parameters.
        VnsOptimizerConstructionParameters` represents constructor parameters for VNS algorithm.
        """
        finish_control: FinishControl = None
        output_control: OutputControl = None
        problem: Problem = None
        solution_template: Solution = None
        problem_solution_vns_support: ProblemSolutionVnsSupport = None
        random_seed: Optional[int] = None
        additional_statistics_control: AdditionalStatisticsControl = None
        k_min: Optional[int] = None
        k_max: Optional[int] = None
        local_search_type: Optional[str] = None

class VnsOptimizer(SingleSolutionMetaheuristic):
    """
    Instance of the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer` encapsulate 
    :ref:`Algorithm_Variable_Neighborhood_Search` optimization algorithm.
    """
    
    def __init__(self, 
            finish_control:FinishControl, 
            random_seed:Optional[int], 
            additional_statistics_control:AdditionalStatisticsControl,
            output_control:OutputControl, 
            problem:Problem, 
            solution_template:Solution,
            problem_solution_vns_support:ProblemSolutionVnsSupport, 
            k_min:int, 
            k_max:int, 
            local_search_type:str)->None:
        """
        Create new instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer`. 
        That instance implements :ref:`VNS<Algorithm_Variable_Neighborhood_Search>` algorithm. 

        :param `FinishControl` finish_control: structure that control finish criteria for metaheuristic execution
        :param int random_seed: random seed for metaheuristic execution
        :param `AdditionalStatisticsControl` additional_statistics_control: structure that controls additional 
        statistics obtained during population-based metaheuristic execution        
        :param `OutputControl` output_control: structure that controls output
        :param `Problem` problem: problem to be solved
        :param `Solution` solution_template: initial solution of the problem 
        :param `ProblemSolutionVnsSupport` problem_solution_vns_support: placeholder for additional methods, specific for VNS 
        execution, which depend of precise solution type 
        :param int k_min: `k_min` parameter for VNS
        :param int k_max: `k_max` parameter for VNS
        :param local_search_type: type of the local search
        :type local_search_type: str, possible values: 'localSearchBestImprovement', 'localSearchFirstImprovement' 
        """
        if not isinstance(finish_control, FinishControl):
                raise TypeError('Parameter \'finish_control\' must be \'FinishControl\'.')
        if not isinstance(random_seed, Optional[int]):
                raise TypeError('Parameter \'random_seed\' must be \'int\' or \'None\'.')
        if not isinstance(additional_statistics_control, AdditionalStatisticsControl):
                raise TypeError('Parameter \'additional_statistics_control\' must be \'AdditionalStatisticsControl\'.')
        if not isinstance(output_control, OutputControl):
                raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
        if not isinstance(problem, Problem):
                raise TypeError('Parameter \'problem\' must be \'Problem\'.')
        if not isinstance(solution_template, Solution) and solution_template is not None:
                raise TypeError('Parameter \'solution_template\' must be \'Solution\' or \'None\'.')        
        if not isinstance(problem_solution_vns_support, ProblemSolutionVnsSupport):
                raise TypeError('Parameter \'problem_solution_vns_support\' must be \'ProblemSolutionVnsSupport\'.')        
        if not isinstance(k_min, int):
                raise TypeError('Parameter \'k_min\' must be \'int\'.')        
        if not isinstance(k_max, int):
                raise TypeError('Parameter \'k_max\' must be \'int\'.')        
        if not isinstance(local_search_type, str):
                raise TypeError('Parameter \'local_search_type\' must be \'str\'.')        
        super().__init__( name='vns', 
                finish_control=finish_control, 
                random_seed=random_seed, 
                additional_statistics_control=additional_statistics_control, 
                output_control=output_control, 
                problem=problem,
                solution_template=solution_template)
        self.__local_search_type:str = local_search_type
        self.__problem_solution_vns_support:ProblemSolutionVnsSupport = problem_solution_vns_support
        self.__implemented_local_searches:dict[str,function] = {
            'localSearchBestImprovement':  self.__problem_solution_vns_support.local_search_best_improvement,
            'localSearchFirstImprovement':  self.__problem_solution_vns_support.local_search_first_improvement,
        }
        if( self.__local_search_type not in self.__implemented_local_searches.keys()):
            raise ValueError( 'Value \'{}\' for VNS local_search_type is not supported'.format(
                    self.__local_search_type))
        self.__ls_method = self.__implemented_local_searches[self.__local_search_type]
        self.__shaking_method = self.__problem_solution_vns_support.shaking
        self.__k_min:int = k_min
        self.__k_max:int = k_max
        # current value of the vns parameter k
        self.__k_current:Optional[int] = None

    @classmethod
    def from_construction_tuple(cls, construction_tuple:VnsOptimizerConstructionParameters):
        """
        Additional constructor, that creates new instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer`. 

        :param `VnsOptimizerConstructionParameters` construction_tuple: tuple with all constructor parameters
        """
        return cls( 
            construction_tuple.finish_control,
            construction_tuple.random_seed, 
            construction_tuple.additional_statistics_control,
            construction_tuple.output_control, 
            construction_tuple.problem, 
            construction_tuple.solution_template,
            construction_tuple.problem_solution_vns_support, 
            construction_tuple.k_min, 
            construction_tuple.k_max, 
            construction_tuple.local_search_type)

    def __copy__(self):
        """
        Internal copy of the current instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer`        
        """
        vns_opt = deepcopy(self)
        return vns_opt

    def copy(self):
        """
        Copy the current instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer`        
        """
        return self.__copy__()

    @property
    def k_min(self)->int:
        """
        Property getter for the `k_min` parameter for VNS

        :return: `k_min` parameter for VNS 
        :rtype: int
        """
        return self.__k_min

    @property
    def k_max(self)->int:
        """
        Property getter for the `k_max` parameter for VNS

        :return: k_max parameter for VNS 
        :rtype: int
        """
        return self.__k_max

    def init(self)->None:
        """
        Initialization of the VNS algorithm
        """
        self.__k_current = self.k_min
        self.current_solution = self.solution_template.copy()
        self.current_solution.init_random(self.problem)
        self.evaluation = 1
        self.current_solution.evaluate(self.problem)
        self.best_solution = self.current_solution
    
    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the VNS algorithm
        """
        self.write_output_values_if_needed("before_step_in_iteration", "shaking")
        if not self.__shaking_method(self.__k_current, self.problem, self.current_solution, self):
            self.write_output_values_if_needed("after_step_in_iteration", "shaking")
            return
        self.write_output_values_if_needed("after_step_in_iteration", "shaking")
        self.iteration += 1
        while self.__k_current <= self.__k_max:
            self.write_output_values_if_needed("before_step_in_iteration", "ls")
            improvement:bool = self.__ls_method(self.__k_current, self.problem, self.current_solution, self)
            self.write_output_values_if_needed("after_step_in_iteration", "ls")
            if improvement:
                # update auxiliary structure that keeps all solution codes
                self.update_additional_statistics_if_required(self.current_solution)
                self.best_solution = self.current_solution
                self.__k_current = self.k_min
            else:
                self.__k_current += 1

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='',group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the `VnsOptimizer` instance

        :param delimiter: delimiter between fields
        :type delimiter: str
        :param indentation: level of indentation
        :type indentation: int, optional, default value 0
        :param indentation_symbol: indentation symbol
        :type indentation_symbol: str, optional, default value ''
        :param group_start: group start string 
        :type group_start: str, optional, default value '{'
        :param group_end: group end string 
        :type group_end: str, optional, default value '}'
        :return: string representation of instance that controls output
        :rtype: str
        """             
        s = delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s = super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        if self.current_solution is not None:
            s += 'current_solution=' + self.current_solution.string_rep(delimiter, indentation + 1, 
                    indentation_symbol, group_start, group_end) + delimiter
        else:
            s += 'current_solution=None' + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'k_min=' + str(self.k_min) + delimiter 
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'k_max=' + str(self.k_max) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += '__problem_solution_vns_support=' + self.__problem_solution_vns_support.string_rep(delimiter, 
                indentation + 1, indentation_symbol, group_start, group_end) + delimiter 
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += '__local_search_type=' + str(self.__local_search_type) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the `VnsOptimizer` instance

        :return: string representation of the `VnsOptimizer` instance
        :rtype: str
        """
        s = self.string_rep('|')
        return s;

    def __repr__(self)->str:
        """
        String representation of the `VnsOptimizer` instance

        :return: string representation of the `VnsOptimizer` instance
        :rtype: str
        """
        s = self.string_rep('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the VnsOptimizer instance

        :param spec: str -- format specification 
        :return: formatted `VnsOptimizer` instance
        :rtype: str
        """
        return self.string_rep('\n',0,'   ','{', '}')
