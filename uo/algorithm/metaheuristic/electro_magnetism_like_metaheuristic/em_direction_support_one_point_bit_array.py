"""
..  _py_set_covering_problem_bit_array_solution_em_support:

The :mod:`~opt.single_objective.comb.set_covering_problem.set_covering_problem_bit_array_solution_em_support`
contains class :class:`~opt.single_objective.comb.set_covering_problem.set_covering_problem_bit_array_solution_em_support.SetCoveringProblemBitArraySolutionEmSupport`, 
that represents supporting parts of the `EM` algorithm, where solution of the :ref:`Problem_SetCovering` have `BitArray` 
representation.
"""
import sys
import numpy as np
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
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_direction_support import EmDirectionSupport

A_co = TypeVar("A_co", covariant=True)

class EmDirectionSupportOnePointBitArray(EmDirectionSupport[BitArray,A_co]):

    # MISLIM DA OVO NE TREBA UOPSTE MENI ILI VIDI DA LI NESTO UOPSTE TREBA DA SE PROSLEDI KAO PARAMETAR
    def __init__(self)->None:
        """
        Create new `EmDirectionSupport` instance
        """
        #self.__direction_probability:float = direction_probability

    # TREBACE SAMO AKO BUDEM NESTO DODAVALA U KONSTRUKTOR
    #@property
    #def direction_probability(self)->float:
        """
        Property getter for direction probability 

        :return: direction probability 
        :rtype: float
        """
      #  return self.__direction_probability    

    def __copy__(self):
        """
        Internal copy of the `EmDirectionSupportOnePointBitArray`

        :return: new `EmDirectionSupportOnePointBitArray` instance with the same properties
        :rtype: `EmDirectionSupportOnePointBitArray`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `EmDirectionSupportOnePointBitArray` instance

        :return: new `EmDirectionSupportOnePointBitArray` instance with the same properties
        :rtype: `EmDirectionSupportOnePointBitArray`
        """
        return self.__copy__()

    def direction(self, problem:Problem, solution1:Solution, solution2:Solution, optimizer:PopulationBasedMetaheuristic) -> None:
        """
        Executes direction within EM 
        
        :param `Problem` problem: problem that is solved
        :param `Solution` solution1: first parent 
        :param `Solution` solution2: second parent
        :param `PopulationBasedMetaheuristic` optimizer: optimizer that is executed
        :rtype: None
        """
        
        if solution1.representation is not None and solution2.representation is not None :
            # POGLEDAJ POSLE RADI LI OVAJ DEO UOPSTE OVAKO ILI BI TREBALO NESTO DRUGACIJE DA SE URADI
            bit_list1 = [int(bit) for bit in solution1.representation.bin]

            # Convert the list to a numpy array
            numpy_array1 = np.array(bit_list1)

            bit_list2 = [int(bit) for bit in solution2.representation.bin]

            # Convert the list to a numpy array
            numpy_array2 = np.array(bit_list2)
            force_direction = np.sum(np.abs(numpy_array1 - numpy_array2))
            return force_direction
        else:
            return 0

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
        return 'EmDirectionSupportOnePointBitArray'

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