
from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from abc import ABCMeta, abstractmethod
from typing import Optional, TypeVar, Generic
from typing import Generic

from random import randint

from uo.solution.solution import Solution

from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizer
from uo.algorithm.metaheuristic.genetic_algorithm.ga_selection import GaSelection

class GaSelectionRoulette(GaSelection):
    
    
    def selection(self, optimizer:GaOptimizer)->None:
        """
        GA selection

        :return: 
        :rtype: None
        """
        pop:Optional[list[Solution]] = optimizer.current_population
        if pop is None:
            raise AttributeError("Population should exist!")
        n:int = len(pop)
        if n<=0:
            raise AttributeError("Population should contain at least one individual")
        n_e:Optional[int] = optimizer.elite_count
        if n_e is None:
            l_lim:int = 0
        else:
            l_lim:int = n_e
        temp:list[Solution] = []
        for _ in range(l_lim,n):
            ind:int = randint(0, n-1)
            temp.append(pop[ind])
        for i in range(l_lim,n):
            pop[i] = temp[i-l_lim]
