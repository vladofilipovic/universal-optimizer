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
from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.quality_of_solution import QualityOfSolution
from uo.target_solution.target_solution import TargetSolution

from uo.algorithm.optimizer import Optimizer
    
class Algorithm(Optimizer, metaclass=ABCMeta):
    """
    This class describes Algorithm.

    Attributes:
        name (str): The name of the algorithm.
        output_control (OutputControl): The structure that controls output.
        target_problem (TargetProblem): The problem to be solved.
        solution_template (Optional[TargetSolution]): The solution template for the problem to be solved.

    Properties:
        solution_template (Optional[TargetSolution]): The solution template for the problem to be solved.
        evaluation (int): The current number of evaluations during algorithm execution.
        iteration (int): The iteration of metaheuristic execution.
        iteration_best_found (int): The iteration when the best solution is found.

    Methods:
        __init__(name: str, output_control: OutputControl, target_problem: TargetProblem, solution_template: Optional[TargetSolution] = None) -> None:
            Create a new Algorithm instance.
        __copy__() -> Algorithm:
            Internal copy of the current algorithm.
        copy() -> Algorithm:
            Copy the current algorithm.
        is_first_better(sol1: TargetSolution, sol2: TargetSolution, problem: TargetProblem) -> Optional[bool]:
            Checks if the first solution is better than the second one, with respect to the problem that is optimized.
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
                output_control:OutputControl, 
                target_problem:TargetProblem,
                solution_template:Optional[TargetSolution] = None)->None:
        """
        Create new Algorithm instance

        :param str name: name of the algorithm
        :param `OutputControl` output_control: structure that controls output
        :param `TargetProblem` target_problem: problem to be solved
        """
        if not isinstance(name, str):
                raise TypeError('Parameter \'name\' must be \'str\'.')
        if not isinstance(output_control, OutputControl):
                raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
        if not isinstance(target_problem, TargetProblem):
                raise TypeError('Parameter \'target_problem\' must be \'TargetProblem\'.')
        if not isinstance(solution_template, TargetSolution) and solution_template is not None:
                raise TypeError('Parameter \'solution_template\' must be \'TargetSolution\' or None.')
        super().__init__(name=name, output_control=output_control, target_problem=target_problem)
        self.__solution_template:Optional[TargetSolution] = solution_template
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
    def best_solution(self, value:TargetSolution)->None:
        """
        Property setter for the best solution so far
        
        :param TargetSolution value: best solution so far
        """
        super(Algorithm, self.__class__).best_solution.fset(self, value)
        self.__evaluation_best_found = self.evaluation
        self.__iteration_best_found = self.iteration

    @property
    def solution_template(self)->Optional[TargetSolution]:
        """
        Property getter for the solution template for the problem to be solved
        
        :return: solution template for the problem to be solved 
        :rtype: `TargetSolution`
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


    def is_first_better(self, sol1:TargetSolution, sol2:TargetSolution, problem: TargetProblem)->Optional[bool]:
        """
        Checks if first solution is better than the second one, with respect to problem that is optimized

        :param TargetSolution sol1: first solution
        :param TargetSolution sol2: second solution
        :param TargetProblem problem: problem to be solved
        :return: `True` if first is better, `False` if first is worse, `None` if quality of both 
                solutions are equal
        :rtype: bool
        """
        if problem.is_multi_objective is None:
            raise ValueError('Field \'is_multi_objective\' must not be None.')
        if problem.is_minimization is None:
            raise ValueError('Field \'is_minimization\' must not be None.')
        if not problem.is_multi_objective:
            fit1:Optional[float] = sol1.fitness_value;
            fit2:Optional[float] = sol2.fitness_value;
            # with fitness is better than without fitness
            if fit1 is None:
                if fit2 is not None:
                    return False
                else:
                    return None
            elif fit2 is None:
                return True
            # if better, return true
            if (problem.is_minimization and fit1 < fit2) or (not problem.is_minimization and fit1 > fit2):
                return True
            # if same fitness, return None
            if fit1 == fit2:
                return None
            # otherwise, return false
            return False
        else:
            raise RuntimeError('Comparison between solutions for multi objective optimization is not currently supported.')
        
    @abstractmethod
    def init(self)->None:
        """
        Initialization of the algorithm
        """
        raise NotImplementedError
    
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
        s += 'target_problem=' + self.target_problem.string_rep(delimiter, indentation + 1, 
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


