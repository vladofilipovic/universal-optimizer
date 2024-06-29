"""
..  _py_ones_count_max_problem_binary_bit_array_solution_ga_support:

The :mod:`~opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_bit_array_solution_ga_support`
contains class :class:`~opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_bit_array_solution_ga_support.OnesCountMaxProblemBinaryBitArraySolutionGaSupport`, 
that represents supporting parts of the `GA` algorithm, where solution of the :ref:`Problem_MinimumMultiCut` have `BitArray` 
representation.
"""
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

from abc import ABCMeta, abstractmethod
from typing import NamedTuple
from typing import TypeVar
from typing import Generic
from typing import Optional


from copy import deepcopy
from random import choice, random, randint

from bitstring import BitArray

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizer
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support import GaCrossoverSupport

A_co = TypeVar("A_co", covariant=True)

class GaCrossoverSupportRepresentationBinaryBitArray(GaCrossoverSupport[BitArray,A_co]):

    def __init__(self, crossover_probability:float)->None:
        """
        Create new `GaCrossoverSupportRepresentationBinaryBitArray` instance
        """
        super().__init__(crossover_probability)

    def __copy__(self):
        """
        Internal copy of the `GaCrossoverSupportRepresentationBinaryBitArray`

        :return: new `GaCrossoverSupportRepresentationBinaryBitArray` instance with the same properties
        :rtype: `GaCrossoverSupportRepresentationBinaryBitArray`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `GaCrossoverSupportRepresentationBinaryBitArray` instance

        :return: new `GaCrossoverSupportRepresentationBinaryBitArray` instance with the same properties
        :rtype: `GaCrossoverSupportRepresentationBinaryBitArray`
        """
        return self.__copy__()

    def crossover(self, problem:Problem, solution1:Solution, solution2:Solution,
                child1:Solution, child2:Solution, optimizer:GaOptimizer) -> None:
        if solution1.representation is not None and solution2.representation is not None :
            child1.representation = BitArray(solution1.representation.len)
            child2.representation = BitArray(solution2.representation.len)
            if random() > self.crossover_probability:
                return
            index:int = randint(0,len(solution1.representation))
            for i in range(index):
                child1.representation.set(solution1.representation[i], i)
                child2.representation.set(solution2.representation[i], i)
            for i in range(index,solution1.representation.len):
                child1.representation.set(solution2.representation[i], i)
                child2.representation.set(solution1.representation[i], i)
            optimizer.evaluation += 2
            child1.evaluate(problem)
            child2.evaluate(problem)        
        else:
            child1.copy_from(solution1)
            child2.copy_from(solution2)
        

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
        return 'GaCrossoverSupportRepresentationBinaryBitArray'

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

