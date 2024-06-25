
from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from abc import ABCMeta, abstractmethod

from uo.algorithm.algorithm import Algorithm
from uo.algorithm.metaheuristic.genetic_algorithm.selection import Selection

class SelectionIdle(Selection):
    
    def __init__(self)->None:
        super().__init__(elite_count=0)
    
    def selection(self, optimizer:Algorithm)->None:
        """
        GA selection

        :return: 
        :rtype: None
        """
        return None
