""" 
..  _py_minimum_multi_cut_problem_bit_array_solution_vns_support:

The :mod:`~opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_bit_array_solution_vns_support` 
contains class :class:`~opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_bit_array_solution_vns_support.MinimumMultiCutProblemBitArraySolutionVnsSupport`, 
that represents supporting parts of the `VNS` algorithm, where solution of the :ref:`Problem_MinimumMultiCut` have `BitArray` 
representation.
"""
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy
from random import choice

from typing import TypeVar

from bitstring import BitArray

from uo.problem.problem import Problem
from uo.solution.solution import Solution
from uo.algorithm.metaheuristic.single_solution_metaheuristic import SingleSolutionMetaheuristic
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support import VnsShakingSupport

A_co = TypeVar("A_co", covariant=True)

class VnsShakingSupportRepresentationBitArray(VnsShakingSupport[BitArray,A_co]):
    
    def __init__(self, k_max:int)->None:
        """
        Create new `VnsLocalSearchSupportRepresentationBitArray` instance
        """
        super().__init__(k_max=k_max)


    def __copy__(self):
        """
        Internal copy of the `VnsShakingSupportRepresentationBitArray`

        :return: new `VnsShakingSupportRepresentationBitArray` instance with the same properties
        :rtype: `VnsShakingSupportRepresentationBitArray`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `VnsShakingSupportRepresentationBitArray` instance

        :return: new `VnsShakingSupportRepresentationBitArray` instance with the same properties
        :rtype: `VnsShakingSupportRepresentationBitArray`
        """
        return self.__copy__()

    def shaking(self, k:int, problem:Problem, solution:Solution, 
            optimizer:SingleSolutionMetaheuristic)->bool:
        """
        Random shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints 

        :param int k: int parameter for VNS
        :param `Problem` problem: problem that is solved
        :param `Solution` solution: solution used for the problem that is solved
        :param `SingleSolutionMetaheuristic` optimizer: optimizer that is executed
        :return: if randomization is successful
        :rtype: bool
        """    
        if optimizer.should_finish():
            return False
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            repres:BitArray = BitArray(solution.representation)
            positions:list[int] = []
            for _ in range(0,k):
                positions.append(choice(range(len(repres))))
            for pos in positions:
                repres.invert(pos)
            solution.representation = repres
            all_ok:bool = True
            if solution.representation.count(value=1) > self.k_max:
                all_ok = False
            if all_ok:
                break
        if tries < limit:
            if optimizer.should_finish():
                return False
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            optimizer.write_output_values_if_needed("after_step_in_iteration", "shaking")
            return True
        else:
            return False 

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the vns support structure

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
        :return: string representation of vns support instance
        :rtype: str
        """        
        return 'VnsShakingSupportRepresentationBitArray'

    def __str__(self)->str:
        """
        String representation of the vns support instance

        :return: string representation of the vns support instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the vns support instance

        :return: string representation of the vns support instance
        :rtype: str
        """
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the vns support instance

        :param str spec: format specification
        :return: formatted vns support instance
        :rtype: str
        """
        return self.string_rep('|')

