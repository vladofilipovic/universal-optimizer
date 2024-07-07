""" 
The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support` module describes the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support.VnsLocalSearchSupport`.
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
from uo.algorithm.metaheuristic.single_solution_metaheuristic import SingleSolutionMetaheuristic

R_co = TypeVar("R_co", covariant=True) 
A_co = TypeVar("A_co", covariant=True)

class VnsLocalSearchSupport(Generic[R_co,A_co], metaclass=ABCMeta):
    
    def __init__(self, dimension:int)->None:
        """
        Create new `VnsLocalSearchSupportStandardBestImprovementInt` instance

        :param int inner_dimension: determine neighborhood size where local search is executed
        """
        if dimension is None:
            raise ValueError('Parameter \'dimension\' must exists.')
        if not isinstance( dimension, int):
            raise TypeError('Parameter \'dimension\' must be int.')
        self.__dimension = dimension


    @property
    def dimension(self)->int:
        """
        Property getter for inner dimension of the local search 

        :return: dimension of the local search  
        :rtype: int
        """
        return self.__dimension

    @abstractmethod
    def local_search(self, k:int, problem:Problem, solution:Solution[R_co,A_co], 
            optimizer:SingleSolutionMetaheuristic)->bool:
        """
        Executes the local search procedure 
        
        :param int k: int parameter for VNS
        :param `Problem` problem: problem that is solved
        :param `Solution` solution: solution used for the problem that is solved
        :param `SingleSolutionMetaheuristic` optimizer: metaheuristic optimizer that is executed
        :return: result of the local search procedure 
        :rtype: if local search is successful
        """
        raise NotImplementedError