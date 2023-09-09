""" 
.. _py_max_ones_problem_int_solution_vns_support:

The :mod:`~app.max_ones_problem.max_ones_problem_binary_int_solution_vns_support` contains class :class:`~app.max_ones_problem.max_ones_problem_binary_int_solution_vns_support.MaxOnesProblemBinaryIntSolutionVnsSupport`, that represents solution of the :ref:`Problem_Max_Ones`, where `int` representation of the problem has been used.
"""

import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy

from random import choice
from random import randint

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import ObjectiveFitnessFeasibility
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import ProblemSolutionVnsSupport

class MaxOnesProblemBinaryIntSolutionVnsSupport(ProblemSolutionVnsSupport):
    
    def __init__(self)->None:
        return

    def __copy__(self):
        sol = deepcopy(self)
        return sol

    def copy(self):
        return self.__copy__()
        
    def vns_randomize(self, k:int, problem:TargetProblem, solution:TargetSolution, solution_codes:list[str])->bool:
        """
        Random VNS shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints 

        :param int k: int parameter for VNS
        :param `TargetProblem` problem: problem that is solved
        :param `TargetSolution` solution: solution used for the problem that is solved
        :param `list[str]` solution_codes: solution codes that should be randomized
        :return: if randomization is successful
        :rtype: bool
        """    
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for i in range(0,k):
                positions.append(choice(range(k)))
            new_representation:int = solution.representation
            mask:int = 0
            for p in positions:
                mask |= 1 << p
            mask = ~mask
            solution.representation ^= mask
            all_ok:bool = True
            for sc in solution_codes:
                sc_representation = int(sc,2)
                if sc_representation != 0:
                    comp_result:int = (sc_representation ^ new_representation).bit_count()
                    if comp_result > k:
                        all_ok = False
            if all_ok:
                break
        if tries < limit:
            solution.representation = new_representation
            solution.evaluate(problem)
            return True
        else:
            return False 

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the target solution instance

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
        :return: string representation of instance that controls output
        :rtype: str
        """        
        return 'MaxOnesProblemBinaryIntSolutionVnsSupport'

    def __str__(self)->str:
        """
        String representation of the cache control and statistics structure

        :return: string representation of the cache control and statistics structure
        :rtype: str
        """
        return self.string_representation('|')

    def __repr__(self)->str:
        """
        Representation of the cache control and statistics structure

        :return: string representation of cache control and statistics structure
        :rtype: str
        """
        return self.string_representation('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the cache control and statistics structure

        :param str spec: format specification
        :return: formatted cache control and statistics structure
        :rtype: str
        """
        return self.string_representation('|')
