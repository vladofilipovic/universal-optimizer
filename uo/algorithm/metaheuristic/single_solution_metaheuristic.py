""" 
The :mod:`~uo.algorithm.metaheuristic.single_solution_metaheuristic` module describes the class :class:`~uo.algorithm.metaheuristic.single_solution_metaheuristic.SingleSolutionMetaheuristic`.
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
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic
from uo.algorithm.metaheuristic.solution_code_distance_cache_control_statistics import DistanceCalculationCacheControlStatistics

class SingleSolutionMetaheuristic(Metaheuristic, metaclass=ABCMeta):
    """
    This class represent single solution metaheuristic
    """

    @abstractmethod
    def __init__(self, 
            name:str, 
            evaluations_max:int, 
            iterations_max:int,
            seconds_max:int, 
            random_seed:int, 
            keep_all_solution_codes:bool,
            distance_calculation_cache_is_used:bool,
            output_control:OutputControl, 
            target_problem:TargetProblem,
            initial_solution:TargetSolution
    )->None:
        """
        Create new SingleSolutionMetaheuristic instance

        :param str name: name of the metaheuristic
        :param int evaluations_max: maximum number of evaluations for algorithm execution
        :param int iterations_max: maximum number of iterations for algorithm execution
        :param int seconds_max: maximum number of seconds for algorithm execution
        :param int random_seed: random seed for metaheuristic execution
        :param bool keep_all_solution_codes: if all solution codes will be remembered        
        :param bool distance_calculation_cache_is_used: if cache is used for distance calculation between solutions        
        :param `OutputControl` output_control: structure that controls output
        :param `TargetProblem` target_problem: problem to be solved
        :param `TargetSolution` initial_solution: initial solution of the problem
        """
        super().__init__(name=name, 
                evaluations_max=evaluations_max,
                iterations_max=iterations_max,
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
            self.__current_solution:TargetSolution =  None

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current single solution metaheuristic

        :return: new `SingleSolutionMetaheuristic` instance with the same properties
        :rtype: `SingleSolutionMetaheuristic`
        """
        met = deepcopy(self)
        return met

    @abstractmethod
    def copy(self):
        """
        Copy the current single solution metaheuristic
        
        :return: new `SingleSolutionMetaheuristic` instance with the same properties
        :rtype: `SingleSolutionMetaheuristic`
        """
        return self.__copy__()

    @property
    def current_solution(self)->TargetSolution:
        """
        Property getter for the current solution used during single solution metaheuristic execution

        :return: instance of the :class:`uo.target_solution.TargetSolution` class subtype -- current solution of the problem 
        :rtype: :class:`TargetSolution`        
        """
        return self.__current_solution

    @current_solution.setter
    def current_solution(self, value:TargetSolution)->None:
        """
        Property setter for the current solution used during single solution metaheuristic execution

        :param value: the current solution
        :type value: :class:`TargetSolution`
        """
        self.__current_solution = value

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
            group_end:str ='}')->str:
        """
        String representation of the SingleSolutionMetaheuristic instance
        
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
        s += 'current_solution=' + str(self.current_solution) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the `SingleSolutionMetaheuristic` instance
        
        :return: string representation of the `SingleSolutionMetaheuristic` instance
        :rtype: str
        """
        s = self.string_rep('|')
        return s

    @abstractmethod
    def __repr__(self)->str:
        """
        String representation of the `SingleSolutionMetaheuristic` instance
        
        :return: string representation of the `SingleSolutionMetaheuristic` instance
        :rtype: str
        """
        s = self.string_rep('\n')
        if self.keep_all_solution_codes:
            s += 'all_solution_codes=' + str(self.all_solution_codes) 
        return s

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the `SingleSolutionMetaheuristic` instance
        
        :param str spec: format specification
        :return: formatted `Metaheuristic` instance
        :rtype: str
        """
        return self.string_rep('|')