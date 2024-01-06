""" 
The :mod:`~uo.algorithm.metaheuristic.population_based_metaheuristic` module describes the class :class:`~uo.algorithm.metaheuristic.population_based_metaheuristic.PopulationBasedMetaheuristic`.
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
from typing import Optional, TypeVar, Generic
from typing import Generic


from uo.utils.logger import logger

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic

class PopulationBasedMetaheuristic(Metaheuristic, metaclass=ABCMeta):
    """
    This class represent population metaheuristic
    """

    @abstractmethod
    def __init__(self, 
            name:str, 
            finish_control:FinishControl,
            random_seed:Optional[int], 
            additional_statistics_control:AdditionalStatisticsControl,
            output_control:OutputControl, 
            target_problem:TargetProblem,
            initial_solutions:list[TargetSolution]
    )->None:
        """
        Create new PopulationBasedMetaheuristic instance

        :param str name: name of the metaheuristic
        :param `FinishControl` finish_control: structure that control finish criteria for metaheuristic execution
        :param int random_seed: random seed for metaheuristic execution
        :param `AdditionalStatisticsControl` additional_statistics_control: structure that controls additional 
        statistics obtained during population-based metaheuristic execution        
        :param `OutputControl` output_control: structure that controls output
        :param `TargetProblem` target_problem: problem to be solved
        :param `list[TargetSolution]` initial_solutions: population with initial solutions of the problem
        """
        if not isinstance(name, str):
                raise TypeError('Parameter \'name\' must be \'str\'.')
        if not isinstance(finish_control, FinishControl):
                raise TypeError('Parameter \'finish_control\' must be \'FinishControl\'.')
        if not isinstance(random_seed, Optional[int]):
                raise TypeError('Parameter \'random_seed\' must be \'int\' or \'None\'.')
        if not isinstance(additional_statistics_control, AdditionalStatisticsControl):
                raise TypeError('Parameter \'additional_statistics_control\' must be \'AdditionalStatisticsControl\'.')
        if not isinstance(output_control, OutputControl):
                raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
        if not isinstance(target_problem, TargetProblem):
                raise TypeError('Parameter \'target_problem\' must be \'TargetProblem\'.')
        if not isinstance(initial_solutions, list[TargetSolution]):
                raise TypeError('Parameter \'initial_solutions\' must be \'list[TargetSolution]\'.')
        super().__init__(name=name, 
                finish_control=finish_control,
                random_seed=random_seed,
                additional_statistics_control=additional_statistics_control,
                output_control=output_control, 
                target_problem=target_problem)
        if initial_solutions is not None: 
            self.__current_solutions:Optional[list[TargetSolution]] = initial_solutions.copy()
        else:
            self.__current_solutions:Optional[list[TargetSolution]] =  None

    @abstractmethod
    def __copy__(self)->'PopulationBasedMetaheuristic':
        """
        Internal copy of the current population based metaheuristic

        :return: new `PopulationBasedMetaheuristic` instance with the same properties
        :rtype: `PopulationBasedMetaheuristic`
        """
        met = deepcopy(self)
        return met

    @abstractmethod
    def copy(self)->'PopulationBasedMetaheuristic':
        """
        Copy the current population based metaheuristic
        
        :return: new `PopulationBasedMetaheuristic` instance with the same properties
        :rtype: `PopulationBasedMetaheuristic`
        """
        return self.__copy__()

    @property
    def current_solutions(self)->list[TargetSolution]:
        """
        Property getter for the current solutions used during population based metaheuristic execution

        :return: list of the :class:`uo.target_solution.TargetSolution` class subtype -- current solutions of the problem 
        :rtype: list[TargetSolution]        
        """
        return self.__current_solutions

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
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s = super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'current_solutions=' + str(self.current_solutions) + delimiter
        for _ in range(0, indentation):
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
