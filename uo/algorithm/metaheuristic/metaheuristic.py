""" 
The :mod:`~uo.algorithm.metaheuristic.metaheuristic` module describes the class :class:`~uo.algorithm.metaheuristic.metaheuristic.Metaheuristic`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

from random import random
from random import randrange
from copy import deepcopy
from datetime import datetime
from io import TextIOWrapper 

from bitstring import BitArray

from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic
from typing import Generic


from uo.utils.logger import logger

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.output_control import OutputControl
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.metaheuristic.solution_code_distance_cache_control_statistics import DistanceCalculationCacheControlStatistics

class Metaheuristic(Algorithm, metaclass=ABCMeta):
    """
    This class represent metaheuristic
    """

    @abstractmethod
    def __init__(self, name:str, evaluations_max:int, seconds_max:int, random_seed:int, 
            keep_all_solution_codes:bool,
            distance_calculation_cache_is_used:bool,
            output_control:OutputControl, 
            target_problem:TargetProblem)->None:
        """
        Create new Metaheuristic instance

        :param str name: name of the metaheuristic
        :param int evaluations_max: maximum number of evaluations for algorithm execution
        :param int seconds_max: maximum number of seconds for algorithm execution
        :param int random_seed: random seed for metaheuristic execution
        :param bool keep_all_solution_codes: if all solution codes will be remembered        
        :param bool distance_calculation_cache_is_used: if cache is used for distance calculation between solutions        
        :param `OutputControl` output_control: structure that controls output
        :param `TargetProblem` target_problem: problem to be solved
        """
        super().__init__(name=name, 
                evaluations_max=evaluations_max, 
                seconds_max=seconds_max, 
                output_control=output_control, 
                target_problem=target_problem)
        if random_seed is not None and isinstance(random_seed, int) and random_seed != 0:
            self.__random_seed:int = random_seed
        else:
            self.__random_seed:int = randrange(sys.maxsize)
        self.__iteration:int = 0
        self.__iteration_best_found:int = 0
        self.__second_when_best_obtained:float = 0.0
        self.__best_solution:TargetSolution = None
        self.__keep_all_solution_codes:bool = keep_all_solution_codes
        #class/static variable all_solution_codes
        if not hasattr(Metaheuristic, 'all_solution_codes'):
            Metaheuristic.all_solution_codes:set[str] = set()
        #class/static variable representation_distance_cache_cs
        if not hasattr(Metaheuristic, 'representation_distance_cache_cs'):
            Metaheuristic.representation_distance_cache_cs:DistanceCalculationCacheControlStatistics = DistanceCalculationCacheControlStatistics(distance_calculation_cache_is_used)

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current metaheuristic

        :return: new `Metaheuristic` instance with the same properties
        :rtype: `Metaheuristic`
        """
        met = deepcopy(self)
        return met

    @abstractmethod
    def copy(self):
        """
        Copy the current metaheuristic
        
        :return: new `Metaheuristic` instance with the same properties
        :rtype: `Metaheuristic`
        """
        return self.__copy__()

    @property
    def random_seed(self)->int:
        """
        Property getter for the random seed used during metaheuristic execution
        
        :return: random seed 
        :rtype: int
        """
        return self.__random_seed

    @property
    def iteration(self)->int:
        """
        Property getter for the iteration of metaheuristic execution
        
        :return: iteration
        :rtype: int
        """
        return self.__iteration

    @iteration.setter
    def iteration(self, value:int)->None:
        """
        Property setter the iteration of metaheuristic execution
        
        :param int value: iteration
        """
        self.__iteration = value

    @property
    def best_solution(self)->TargetSolution:
        """
        Property getter for the best solution obtained during metaheuristic execution
        
        :return: best solution so far 
        :rtype: TargetSolution
        """
        return self.__best_solution

    @property
    def keep_all_solution_codes(self)->bool:
        """
        Property getter for decision should be kept all solution codes
        
        :return: decision should be kept all solution codes
        :rtype: bool
        """
        return self.__keep_all_solution_codes

    @abstractmethod
    def init(self)->None:
        """
        Initialization of the metaheuristic algorithm
        """
        raise NotImplementedError

    @abstractmethod
    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the metaheuristic algorithm
        """
        raise NotImplementedError

    def elapsed_seconds(self)->float:
        """
        Calculate time elapsed during execution of the metaheuristic algorithm 
        
        :return: elapsed time (in seconds)
        :rtype: float
        """
        delta = datetime.now() - self.execution_started
        return delta.total_seconds()

    def main_loop(self)->None:
        """
        Main loop of the metaheuristic algorithm
        """
        while (self.evaluations_max == 0 or self.evaluation < self.evaluations_max) and (self.seconds_max == 
                0 or self.elapsed_seconds() < self.seconds_max):
            self.write_output_values_if_needed("before_iteration", "b_i")
            self.main_loop_iteration()
            self.write_output_values_if_needed("after_iteration", "a_i")
            logger.debug('Iteration:{}, Evaluations:{}, Solution:{}'.format(self.iteration, self.evaluation,
                self.best_solution.string_representation()))

    def optimize(self)->None:
        """
        Executing optimization by the metaheuristic algorithm
        """
        self.execution_started = datetime.now()
        self.init()
        self.write_output_headers_if_needed()
        self.write_output_values_if_needed("before_algorithm", "b_a")
        self.main_loop()
        self.execution_ended = datetime.now()
        self.write_output_values_if_needed("after_algorithm", "a_a")

    def is_first_solution_better(self, sol1:TargetSolution, sol2:TargetSolution)->bool:
        """
        Checks if first solution is better than the second one

        :param TargetSolution sol1: first solution
        :param TargetSolution sol2: second solution
        :return: `True` if first solution is better, `False` if first solution is worse, `None` if fitnesses of both 
                solutions are equal
        :rtype: bool
        """
        if self.target_problem is None:
            raise ValueError('Target problem have to be defined within metaheuristic.')
        if self.target_problem.is_minimization is None:
            raise ValueError('Information if minimization or maximization is set within metaheuristic target problem'
                    'have to be defined.')
        is_minimization:bool = self.target_problem.is_minimization
        if sol1 is None:
            fit1:float = None
        else:
            fit1:float = sol1.calculate_objective_fitness_feasibility(self.target_problem).fitness_value;
        if sol2 is None:
            fit2:float = None
        else:
            fit2:float = sol2.calculate_objective_fitness_feasibility(self.target_problem).fitness_value;
        # with fitness is better than without fitness
        if fit1 is None:
            if fit2 is not None:
                return False
            else:
                return None
        elif fit2 is None:
            return True
        # if better, return true
        if (is_minimization and fit1 < fit2) or (not is_minimization and fit1 > fit2):
            return True
        # if same fitness, return None
        if fit1 == fit2:
            return None
        # otherwise, return false
        return False

    def copy_to_best_solution(self, solution:TargetSolution)->None:
        """
        Copies function argument to become the best solution within metaheuristic instance and update info about time 
        and iteration when the best solution is updated 

        :param TargetSolution solution: solution that is source for coping operation
        """
        self.__best_solution = solution.copy()
        self.__second_when_best_obtained = (datetime.now() - self.execution_started).total_seconds()
        self.__iteration_best_found = self.iteration

    def calculate_representation_distance(self, code_x:str, code_y:str)->float:
        """
        Calculate distance between two solution codes with optional cache consultation
        
        :param str code_x: first solution code 
        :param str code_y: second solution code 
        :return: distance between solution codes 
        :rtype: float
        """
        if code_x == code_y:
            return 0;
        scdc = self.__representation_distance_cache_cs 
        scdc.requests_count += 1
        if scdc.is_caching: 
            if code_x in scdc.cache and code_y in scdc.cache[code_x]:
                scdc.hit_count += 1
                return scdc.cache[code_x][code_y]
            dist = TargetSolution.representation_distance(code_x, code_y)
            if code_x not in scdc.cache:
                scdc.cache[code_x] = {};
            scdc.cache[code_x][code_y] = dist;
            return dist;
        else:
            dist = TargetSolution.representation_distance(code_x, code_y)
            return dist

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
            group_end:str ='}')->str:
        """
        String representation of the Metaheuristic instance
        
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
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'random_seed=' + str(self.random_seed) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__iteration=' + str(self.__iteration) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__iteration_best_found=' + str(self.__iteration_best_found) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__second_when_best_obtained=' + str(self.__second_when_best_obtained) + delimiter
        if self.__best_solution is not None:
            s += '__best_solution=' + self.__best_solution.string_rep(delimiter, indentation + 1,
                    indentation_symbol, group_start, group_end) + delimiter
        else:
            for i in range(0, indentation):
                s += indentation_symbol  
            s += '__best_solution=None' + delimiter
        s += '__representation_distance_cache_cs(static)=' + Metaheuristic.representation_distance_cache_cs.string_rep(
                delimiter, indentation + 1, indentation_symbol, '{', '}') + delimiter
        if self.execution_ended is not None and self.execution_started is not None:
            for i in range(0, indentation):
                s += indentation_symbol  
            s += 'execution time=' + str( (self.execution_ended - self.execution_started).total_seconds() ) + delimiter
        if self.keep_all_solution_codes:
            for i in range(0, indentation):
                s += indentation_symbol  
            s += 'all solution codes=' + str(len(Metaheuristic.all_solution_codes)) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the `Metaheuristic` instance
        
        :return: string representation of the `Metaheuristic` instance
        :rtype: str
        """
        s = self.string_rep('|')
        return s

    @abstractmethod
    def __repr__(self)->str:
        """
        String representation of the `Metaheuristic` instance
        
        :return: string representation of the `Metaheuristic` instance
        :rtype: str
        """
        s = self.string_rep('\n')
        if self.keep_all_solution_codes:
            s += 'all_solution_codes=' + str(self.all_solution_codes) 
        return s

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the `Metaheuristic` instance
        
        :param str spec: format specification
        :return: formatted `Metaheuristic` instance
        :rtype: str
        """
        return self.string_rep('|')
