""" 
..  _py_vns_optimizer:

The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search` contains class :class:`~.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer`, that represents implements algorithm :ref:`VNS<Algorithm_Variable_Neighborhood_Search>`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy
from random import choice
from random import random
from typing import TypeVar, Generic
from typing import Generic

from uo.utils.logger import logger
from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import ProblemSolutionVnsSupport

class VnsOptimizer(Metaheuristic):
    """
    Instance of the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer` encapsulate 
    :ref:`Algorithm_Variable_Neighborhood_Search` optimization algorithm.
    """
    
    def __init__(self, evaluations_max:int, 
            seconds_max:int, 
            random_seed:int, 
            keep_all_solution_codes:bool, 
            distance_calculation_cache_is_used:bool,
            output_control:OutputControl, 
            target_problem:TargetProblem, 
            initial_solution:TargetSolution, 
            problem_solution_vns_support:ProblemSolutionVnsSupport, 
            k_min:int, k_max:int, max_local_optima:int, local_search_type:str)->None:
        """
        Create new instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer`. 
        That instance implements :ref:`VNS<Algorithm_Variable_Neighborhood_Search>` algorithm. 

        :param int evaluations_max: maximum number of evaluations for algorithm execution
        :param int seconds_max: maximum number of seconds for algorithm execution
        :param int random_seed: random seed for metaheuristic execution
        :param bool keep_all_solution_codes: if all solution codes will be remembered
        :param bool distance_calculation_cache_is_used: if cache is used for distance calculation between solutions        
        :param `OutputControl` output_control: structure that controls output
        :param `TargetProblem` target_problem: problem to be solved
        :param `TargetSolution` initial_solution: initial solution of the problem that is optimized by VNS 
        :param `ProblemSolutionVnsSupport` problem_solution_vns_support: placeholder for additional methods for VNS 
        execution, which depend of precise solution type 
        :param int k_min: `k_min` parameter for VNS
        :param int k_max: `k_max` parameter for VNS
        :param int max_local_optima: max_local_optima parameter for VNS
        :param local_search_type: type of the local search
        :type local_search_type: str, possible values: 'local_search_best_improvement', 'local_search_first_improvement' 
        """
        super().__init__( name='vns', 
                evaluations_max=evaluations_max, 
                seconds_max=seconds_max, 
                random_seed=random_seed, 
                keep_all_solution_codes=keep_all_solution_codes,
                distance_calculation_cache_is_used=distance_calculation_cache_is_used, 
                output_control=output_control, 
                target_problem=target_problem)
        if initial_solution is not None:
            if isinstance(initial_solution, TargetSolution):
                self.__current_solution:TargetSolution = initial_solution.copy()
            else:
                self.__current_solution:TargetSolution = initial_solution
        else:
            self.__current_solution:TargetSolution = None
        self.__local_search_type:str = local_search_type
        if problem_solution_vns_support is not None:
            if isinstance(problem_solution_vns_support, ProblemSolutionVnsSupport):
                self.__problem_solution_vns_support:ProblemSolutionVnsSupport = problem_solution_vns_support.copy()
                self.__implemented_local_searches:Dict[str,function] = {
                    'local_search_best_improvement':  self.__problem_solution_vns_support.local_search_best_improvement,
                    'local_search_first_improvement':  self.__problem_solution_vns_support.local_search_first_improvement,
                }
                if( self.__local_search_type not in self.__implemented_local_searches):
                    raise ValueError( 'Value \'{} \' for VNS local_search_type is not supported'.format(
                            self.__local_search_type))
                self.__ls_method = self.__implemented_local_searches[self.__local_search_type]
                self.__shaking_method = self.__problem_solution_vns_support.shaking
            else:
                self.__problem_solution_vns_support:ProblemSolutionVnsSupport = problem_solution_vns_support
                self.__implemented_local_searches:Dict[str,function] = None
                self.__ls_method = None
                self.__shaking_method = None
        else:
            self.__problem_solution_vns_support:ProblemSolutionVnsSupport = None
            self.__implemented_local_searches:Dict[str,function] = None
            self.__ls_method = None
            self.__shaking_method = None
        self.__k_min:int = k_min
        self.__k_max:int = k_max
        self.__max_local_optima:int = max_local_optima
        # current value of the vns parameter k
        self.__k_current:int = None
        # values of the local optima foreach element calculated 
        self.__local_optima:Dict[int|BitArray, float] = {}

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
    def current_solution(self)->TargetSolution:
        """
        Property getter for the current solution used during VNS execution

        :return: instance of the :class:`uo.target_solution.TargetSolution` class subtype -- current solution of the problem 
        :rtype: :class:`TargetSolution`        
        """
        return self.__current_solution

    @current_solution.setter
    def current_solution(self, value:TargetSolution)->None:
        """
        Property setter for for the current solution used during VNS execution

        :param value: the current solution
        :type value: :class:`TargetSolution`
        """
        self.__current_solution = value

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
        self.current_solution.evaluate(self.target_problem);
        self.copy_to_best_solution(self.current_solution);

    def __add_local_optima__(self, current_solution:TargetSolution)->bool:
        """
        Add solution to the local optima structure 

        :param current_solution: solution to be added to local optima structure
        :type current_solution: :class:`optimization_algorithms.target_solution.TargetSolution`
        :return:  if adding is successful e.g. current_solution is new element in the structure
        :rtype: bool
        """       
        if current_solution.representation in self.__local_optima:
            return False
        if len(self.__local_optima) >= self.__max_local_optima:
            # removing random, just taking care not to remove the best ones
            while True:
                code = random.choice(self.__local_optima.keys())
                if code != self.best_solution.representation:
                    del self.__local_optima[code]
                    break
        self.__local_optima[current_solution.representation]=current_solution.fitness_value
        return True

    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the VNS algorithm
        """
        self.write_output_values_if_needed("before_step_in_iteration", "shaking")
        if not self.__shaking_method(self.__k_current, self.target_problem, self.current_solution, self):
            self.write_output_values_if_needed("after_step_in_iteration", "shaking")
            return False
        self.write_output_values_if_needed("after_step_in_iteration", "shaking")
        self.iteration += 1
        while self.__k_current <= self.__k_max:
            self.write_output_values_if_needed("before_step_in_iteration", "ls")
            self.current_solution = self.__ls_method(self.__k_current, self.target_problem, self.current_solution, self)
            self.write_output_values_if_needed("after_step_in_iteration", "ls")
            # update auxiliary structure that keeps all solution codes
            if self.keep_all_solution_codes:
                self.all_solution_codes.add(self.current_solution.string_representation())
            new_is_better = self.is_first_solution_better(self.current_solution, self.best_solution)
            make_move:bool = new_is_better
            if new_is_better is None:
                if  self.current_solution.string_representation() == self.best_solution.string_representation():
                    make_move = False
                else:
                    logger.debug("Same solution quality, generating random true with probability 0.5");
                    make_move = random() < 0.5
            if make_move:
                self.copy_to_best_solution(self.current_solution)
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
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s = super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += 'current_solution=' + self.current_solution.string_rep(delimiter, indentation + 1, 
                indentation_symbol, group_start, group_end) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'k_min=' + str(self.k_min) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'k_max=' + str(self.k_max) + delimiter
        s += delimiter
        s += '__problem_solution_vns_support=' + self.__problem_solution_vns_support.string_rep(delimiter, 
                indentation + 1, indentation_symbol, group_start, group_end) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__max_local_optima=' + str(self.__max_local_optima) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__local_search_type=' + str(self.__local_search_type) + delimiter
        for i in range(0, indentation):
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
