""" 
.. _py_max_ones_problem_int_solution:

The :mod:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_int_solution` contains class :class:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_int_solution.MaxOnesProblemBinaryIntSolution`, that represents solution of the :ref:`Problem_Max_Ones`, where `int` representation of the problem has been used.
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

from uo.utils.logger import logger

class MaxOnesProblemBinaryIntSolution(TargetSolution[int]):
    
    def __init__(self, random_seed:int=None)->None:
        """
        Create new `MaxOnesProblemBinaryIntSolution` instance

        :param int random_seed: random seed for initialization, default value `Null`
        """
        super().__init__("MaxOnesProblemBinaryIntSolution", random_seed, fitness_value=None, objective_value=None, 
                is_feasible=False)

    def __copy__(self):
        """
        Internal copy of the `MaxOnesProblemBinaryIntSolution`

        :return: new `MaxOnesProblemBinaryIntSolution` instance with the same properties
        :rtype: MaxOnesProblemBinaryIntSolution
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `MaxOnesProblemBinaryIntSolution`
        
        :return: new `MaxOnesProblemBinaryIntSolution` instance with the same properties
        :rtype: `MaxOnesProblemBinaryIntSolution`
        """
        return self.__copy__()
        
    def copy_to(self, destination)->None:
        """
        Copy the `MaxOnesProblemBinaryIntSolution` to the already existing destination `MaxOnesProblemBinaryIntSolution`

        :param `MaxOnesProblemBinaryIntSolution` destination: destination `MaxOnesProblemBinaryIntSolution`
        """
        destination = self.__copy__()

    def __make_to_be_feasible_helper__(self, problem:TargetProblem):
        """
        Helper function that modifies representation to be feasible

        :param `TargetProblem` problem: problem which is solved by solution
        """
        mask:int = ~0
        mask <<= 32-problem.dimension
        mask = ~mask 
        self.representation &= mask

    def random_init(self, problem:TargetProblem)->None:
        """
        Random initialization of the solution

        :param `TargetProblem` problem: problem which is solved by solution
        """
        if problem.dimension is None:
            raise ValueError("Problem dimension should not be None!")
        if problem.dimension <= 0:
            raise ValueError("Problem dimension should be positive!")
        if problem.dimension >= 32:
            raise ValueError("Problem dimension should be less than 32!")
        self.representation = randint(0, 2^problem.dimension-1)
        self.__make_to_be_feasible_helper__(problem)

    def solution_code(self)->str:
        """
        Solution code of the target solution

        :return: solution code
        :rtype: str 
        """
        return bin(self.__representation)

    def calculate_objective_fitness_feasibility(self, problem:TargetProblem)->ObjectiveFitnessFeasibility:
        """
        Fitness calculation of the max ones binary int solution

        :param TargetProblem problem: problem that is solved
        :return: objective value, fitness value and feasibility of the solution instance  
        :rtype: `ObjectiveFitnessFeasibility`
        """
        ones_count = self.representation.bit_count()
        return ObjectiveFitnessFeasibility(ones_count, ones_count, True)

    def native_representation_from_solution_code(self, representation_str:str)->int:
        """
        Obtain `int` representation from string representation of the integer binary solution of the Max Ones problem 

        :param str representation_str: solution's representation as string
        :return: solution's representation as int
        :rtype: int
        """
        ret:int = int(representation_str, 2)

    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        rep_1:int = self.native_representation_from_solution_code(solution_code_1)
        rep_2:int = self.native_representation_from_solution_code(solution_code_2)
        result = (rep_1 ^ rep_2).count(True)
        return result 


    def string_representation(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
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
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s += super().string_representation(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'representation=' + bin(self.__representation)
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the solution instance

        :return: string representation of the solution instance
        :rtype: str
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __repr__(self)->str:
        """
        Representation of the solution instance

        :return: string representation of the solution instance
        :rtype: str
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the solution instance

        :param str spec: format specification
        :return: formatted solution instance
        :rtype: str
        """
        return self.string_representation('\n', 0, '   ', '{', '}')
