""" 
The :mod:`~uo.algorithm.exact.total_enumeration` module describes the class :class:`~uo.algorithm.exact.total_enumeration.TotalEnumeration`.
"""

from pathlib import Path

from uo.solution.quality_of_solution import QualityOfSolution
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

from typing import Optional, TypeVar, Generic
from typing import Generic
from typing import NamedTuple

from dataclasses import dataclass

from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.exact.total_enumeration.te_operations_support import TeOperationsSupport

@dataclass
class TeOptimizerConstructionParameters:
    """
    Instance of the class :class:`~uo.algorithm.exact.total_enumerations.TotalEnumerationConstructorParameters` represents constructor parameters for total enumeration algorithm.
    """
    output_control:Optional[OutputControl] = None
    problem:Optional[Problem] = None
    solution_template:Optional[Solution] = None
    te_operations_support:TeOperationsSupport = None

class TeOptimizer(Algorithm):
    """
    This class represent total enumeration algorithm
    """

    def __init__(self,   
            problem:Problem,
            solution_template:Optional[Solution],
            te_operations_support:TeOperationsSupport,
            output_control:Optional[OutputControl]=None
            )->None:
        """
        Create new TeOptimizer instance

        :param `Optional[OutputControl]` output_control: structure that controls output
        :param `Problem` problem: problem to be solved
        :param `TeOperationsSupport` te_operations_support: placeholder for operations, specific for TE 
        :param `Optional[Solution]` solution_template: solution from which algorithm started
        """
        if not isinstance(output_control, OutputControl) and output_control is not None:
                raise TypeError('Parameter \'output_control\' must be \'OutputControl\'. or None')
        if not isinstance(problem, Problem):
                raise TypeError('Parameter \'problem\' must be \'Problem\'.')
        if not isinstance(solution_template, Solution) and solution_template is not None:
                raise TypeError('Parameter \'solution_template\' must be \'Solution\' or None.')
        if not isinstance(te_operations_support, TeOperationsSupport):
                raise TypeError('Parameter \'te_operations_support\' must be \'TeOperationsSupport\'.')
        super().__init__(name='total_enumerations', 
                output_control=output_control, 
                problem=problem,
                solution_template=solution_template)
        # total enumeration support
        self.__te_operations_support:TeOperationsSupport = te_operations_support
        self.__reset_method = self.__te_operations_support.reset
        self.__progress_method = self.__te_operations_support.progress
        self.__can_progress_method = self.__te_operations_support.can_progress
        # current solution
        self.__current_solution:Optional[Solution] = None

    @classmethod
    def from_construction_tuple(cls, construction_tuple:TeOptimizerConstructionParameters):
        """
        Additional constructor, that creates new instance of class :class:`~uo.algorithm.exact.te_optimizer.TeOptimizer`. 

        :param `TeOptimizerConstructionParameters` construction_tuple: tuple with all constructor parameters
        """
        return cls(construction_tuple.problem, 
            construction_tuple.solution_template,
            construction_tuple.te_operations_support,
            construction_tuple.output_control)

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
    def current_solution(self)->Optional[Solution]:
        """
        Property getter for the current solution used during VNS execution

        :return: instance of the :class:`uo.solution.Solution` class subtype -- current solution of the problem 
        :rtype: :class:`Optional[Solution]`        
        """
        return self.__current_solution

    @current_solution.setter
    def current_solution(self, value:Optional[Solution])->None:
        """
        Property setter for the current solution used during VNS execution

        :param value: the current solution
        :type value: :class:`Optional[Solution]`
        """
        if not isinstance(value, Solution) and value is not None:
            raise TypeError('Parameter \'current_solution\' must have type \'Solution\' or be None.')
        self.__current_solution = value

    def init(self):
        """
        Initialization of the total enumeration algorithm
        """
        self.current_solution = self.solution_template.copy()
        self.__reset_method(self.problem,self.current_solution, self)
        self.write_output_values_if_needed("before_evaluation", "b_e")
        self.evaluation += 1
        self.current_solution.evaluate(self.problem);
        self.write_output_values_if_needed("after_evaluation", "a_e")
        self.best_solution = self.current_solution
        self.iteration = 1

    def optimize(self)->Solution:
        self.execution_started = datetime.now()
        self.init()
        logger.debug('Overall number of evaluations: {}'.format(
            self.__te_operations_support.overall_number_of_evaluations(self.problem, 
            self.current_solution, self)))
        self.write_output_headers_if_needed()
        self.write_output_values_if_needed("before_algorithm", "b_a")
        while True:
            self.write_output_values_if_needed("before_iteration", "b_i")
            self.iteration += 1
            self.__progress_method(self.problem, self.current_solution, self)
            new_is_better:bool = self.current_solution.is_better(self.best_solution, self.problem)
            if new_is_better:
                self.best_solution = self.current_solution
            self.write_output_values_if_needed("after_iteration", "a_i")
            if not self.__can_progress_method(self.problem,self.current_solution, self):
                break
        self.execution_ended = datetime.now()
        self.write_output_values_if_needed("after_algorithm", "a_a")
        return self.best_solution

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
