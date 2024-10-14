"""
..  _py_set_covering_problem_bit_array_solution_em_support:

The :mod:`~opt.single_objective.comb.set_covering_problem.set_covering_problem_bit_array_solution_em_support`
contains class :class:`~opt.single_objective.comb.set_covering_problem.set_covering_problem_bit_array_solution_em_support.MinSetCoverProblemBitArraySolutionEmSupport`, 
that represents supporting parts of the `EM` algorithm, where solution of the :ref:`Problem_SetCovering` have `BitArray` 
representation.
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
import numpy as np

from bitstring import BitArray

from uo.problem.problem import Problem
from uo.solution.solution import Solution
from uo.algorithm.metaheuristic.population_based_metaheuristic import PopulationBasedMetaheuristic
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_attraction_support import EmAttractionSupport

A_co = TypeVar("A_co", covariant=True)

class EmAttractionSupportOnePointBitArray(EmAttractionSupport[BitArray,A_co]):

    # MISLIM DA OVO NE TREBA UOPSTE MENI ILI VIDI DA LI NESTO UOPSTE TREBA DA SE PROSLEDI KAO PARAMETAR
    def __init__(self)->None:
        """
        Create new `EmAttractionSupport` instance
        """
   

    def __copy__(self):
        """
        Internal copy of the `EmAttractionSupportOnePointBitArray`

        :return: new `EmAttractionSupportOnePointBitArray` instance with the same properties
        :rtype: `EmAttractionSupportOnePointBitArray`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `EmAttractionSupportOnePointBitArray` instance

        :return: new `EmAttractionSupportOnePointBitArray` instance with the same properties
        :rtype: `EmAttractionSupportOnePointBitArray`
        """
        return self.__copy__()

    def attraction(self, problem:Problem, solution1:Solution, solution2:Solution, charge1:float, charge2: float, optimizer:PopulationBasedMetaheuristic) -> float:
        """
        Executes attraction within EM 
        
        :param `Problem` problem: problem that is solved
        :param `Solution` solution1: first parent 
        :param `Solution` solution2: second parent
        :param 'float' charge1: charge of the first particle
        :param 'float' charge2: charge of the second particle
        :param `PopulationBasedMetaheuristic` optimizer: optimizer that is executed
        :rtype: float
        """
        
        if solution1.representation is not None and solution2.representation is not None :
            # POGLEDAJ POSLE RADI LI OVAJ DEO UOPSTE OVAKO ILI BI TREBALO NESTO DRUGACIJE DA SE URADI
            distance = np.sum(np.abs(solution1.representation ^ solution2.representation))
            if distance == 0:
                return 0
            force = charge1 * charge2 / (distance**2)
            return force

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the em support structure

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
        :return: string representation of em support instance
        :rtype: str
        """
        return 'EmAttractionSupportOnePointBitArray'

    def __str__(self)->str:
        """
        String representation of the em support instance

        :return: string representation of the em support instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the em support instance

        :return: string representation of the em support instance
        :rtype: str
        """
        return self.string_rep('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted the em support instance

        :param str spec: format specification
        :return: formatted em support instance
        :rtype: str
        """
        return self.string_rep('|')