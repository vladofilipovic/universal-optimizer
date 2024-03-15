""" 
.. _py_ones_count_max_problem_int_solution:

The :mod:`~opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_int_solution` contains class :class:`~opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_int_solution.OnesCountMaxProblemBinaryIntSolution`, that represents solution of the :ref:`Problem_Ones_Count_Max`, where `int` representation of the problem has been used.
"""

import sys
from pathlib import Path
from typing import Optional

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy
from random import choice
from random import randint

from uo.problem.problem import Problem
from uo.solution.quality_of_solution import QualityOfSolution
from uo.solution.solution import Solution

from uo.utils.logger import logger

class OnesCountMaxProblemBinaryIntSolution(Solution[int,str]):
    
    def __init__(self,random_seed:Optional[int]=None, 
            evaluation_cache_is_used:bool=False, 
            evaluation_cache_max_size:int=0,
            distance_calculation_cache_is_used:bool=False,
            distance_calculation_cache_max_size:int=0)->None:
        """
        Create new `OnesCountMaxProblemBinaryIntSolution` instance

        :param int random_seed: random seed for initialization, default value `Null`
        """
        if not isinstance(random_seed, int) and random_seed is not None:
            raise TypeError('Parameter \'random_seed\' must be \'int\' or \'None\'.')
        super().__init__(random_seed=random_seed, fitness_value=None, 
                fitness_values=None,
                objective_value=None, objective_values=None, is_feasible=False, 
                evaluation_cache_is_used=evaluation_cache_is_used,
                evaluation_cache_max_size=evaluation_cache_max_size, 
                distance_calculation_cache_is_used=distance_calculation_cache_is_used,
                distance_calculation_cache_max_size=distance_calculation_cache_max_size)

    def __copy__(self):
        """
        Internal copy of the `OnesCountMaxProblemBinaryIntSolution`

        :return: new `OnesCountMaxProblemBinaryIntSolution` instance with the same properties
        :rtype: OnesCountMaxProblemBinaryIntSolution
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `OnesCountMaxProblemBinaryIntSolution`
        
        :return: new `OnesCountMaxProblemBinaryIntSolution` instance with the same properties
        :rtype: `OnesCountMaxProblemBinaryIntSolution`
        """
        return self.__copy__()
        
    def obtain_feasible_representation(self, problem:Problem) -> int:
        """
        Helper function that modifies representation to be feasible

        :param `Problem` problem: problem which is solved by solution
        """
        if self.representation is None:
            raise ValueError('Solution representation should not be None.')
        mask:int = ~0
        mask <<= 32-problem.dimension
        mask = (mask % 0x100000000) >> (32-problem.dimension) 
        return self.representation & mask

    def argument(self, representation:int)->str:
        """
        Argument of the target solution for specific problem

        :param representation: internal representation of the solution
        :type representation: int
        :return: solution representation as string
        :rtype: str 
        """
        return bin(representation)

    def init_random(self, problem:OnesCountMaxProblem)->None:
        """
        Random initialization of the solution

        :param `Problem` problem: problem which is solved by solution
        """
        if problem.dimension is None:
            raise ValueError("Problem dimension should not be None!")
        if problem.dimension <= 0:
            raise ValueError("Problem dimension should be positive!")
        if problem.dimension >= 32:
            raise ValueError("Problem dimension should be less than 32!")
        self.representation = randint(0, 2 ^ problem.dimension - 1) 
        self.representation = self.obtain_feasible_representation(problem)

    def init_from(self, representation:int, problem:Problem)->None:
        """
        Initialization of the solution, by setting its native representation 

        :param int representation: representation that will be ste to solution
        :param `Problem` problem: problem which is solved by solution
        """
        if not isinstance(representation, int):
            raise TypeError('Parameter \'representation\' must have type \'int\'.')
        self.representation = representation

    def calculate_quality_directly(self, representation:int, 
            problem:Problem)->QualityOfSolution:
        """
        Fitness calculation of the max ones binary int solution

        :param int representation: native representation of the solution whose fitness, objective and feasibility is calculated
        :param Problem problem: problem that is solved
        :return: objective value, fitness value and feasibility of the solution instance  
        :rtype: `QualityOfSolution`
        """
        ones_count = representation.bit_count()
        return QualityOfSolution(ones_count, None, ones_count, None, True)

    def native_representation(self, representation_str:str)->int:
        """
        Obtain `int` representation from string representation of the integer binary solution of the Max Ones problem 

        :param str representation_str: solution's representation as string
        :return: solution's representation as int
        :rtype: int
        """
        ret:int = int(representation_str, 2)
        return ret

    def representation_distance_directly(self, solution_code_1:str, solution_code_2:str)->float:
        """
        Calculating distance between two solutions determined by its code

        :param str solution_code_1: solution code for the first solution
        :param str solution_code_2: solution code for the second solution
        :return: distance between two solutions represented by its code
        :rtype: float
        """
        rep_1:int = self.native_representation(solution_code_1)
        rep_2:int = self.native_representation(solution_code_2)
        result = (rep_1 ^ rep_2).bit_count()
        return result 


    def string_rep(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
        """
        String representation of the solution instance

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
        s = delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s += super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'string_representation()=' + self.string_representation()
        s += delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the solution instance

        :return: string representation of the solution instance
        :rtype: str
        """
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __repr__(self)->str:
        """
        Representation of the solution instance

        :return: string representation of the solution instance
        :rtype: str
        """
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the solution instance

        :param str spec: format specification
        :return: formatted solution instance
        :rtype: str
        """
        return self.string_rep('\n', 0, '   ', '{', '}')
