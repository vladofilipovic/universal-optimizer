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

from uo.utils.logger import logger
from uo.algorithm.output_control import OutputControl
from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution

from uo.algorithm.optimizer import Optimizer
    
class Algorithm(Optimizer, metaclass=ABCMeta):
    """
    This class describes Algorithm
    """

    @abstractmethod
    def __init__(self, name:str, output_control:OutputControl, target_problem:TargetProblem)->None:
        """
        Create new Algorithm instance

        :param str name: name of the algorithm
        :param `OutputControl` output_control: structure that controls output
        :param `TargetProblem` target_problem: problem to be solved
        """
        super().__init__(name=name, output_control=output_control, target_problem=target_problem)
        self.__evaluation:int = 0
        self.__iteration:int = 0
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
        self.__iteration = value

    @abstractmethod
    def init(self)->None:
        """
        Initialization of the algorithm
        """
        raise NotImplementedError

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
            fit1:float = sol1.calculate_quality(self.target_problem).fitness_value;
        if sol2 is None:
            fit2:float = None
        else:
            fit2:float = sol2.calculate_quality(self.target_problem).fitness_value;
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
        super().copy_to_best_solution(solution)
        self.__iteration_best_found = self.iteration

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
        for i in range(0, indentation):
            s += indentation_symbol  
        s = group_start
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'name=' + self.name + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'target_problem=' + self.target_problem.string_rep(delimiter, indentation + 1, 
                indentation_symbol, '{', '}')  + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__output_control=' + self.__output_control.string_rep(
                delimiter, indentation + 1, indentation_symbol, '{', '}') + delimiter
        s += '__evaluation=' + str(self.__evaluation) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'execution_started=' + str(self.execution_started) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'execution_ended=' + str(self.execution_ended) + delimiter
        for i in range(0, indentation):
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
