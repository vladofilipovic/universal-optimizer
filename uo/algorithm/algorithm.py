""" 
The :mod:`~uo.algorithm.algorithm` module describes the class :class:`~uo.algorithm.Algorithm`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from datetime import datetime

from abc import ABCMeta, abstractmethod

from typing import Optional

from uo.utils.logger import logger
from uo.algorithm.output_control import OutputControl
from uo.problem.problem import Problem
from uo.solution.quality_of_solution import QualityOfSolution
from uo.solution.solution import Solution

from uo.algorithm.optimizer import Optimizer
    
class Algorithm(Optimizer, metaclass=ABCMeta):
    """
    This class describes Algorithm.

    Attributes:
        name (str): The name of the algorithm.
        output_control (OutputControl): The structure that controls output.
        problem (Problem): The problem to be solved.
        solution_template (Optional[Solution]): The solution template for the problem to be solved.

    Properties:
        solution_template (Optional[Solution]): The solution template for the problem to be solved.
        evaluation (int): The current number of evaluations during algorithm execution.
        iteration (int): The iteration of metaheuristic execution.
        iteration_best_found (int): The iteration when the best solution is found.

    Methods:
        __init__(name: str, output_control: OutputControl, problem: Problem, solution_template: Optional[Solution] = None) -> None:
            Create a new Algorithm instance.
        __copy__() -> Algorithm:
            Internal copy of the current algorithm.
        copy() -> Algorithm:
            Copy the current algorithm.
        init() -> None:
            Initialization of the algorithm.
        string_rep(delimiter: str, indentation: int = 0, indentation_symbol: str = '', group_start: str = '{', group_end: str = '}') -> str:
            String representation of the 'Algorithm' instance.
        __str__() -> str:
            String representation of the 'Algorithm' instance.
        __repr__() -> str:
            Representation of the 'Algorithm' instance.
        __format__(spec: str) -> str:
            Formatted 'Algorithm' instance.
    """

    @abstractmethod
    def __init__(self, 
                name:str, 
                output_control:Optional[OutputControl], 
                problem:Problem,
                solution_template:Solution)->None:
        """
        Create new Algorithm instance

        :param str name: name of the algorithm
        :param `OutputControl` output_control: structure that controls output
        :param `Problem` problem: problem to be solved
        :param `Solution` solution_template: solution for the problem that is solved
        """
        if not isinstance(name, str):
                raise TypeError('Parameter \'name\' must be \'str\'.')
        if not isinstance(output_control, OutputControl) and output_control is not None:
                raise TypeError('Parameter \'output_control\' must be \'OutputControl\' or None.')
        if not isinstance(problem, Problem):
                raise TypeError('Parameter \'problem\' must be \'Problem\'.')
        if not isinstance(solution_template, Solution):
                raise TypeError('Parameter \'solution_template\' must be \'Solution\'.')
        super().__init__(name=name, output_control=output_control, problem=problem)
        self.__solution_template:Solution = solution_template
        self.__evaluation:int = 0
        self.__iteration:int = 0
        self.__evaluation_best_found:int = 0
        self.__iteration_best_found:int = 0

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current algorithm

        :return:  new `Algorithm` instance with the same properties
        :rtype: :class:`uo.algorithm.Algorithm`
        """
        alg = deepcopy(self)
        return alg

    @abstractmethod
    def copy(self):
        """
        Copy the current algorithm

        :return:  new `Algorithm` instance with the same properties
        :rtype: :class:`uo.algorithm.Algorithm`
        """
        return self.__copy__()

    @Optimizer.best_solution.setter
    def best_solution(self, value:Solution)->None:
        """
        Property setter for the best solution so far
        
        :param Solution value: best solution so far
        """
        super(Algorithm, self.__class__).best_solution.fset(self, value)
        self.__evaluation_best_found = self.evaluation
        self.__iteration_best_found = self.iteration

    @property
    def solution_template(self)->Solution:
        """
        Property getter for the solution template for the problem to be solved
        
        :return: solution template for the problem to be solved 
        :rtype: `Solution`
        """
        return self.__solution_template

    @property
    def evaluation(self)->int:
        """
        Property getter for current number of evaluations during algorithm execution
        
        :return: current number of evaluations 
        :rtype: int
        """
        return self.__evaluation

    @evaluation.setter
    def evaluation(self, value:int)->None:
        """
        Property setter for current number of evaluations
        """
        if not isinstance(value, int):
            raise TypeError('Parameter \'evaluation\' must have type \'int\'.')
        self.__evaluation = value

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
        if not isinstance(value, int):
            raise TypeError('Parameter \'iteration\' must have type \'int\'.')
        self.__iteration = value

    @property
    def iteration_best_found(self)->int:
        """
        Property getter for the iteration when the best solution is found
        
        :return: iteration when the best solution is found
        :rtype: int
        """
        return self.__iteration_best_found

    @iteration_best_found.setter
    def iteration_best_found(self, value:int)->None:
        """
        Property setter the iteration when the best solution is found
        
        :param int value: iteration when the best solution is found
        """
        if not isinstance(value, int):
            raise TypeError('Parameter \'iteration_best_found\' must have type \'int\'.')
        self.__iteration_best_found = value

    @property
    def evaluation_best_found(self)->int:
        """
        Property getter for the evaluation when the best solution is found
        
        :return: evaluation when the best solution is found
        :rtype: int
        """
        return self.__evaluation_best_found

    @evaluation_best_found.setter
    def evaluation_best_found(self, value:int)->None:
        """
        Property setter the evaluation when the best solution is found
        
        :param int value: evaluation when the best solution is found
        """
        if not isinstance(value, int):
            raise TypeError('Parameter \'evaluation_best_found\' must have type \'int\'.')
        self.__evaluation_best_found = value

    def determine_fields_val(self, fields_def:list[str], fields_val:list[str])->list[str]:
        """
        Determines fields values upon fields definition and old values 

        :param list[str] fields_def: list of field definitions
        :param list[str] fields_val: list of old field values
        :return: list of new field values
        :rtype: list[str]
        """ 
        for i in range(len(fields_def)):
            f_def = fields_def[i]
            old_val = fields_val[i]
            if f_def != "" and old_val == "XXX":
                s_data = "XXX"
                if f_def == "evaluation":
                    s_data = str(self.evaluation)
                elif f_def == "iteration":
                    s_data = str(self.iteration)
                elif f_def == "evaluation_best_found":
                    s_data = str(self.evaluation_best_found)
                elif f_def == "iteration_best_found":
                    s_data = str(self.iteration_best_found)
                fields_val[i] = s_data
        fields_val = super().determine_fields_val(fields_def, fields_val)
        return fields_val

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the 'Algorithm' instance
        
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
        s = group_start
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'name=' + self.name + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'problem=' + self.problem.string_rep(delimiter, indentation + 1, 
                indentation_symbol, '{', '}')  + delimiter 
        for _ in range(0, indentation):
            s += indentation_symbol  
        if self.solution_template is not None:
            s += 'solution_template=' + self.solution_template.string_rep(delimiter, indentation + 1, 
                    indentation_symbol, '{', '}')  + delimiter 
        else:
            s += 'solution_template=None' + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += '__evaluation=' + str(self.__evaluation) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += '__iteration=' + str(self.__iteration) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += '__iteration_best_found=' + str(self.__iteration_best_found) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the 'Algorithm' instance
        
        :return: string representation of the 'Algorithm' instance
        :rtype: str
        """
        return self.string_rep('|')

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the 'Algorithm' instance
        
        :return: string representation of the 'Algorithm' instance
        :rtype: str
        """
        return self.string_rep('\n')

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted 'Algorithm' instance
        
        :param str spec: format specification
        :return: formatted 'Algorithm' instance
        :rtype: str
        """
        return self.string_rep('|')


