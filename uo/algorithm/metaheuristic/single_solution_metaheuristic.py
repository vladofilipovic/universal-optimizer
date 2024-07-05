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
from typing import Optional, TypeVar, Generic
from typing import Generic


from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic

class SingleSolutionMetaheuristic(Metaheuristic, metaclass=ABCMeta):
    """
    This class represent single solution metaheuristic
    """

    @abstractmethod
    def __init__(self, 
            finish_control:FinishControl,
            problem:Problem,
            solution_template:Optional[Solution],
            name:str, 
            output_control:Optional[OutputControl], 
            random_seed:Optional[int], 
            additional_statistics_control:Optional[AdditionalStatisticsControl]
    )->None:
        """
        Create new SingleSolutionMetaheuristic instance

        :param str name: name of the metaheuristic
        :param `FinishControl` finish_control: structure that control finish criteria for metaheuristic execution
        :param int random_seed: random seed for metaheuristic execution
        :param `Optional[AdditionalStatisticsControl]` additional_statistics_control: structure that controls additional 
        statistics obtained during population-based metaheuristic execution        
        :param `Optional[OutputControl]` output_control: structure that controls output
        :param `Problem` problem: problem to be solved
        :param `Optional[Solution]` solution_template: initial solution of the problem
        """
        super().__init__(
                finish_control=finish_control,
                problem=problem,
                solution_template=solution_template,
                name=name, 
                output_control=output_control,
                random_seed=random_seed,
                additional_statistics_control=additional_statistics_control)
        self.__current_solution:Optional[Solution] =  None

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
    def current_solution(self)->Optional[Solution]:
        """
        Property getter for the current solution used during single solution metaheuristic execution

        :return: instance of the :class:`uo.solution.Solution` class subtype -- current solution of the problem 
        :rtype: :class:`Solution`        
        """
        return self.__current_solution

    @current_solution.setter
    def current_solution(self, value:Optional[Solution])->None:
        """
        Property setter for the current solution used during single solution metaheuristic execution
        
        :param datetime value: the current solution used during single solution metaheuristic execution
        """
        if not isinstance(value, Solution) and value is not None:
            raise TypeError('Parameter \'current_solution\' must have type \'Solution\' or be None.')
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
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s = super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'current_solution=' + str(self.current_solution) + delimiter
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

