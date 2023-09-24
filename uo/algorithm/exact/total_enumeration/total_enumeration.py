""" 
The :mod:`~uo.algorithm.exact.total_enumeration` module describes the class :class:`~uo.algorithm.exact.total_enumeration.TotalEnumeration`.
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

from typing import TypeVar, Generic
from typing import Generic


from uo.utils.logger import logger

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.output_control import OutputControl
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.exact.total_enumeration.problem_solution_te_support import ProblemSolutionTeSupport

class TotalEnumeration(Algorithm):
    """
    This class represent total enumeration algorithm
    """

    def __init__(self, name:str, evaluations_max:int, seconds_max:int, random_seed:int, 
            keep_all_solution_codes:bool,
            distance_calculation_cache_is_used:bool,
            output_control:OutputControl, 
            target_problem:TargetProblem,
            problem_solution_te_support:ProblemSolutionTeSupport)->None:
        """
        Create new TotalEnumeration instance

        :param int evaluations_max: maximum number of evaluations for algorithm execution
        :param int seconds_max: maximum number of seconds for algorithm execution
        :param `OutputControl` output_control: structure that controls output
        :param `TargetProblem` target_problem: problem to be solved
        :param `ProblemSolutionTeSupport` problem_solution_te_support: placeholder for additional methods, specific for TE 
        """
        super().__init__(name='total_enumerations', 
                evaluations_max=evaluations_max, 
                seconds_max=seconds_max, 
                output_control=output_control, 
                target_problem=target_problem)
        if problem_solution_te_support is not None:
            if isinstance(problem_solution_te_support, ProblemSolutionTeSupport):
                self.__problem_solution_te_support:ProblemSolutionTeSupport = problem_solution_te_support.copy()
                self.__reset_method = self.__problem_solution_te_support.reset
                self.__progress_method = self.__problem_solution_te_support.progress
                self.__can_progress_method = self.__problem_solution_te_support.can_progress
            else:
                self.__problem_solution_te_support:ProblemSolutionTeSupport = problem_solution_te_support
                self.__reset_method = None
                self.__progress_method = None
                self.__can_progress_method = None
        else:
            self.__problem_solution_te_support:ProblemSolutionTeSupport = None
            self.__reset_method = None
            self.__progress_method = None
            self.__can_progress_method = None
        # current solution
        self.__current_solution = None

    def __copy__(self):
        """
        Internal copy of the current total enumeration algorithm

        :return: new `TotalEnumeration` instance with the same properties
        :rtype: `TotalEnumeration`
        """
        tot = deepcopy(self)
        return tot

    def copy(self):
        """
        Copy the current total enumeration algorithm
        
        :return: new `TotalEnumeration` instance with the same properties
        :rtype: `TotalEnumeration`
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


    def init(self):
        """
        Initialization of the total enumeration algorithm
        """
        self.__reset_method(self.target_problem,self.current_solution, self)
        self.current_solution.evaluate(self.target_problem);
        self.copy_to_best_solution(self.current_solution);

    def optimize(self):
        self.init()
        while self.__can_progress_method(self.target_problem,self.current_solution, self):
            new_is_better:bool = self.is_first_solution_better(self.current_solution, self.best_solution)
            if new_is_better:
                self.copy_to_best_solution(self.current_solution)
            self.__progress_method(self.target_problem,self.current_solution, self)

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the 'TotalEnumeration' instance
        
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
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the 'TotalEnumeration' instance
        
        :return: string representation of the 'TotalEnumeration' instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the 'TotalEnumeration' instance
        
        :return: string representation of the 'TotalEnumeration' instance
        :rtype: str
        """
        return self.string_rep('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted 'TotalEnumeration' instance
        
        :param str spec: format specification
        :return: formatted 'TotalEnumeration' instance
        :rtype: str
        """
        return self.string_rep('|')
