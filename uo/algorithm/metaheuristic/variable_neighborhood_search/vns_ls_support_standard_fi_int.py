""" 
.. _py_vns_ls_support_standard_bi_int:

The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_int` contains 
class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsLocalSearchSupportStandardFirstImprovementInt`, 
that represents VNS local search support, where `int` representation of the problem has been used.
"""

import sys
from pathlib import Path
from typing import Optional
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy
from random import choice
from random import randint

from typing import TypeVar

from uo.utils.logger import logger
from uo.utils.complex_counter_uniform_ascending import ComplexCounterUniformAscending


from uo.problem.problem import Problem
from uo.solution.solution import Solution
from uo.algorithm.metaheuristic.single_solution_metaheuristic import SingleSolutionMetaheuristic
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support import VnsLocalSearchSupport

A_co = TypeVar("A_co", covariant=True)

class VnsLocalSearchSupportStandardFirstImprovementInt(VnsLocalSearchSupport[int,A_co]):
    
    def __init__(self, dimension:int)->None:
        """
        Create new `VnsLocalSearchSupportStandardBestImprovementBitArray` instance
        """
        super().__init__(dimension=dimension)

    def __copy__(self):
        """
        Internal copy of the `VnsLocalSearchSupportStandardFirstImprovementInt`

        :return: new `VnsLocalSearchSupportStandardFirstImprovementInt` instance with the same properties
        :rtype: VnsLocalSearchSupportStandardFirstImprovementInt
        """
        sup = deepcopy(self)
        return sup

    def copy(self):
        """
        Copy the `VnsLocalSearchSupportStandardFirstImprovementInt`
        
        :return: new `VnsLocalSearchSupportStandardFirstImprovementInt` instance with the same properties
        :rtype: `VnsLocalSearchSupportStandardFirstImprovementInt`
        """        
        return self.__copy__()
        
    def local_search(self, k:int, problem:Problem, solution:Solution, 
            optimizer: SingleSolutionMetaheuristic)->bool:
        """
        Executes "first improvement" variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `Problem` problem: problem that is solved
        :param `Solution` solution: solution used for the problem that is solved
        :param `SingleSolutionMetaheuristic` optimizer: metaheuristic optimizer that is executed
        :return: result of the local search procedure 
        :rtype: if local search is successful
        """
        if optimizer.should_finish():
            return False
        if k < optimizer.k_min or k > optimizer.k_max:
            return False
        start_sol:Solution = solution.copy()
        # initialize indexes
        indexes:ComplexCounterUniformAscending = ComplexCounterUniformAscending(k, self.dimension)
        in_loop:bool = indexes.reset()
        while in_loop:
            # collect positions for inversion from indexes
            positions:list[int] = indexes.current_state()
            # invert and compare, switch and exit if new is better
            mask:int = 0
            for i in positions:
                mask |= 1 << i
            solution.representation ^= mask 
            if optimizer.should_finish():
                solution.copy_from(start_sol)
                return False
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            if solution.is_better(start_sol, problem):
                return True
            solution.representation ^= mask
            # increment indexes and set in_loop accordingly
            in_loop = indexes.progress()
        solution.copy_from(start_sol)
        return False

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the vns support instance

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
        return 'VnsLocalSearchSupportStandardFirstImprovementInt'

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
