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
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_support_for_target_solution import VnsSupportForTargetSolution

S_co = TypeVar("S_co", covariant=True, bound=TargetSolution) # and bound by VnsSupportForTargetSolution 

class VnsOptimizer(Metaheuristic, Generic[S_co]):
    """
    Instance of the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer` encapsulate :ref:`Algorithm_Variable_Neighborhood_Search` optimization algorithm.
    """
    
    def __init__(self, evaluations_max:int, seconds_max:int, random_seed:int, keep_all_solution_codes:bool, 
            target_problem:TargetProblem, initial_solution:S_co, k_min:int, k_max:int, max_local_optima:int, 
            local_search_type:str)->None:
        """
        Create new instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsOptimizer`. 
        That instance implements :ref:`VNS<Algorithm_Variable_Neighborhood_Search>` algorithm. 

        :param int evaluations_max: maximum number of evaluations for algorithm execution
        :param int seconds_max: maximum number of seconds for algorithm execution
        :param int random_seed: random seed for metaheuristic execution
        :param bool keep_all_solution_codes: if all solution codes will be remembered
        :param TargetProblem target_problem: problem to be solved
        :param S_co initial_solution: initial solution of the problem that is optimized by VNS 
        :param int k_min: `k_min` parameter for VNS
        :param int k_max: `k_max` parameter for VNS
        :param int max_local_optima: max_local_optima parameter for VNS
        """
        super().__init__('vns', evaluations_max, seconds_max, random_seed, keep_all_solution_codes, target_problem)
        self.__current_solution:S_co = initial_solution
        self.__k_min:int = k_min
        self.__k_max:int = k_max
        self.__max_local_optima:int = max_local_optima
        self.__local_search_type:str = local_search_type        
        self.__k_current:int = None
        self.__local_optima:Dict[str, float] = {}
        self.__shaking_counts:Dict[int,int] = {}

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
    def current_solution(self)->S_co:
        """
        Property getter for the current solution used during VNS execution

        :return: instance of the :class:`uo.target_solution.TargetSolution` class subtype -- current solution of the problem 
        :rtype: :class:`S_co`        
        """
        return self.__current_solution

    @current_solution.setter
    def current_solution(self, value:S_co)->None:
        """
        Property setter for for the current solution used during VNS execution

        :param value: the current solution
        :type value: :class:`S_co`
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

    def __select_shaking_points__(self)->list[str]:
        """
        Selecting shaking point for the VNS algorithm
        
        :return:  list with solution codes that represents start of the shaking 
        :rtype: list[str]
        """
        return [self.current_solution.solution_code()]

    def __add_local_optima__(self, current_solution:TargetSolution)->bool:
        """
        Add solution to the local optima structure 

        :param current_solution: solution to be added to local optima structure
        :type current_solution: :class:`optimization_algorithms.target_solution.TargetSolution`
        :return:  if adding is successful e.g. current_solution is new element in the structure
        :rtype: bool
        """       
        if current_solution.solution_code() in self.__local_optima:
            return False
        if len(self.__local_optima) >= self.__max_local_optima:
            # removing random, just taking care not to remove the best ones
            while True:
                code = random.choice(self.__local_optima.keys())
                if code != self.best_solution.solution_code():
                    del self.__local_optima[code]
                    break
        self.__local_optima[current_solution.solution_code()]=current_solution.fitness_value
        return True

    def __shaking_ls__(self)->bool:
        """
        Shaking phase of the VNS algorithm

        :return: if result obtain by shaking is better than initial
        :rtype: bool
        """
        #logger.debug('__shaking_ls__ - start')
        #logger.debug('Current: {}'.format(self.current_solution))
        #logger.debug('Best: {}'.format(self.current_solution))
        shaking_points:list[str] = self.__select_shaking_points__()
        if not self.current_solution.vns_randomize(self.target_problem, self.__k_current, shaking_points):
            return False
        if self.__k_current in self.__shaking_counts:
            self.__shaking_counts[self.__k_current] += 1
        else:
            self.__shaking_counts[self.__k_current] = 1
        self.iteration += 1
        self.evaluation += 1
        self.current_solution.evaluate(self.target_problem)
        if self.__local_search_type == 'local_search_best_improvement':
            self.current_solution = self.local_search_best_improvement(self.current_solution)
        else:
            raise ValueError( 'Value \'{} \' for VNS local_search_type is not supported'.format(
                    self.__local_search_type))
        if self.keep_all_solution_codes:
            self.all_solution_codes.add(self.current_solution)
        new_is_better = self.is_first_solution_better(self.current_solution, self.best_solution)
        if new_is_better is None:
            if self.current_solution.solution_code() == self.best_solution.solution_code():
                return False
            else:
                logger.debug("Same solution quality, generating random true with probability 0.5");
                return random() < 0.5
        #logger.debug('__shaking_ls__ - end')
        #logger.debug('Current: {}'.format(self.current_solution))
        #logger.debug('Best: {}'.format(self.current_solution))
        return new_is_better

    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the VNS algorithm
        """
        while self.__shaking_ls__():
            self.copy_to_best_solution(self.current_solution)
            self.__k_current = self.k_min
        if self.__k_current < self.k_max:
            self.__k_current += 1
        else:
            self.__k_current = self.k_min

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='',group_start:str ='{', 
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
        s = super().string_representation(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += 'current_solution=' + self.current_solution.string_representation(delimiter, indentation + 1, 
                indentation_symbol, group_start, group_end) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'k_min=' + str(self.k_min) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'k_max=' + str(self.k_max) + delimiter
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
        s = self.string_representation('|')
        return s;

    def __repr__(self)->str:
        """
        String representation of the `VnsOptimizer` instance

        :return: string representation of the `VnsOptimizer` instance
        :rtype: str
        """
        s = self.string_representation('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the VnsOptimizer instance

        :param spec: str -- format specification 
        :return: formatted `VnsOptimizer` instance
        :rtype: str
        """
        return self.string_representation('\n',0,'   ','{', '}')
