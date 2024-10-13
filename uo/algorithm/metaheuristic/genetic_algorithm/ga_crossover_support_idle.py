"""
..  _py_ga_crossover_support_idle:

The :mod:`~uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support_idle`
contains class :class:`uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support_idle.GaCrossoverSupportIdle`, 
that represents supporting parts of the `GA` algorithm.
"""
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

from typing import TypeVar


from copy import deepcopy
from random import choice, random, randint

from bitstring import BitArray

from uo.problem.problem import Problem
from uo.solution.solution import Solution
from uo.algorithm.metaheuristic.population_based_metaheuristic import PopulationBasedMetaheuristic
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support import GaCrossoverSupport

R_co = TypeVar("R_co", covariant=True)
A_co = TypeVar("A_co", covariant=True)

class GaCrossoverSupportIdle(GaCrossoverSupport[R_co, A_co]):

    def __copy__(self):
        """
        Internal copy of the `GaCrossoverSupportIdle`

        :return: new `GaCrossoverSupportIdle` instance with the same properties
        :rtype: `GaCrossoverSupportIdle`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `GaCrossoverSupportIdle` instance

        :return: new `GaCrossoverSupportIdle` instance with the same properties
        :rtype: `GaCrossoverSupportIdle`
        """
        return self.__copy__()

    def crossover(self, problem:Problem, solution1:Solution, solution2:Solution,
                child1:Solution, child2:Solution, optimizer:PopulationBasedMetaheuristic) -> None:
        """
        Executes crossover within GA 
        
        :param `Problem` problem: problem that is solved
        :param `Solution` solution1: first parent 
        :param `Solution` solution2: second parent
        :param `Solution` child1: first child 
        :param `Solution` child2: second child
        :param `PopulationBasedMetaheuristic` optimizer: optimizer that is executed
        :rtype: None
        """
        return None
        
    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the ga support structure

        :param delimiter: delimiter between fields
        :type delimiter: str
        :param indentation: level of indentation
        :type indentation: int, optional, default value 0
        :param indentation_symbol: indentation symbol
        :type indentation_symbol: str, optional, default value ''
        :param group_start: group start string 
        :type group_start: str, optional, default value '{'
        :param group_end: group end string 
        :type group_end: str, optional, default value '}'
        :return: string representation of ga support instance
        :rtype: str
        """
        return 'GaCrossoverSupportIdle'

    def __str__(self)->str:
        """
        String representation of the ga support instance

        :return: string representation of the ga support instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the ga support instance

        :return: string representation of the ga support instance
        :rtype: str
        """
        return self.string_rep('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted the ga support instance

        :param str spec: format specification
        :return: formatted ga support instance
        :rtype: str
        """
        return self.string_rep('|')

