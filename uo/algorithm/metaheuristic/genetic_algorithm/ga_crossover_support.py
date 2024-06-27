"""
The :mod:`~uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support` module describes the class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support.GaCrossoverSupport`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from abc import ABCMeta, abstractmethod
from typing import TypeVar
from typing import Generic

from uo.problem.problem import Problem
from uo.solution.solution import Solution
from uo.algorithm.algorithm import Algorithm

R_co = TypeVar("R_co", covariant=True)
A_co = TypeVar("A_co", covariant=True)

class GaCrossoverSupport(Generic[R_co,A_co], metaclass=ABCMeta):
    
    def __init__(self, crossover_probability:float)->None:
        """
        Create new `GaCrossoverSupport` instance
        """
        self.__crossover_probability:float = crossover_probability

    @property
    def crossover_probability(self)->float:
        """
        Property getter for crossover probability 

        :return: crossover probability 
        :rtype: float
        """
        return self.__crossover_probability    

    @abstractmethod
    def crossover(self, problem:Problem, 
                solution1:Solution[R_co,A_co], solution2:Solution[R_co,A_co], 
                child1:Solution[R_co,A_co], child2:Solution[R_co,A_co], optimizer:Algorithm):
        """
        GA crossover on two parents

        :param float crossover_probability: float parameter for crossover probability
        :param `Problem` problem: problem that is solved
        :param `Solution[R_co,A_co]` solution1: first parent
        :param `Solution[R_co,A_co]` solution2: second parent
        :param `Solution[R_co,A_co]` child1: first child that is created
        :param `Solution[R_co,A_co]` child2: second child that is created
        :param `Algorithm` optimizer: optimizer that is executed
        """
        raise NotImplementedError
    