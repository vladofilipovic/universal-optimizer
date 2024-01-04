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
        if not isinstance(name, str):
                raise TypeError('Parameter \'name\' must be \'str\'.')
        if not isinstance(output_control, OutputControl):
                raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
        if not isinstance(target_problem, TargetProblem):
                raise TypeError('Parameter \'target_problem\' must be \'TargetProblem\'.')
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

    @abstractmethod
    def init(self)->None:
        """
        Initialization of the algorithm
        """
        raise NotImplementedError

    def is_first_solution_better(self, sol1:TargetSolution, sol2:TargetSolution)->Optional[bool]:
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
            qos1:Optional[QualityOfSolution] = None
        else:
            qos1:Optional[QualityOfSolution] = sol1.calculate_quality(self.target_problem)
        if sol2 is None:
            qos2:Optional[QualityOfSolution] = None
        else:
            qos2:Optional[QualityOfSolution] = sol2.calculate_quality(self.target_problem)
        # with fitness is better than without fitness
        if qos1 is None:
            if qos2 is not None:
                return False
            else:
                return None
        elif qos2 is None:
            return True
        if qos1.fitness_value is not None or qos2.fitness_value is not None:
            return QualityOfSolution.is_first_fitness_better(qos1, qos2, is_minimization)
        return None

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


