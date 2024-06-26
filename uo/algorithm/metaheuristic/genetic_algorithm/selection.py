
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
    

    @abstractmethod
    def selection(self, optimizer:Algorithm)->None:
        """
        GA selection

        :return: 
        :rtype: None
        """
        raise NotImplementedError
