
from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from abc import ABCMeta, abstractmethod
from typing import Optional, TypeVar, Generic
from typing import Generic

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.algorithm import Algorithm

class Selection(metaclass=ABCMeta):
    
    
    def __init__(self, elite_count:Optional[int])->None:
        self.__elite_count:Optional[int] = elite_count
        self.__elite_solutions:Optional[list[Solution]] = None
        if(elite_count > 0):
            self.__elite_solutions = [None] * elite_count
            
    @property
    def elite_count(self)->Optional[int]:
        """
        Property getter for elitist count in selection 
        
        :return: count of elite number
        :rtype: Optional[int]
        """
        return self.__elite_count

    @elite_count.setter
    def elite_count(self, value:Optional[int])->None:
        """
        Property setter for elitist count in selection
        """
        self.__elite_count = value
        self.__elite_solutions = None
        if self.__elite_count > 0:
            self.__elite_solutions = [None] * self.__elite_count
        
    @property
    def elite_count(self)->Optional[int]:
        """
        Property getter for elitist count in selection 
        
        :return: count of elite number
        :rtype: Optional[int]
        """
        return self.__elite_count

    
    @abstractmethod
    def selection(self, optimizer:Algorithm)->None:
        """
        GA selection

        :return: 
        :rtype: None
        """
        raise NotImplementedError
