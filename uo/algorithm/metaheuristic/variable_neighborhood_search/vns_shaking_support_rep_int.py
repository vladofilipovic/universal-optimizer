""" 
.. _py_vns_shaking_support_rep_int:

The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_rep_int` contains 
class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsShakingSupportRepresentationInt`, 
that represents VNS shaking support, where `int` representation of the problem has been used.
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
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support import VnsShakingSupport

A_co = TypeVar("A_co", covariant=True)

class VnsShakingSupportRepresentationInt(VnsShakingSupport[int,A_co]):
    
    def __init__(self, dimension:int)->None:
        """
        Create new `VnsLocalSearchSupportRepresentationBitArray` instance
        """
        super().__init__(dimension=dimension)


    def __copy__(self):
        """
        Internal copy of the `VnsShakingSupportRepresentationInt`

        :return: new `VnsShakingSupportRepresentationInt` instance with the same properties
        :rtype: VnsShakingSupportRepresentationInt
        """
        sup = deepcopy(self)
        return sup

    def copy(self):
        """
        Copy the `VnsShakingSupportRepresentationInt`
        
        :return: new `VnsShakingSupportRepresentationInt` instance with the same properties
        :rtype: `VnsShakingSupportRepresentationInt`
        """        
        return self.__copy__()
        
    def shaking(self, k:int, problem:Problem, solution:Solution, 
            optimizer:SingleSolutionMetaheuristic)->bool:
        """
        Random VNS shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints 

        :param int k: int parameter for VNS
        :param `Problem` problem: problem that is solved
        :param `Solution` solution: solution used for the problem that is solved
        :param `Metaheuristic` optimizer: metaheuristic optimizer that is executed
        :return: if shaking is successful
        :rtype: bool
        """    
        if optimizer.should_finish():
            return False
        if k <= 0:
            return False
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for _ in range(0,k):
                positions.append(choice(range(self.dimension)))
            mask:int = 0
            for p in positions:
                mask |= 1 << p
            solution.representation ^= mask
            all_ok:bool = True
            if solution.representation.bit_count() > self.dimension:
                all_ok = False
            if all_ok:
                break
        if tries < limit:
            if optimizer.should_finish():
                return solution
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            return True
        else:
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
        return 'VnsShakingSupportRepresentationInt'

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
