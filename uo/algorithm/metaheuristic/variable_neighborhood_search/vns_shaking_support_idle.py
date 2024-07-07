""" 
.. _py_vns_shaking_support_standard_int:

The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_int` contains 
class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.VnsShakingSupportIdle`, 
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

R_co = TypeVar("R_co", covariant=True)
A_co = TypeVar("A_co", covariant=True)

class VnsShakingSupportIdle(VnsShakingSupport[R_co,A_co]):
    
    def __copy__(self):
        """
        Internal copy of the `VnsShakingSupportIdle`

        :return: new `VnsShakingSupportIdle` instance with the same properties
        :rtype: VnsShakingSupportIdle
        """
        sup = deepcopy(self)
        return sup

    def copy(self):
        """
        Copy the `VnsShakingSupportIdle`
        
        :return: new `VnsShakingSupportIdle` instance with the same properties
        :rtype: `VnsShakingSupportIdle`
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
        return 'VnsShakingSupportIdle'

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
