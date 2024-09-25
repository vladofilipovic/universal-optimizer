"""
The :mod:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support` module describes the class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support.EmMutationSupport`.
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
from uo.algorithm.metaheuristic.population_based_metaheuristic import PopulationBasedMetaheuristic

R_co = TypeVar("R_co", covariant=True)
A_co = TypeVar("A_co", covariant=True)

class EmMutationSupport(Generic[R_co,A_co], metaclass=ABCMeta):
    
    @abstractmethod
    def mutation(self, problem:Problem, solution:Solution[R_co,A_co],  
                optimizer:PopulationBasedMetaheuristic)->None:
        """
        EM individual mutation based on some probability

        :param `Problem` problem: problem that is solved
        :param `Solution[R_co,A_co]` solution: individual that is mutated
        :param `PopulationBasedMetaheuristic` optimizer: metaheuristic optimizer that is executed
        :return: None
        """
        raise NotImplementedError