
from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from abc import ABCMeta, abstractmethod

from uo.algorithm.algorithm import Algorithm
from uo.algorithm.metaheuristic.genetic_algorithm.ga_selection import GaSelection

class GaSelectionIdle(GaSelection):
    
    def __init__(self)->None:
        super().__init__(elite_count=None)
    
    def selection(self, optimizer:Algorithm)->None:
        """
        GA selection

        :return: 
        :rtype: None
        """
        return None
