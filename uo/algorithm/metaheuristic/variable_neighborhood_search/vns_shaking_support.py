""" 
The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support` module describes the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support.VnsShakingSupport`.
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
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic

R_co = TypeVar("R_co", covariant=True) 
A_co = TypeVar("A_co", covariant=True)

class VnsShakingSupport(Generic[R_co,A_co], metaclass=ABCMeta):
    
    @abstractmethod
    def shaking(self, k:int, problem:Problem, solution:Solution[R_co,A_co], optimizer:Metaheuristic)->bool:
        """
        Random VNS shaking of several parts such that new solution code does not differ more than supplied from all 
        solution codes inside collection

        :param int k: int parameter for VNS
        :param `Problem` problem: problem that is solved
        :param `Solution[R_co,A_co]` solution: solution used for the problem that is solved
        :param `Metaheuristic` optimizer: metaheuristic optimizer that is executed
        :param `list[R_co]` solution_representations: solution representations that should be shaken
        :return: if shaking is successful
        :rtype: bool
        """        
        raise NotImplementedError
