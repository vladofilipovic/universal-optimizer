
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

class Selection(Generic[R_co,A_co], metaclass=ABCMeta):
    
    @abstractmethod
    def selection(self, optimizer:Algorithm)->None:
        """
        GA selection

        :return: 
        :rtype: None
        """
        raise NotImplementedError
