
from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from abc import ABCMeta, abstractmethod
from typing import Optional, TypeVar, Generic
from typing import Generic

from uo.solution.solution import Solution

from uo.algorithm.algorithm import Algorithm
from uo.algorithm.metaheuristic.genetic_algorithm.selection import Selection

class SelectionRoulette(Selection):
    
    def __init__(self, elite_count:int)->None:
        super().__init__(elite_count=elite_count)
        
    
    def selection(self, optimizer:Algorithm)->None:
        """
        GA selection

        :return: 
        :rtype: None
        """
        old_pop:Optional[list[Solution]] = optimizer.current_population
        if old_pop is None:
            raise AttributeError("Population should exist!")
        n:int = old_pop.length()
        if n<=0:
            raise AttributeError("Population should contain at least one individual")
        elc:int = self.elite_count
        if elc>=n:
            return