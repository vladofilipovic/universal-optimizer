""" 
..  _py_max_ones_problem_bit_array_solution:

The :mod:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution` contains class :class:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution.MaxOnesProblemBinaryBitArraySolution`, that represents solution of the :ref:`Problem_Max_Ones`, where `BitArray` representation of the problem has been used.
"""
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy
from random import choice
from random import random
from bitstring import BitArray

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import ObjectiveFitnessFeasibility
from uo.target_solution.target_solution import TargetSolution

from uo.utils.logger import logger

class MaxOnesProblemBinaryBitArraySolution(TargetSolution):
    
    def __init__(self)->None:
        """
        Create new `MaxOnesProblemBinaryBitArraySolution` instance
        """
        super().__init__("MaxOnesProblemBinaryBitArraySolution", fitness_value=None, objective_value=None, is_feasible=False)
        self.__representation:BitArray = BitArray()

    def __copy__(self):
        """
        Internal copy of the `MaxOnesProblemBinaryBitArraySolution`

        :return: new `MaxOnesProblemBinaryBitArraySolution` instance with the same properties
        :rtype: MaxOnesProblemBinaryBitArraySolution
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `MaxOnesProblemBinaryBitArraySolution`
        
        :return: new `MaxOnesProblemBinaryBitArraySolution` instance with the same properties
        :rtype: `MaxOnesProblemBinaryBitArraySolution`
        """
        return self.__copy__()
        
    def copy_to(self, destination)->None:
        """
        Copy the `MaxOnesProblemBinaryBitArraySolution` to the already existing destination `MaxOnesProblemBinaryBitArraySolution`

        :param `MaxOnesProblemBinaryBitArraySolution` destination: destination `MaxOnesProblemBinaryBitArraySolution`
        """
        destination = self.__copy__()

    @property
    def representation(self)->BitArray:
        """
        Property getter for the target solution representation

        :return: the target solution instance representation
        :rtype: `bitstring.BitArray`
        """
        return self.__representation

    @representation.setter
    def representation(self, value:BitArray)->None:
        """
        Property setter for representation of the target solution

        :param `BitArray` value: representation of the target solution
        """
        self.__representation = value

    def random_init(self, problem:TargetProblem)->None:
        """
        Random initialization of the target solution
        """
        #logger.debug( "\nSolution: {}".format(self))
        self.representation = BitArray(problem.dimension)
        for i in range(problem.dimension):
            if random() > 0.5:
                self.representation[i] = True
            else:
                self.representation[i] = False


    def solution_code(self)->str:
        """
        Solution code of the target solution

        :return: solution code
        :rtype: str 
        """
        s:str = ''
        for bit in self.representation:
            if bit:
                s += '1'
            else:
                s += '0'
        return s

    def calculate_objective_fitness_feasibility(self, problem:TargetProblem)->ObjectiveFitnessFeasibility:
        """
        Fitness calculation of the max ones binary BitArray solution

        :param TargetProblem problem: problem that is solved
        :return: objective value, fitness value and feasibility of the solution instance  
        :rtype: `ObjectiveFitnessFeasibility`
        """
        ones_count = 0
        for i in range(problem.dimension):
            if self.representation[i]:
                ones_count += 1
        return ObjectiveFitnessFeasibility(ones_count, ones_count, True)

    def representation_string_to_bit_array(self, representation_str:str)->BitArray:
        """
        Obtain `BitArray` representation from string representation

        :param str representation_str: solution's representation as string
        :return: solution's representation as BitArray
        :rtype: `BitArray`
        """
        ret:BitArray(bin=representation_str)

    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        """
        Calculating distance between two solutions determined by its code

        :param str solution_code_1: solution code for the first solution
        :param str solution_code_2: solution code for the second solution
        :return: distance between two solutions represented by its code
        :rtype: float
        """
        rep_1:BitArray = self.__representation_string_to_bit_array__(solution_code_1)
        rep_2:BitArray = self.__representation_string_to_bit_array__(solution_code_2)
        result = (rep_1 ^ rep_2).count(True)
        return result 

    def string_representation(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
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
        s = delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s += super().string_representation(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'representation=' + str(self.__representation)
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the target solution instance

        :return: string representation of the target solution instance
        :rtype: str
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __repr__(self)->str:
        """
        Representation of the target solution instance

        :return: string representation of the solution instance
        :rtype: str
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the target solution instance

        :param str spec: format specification
        :return: formatted target solution instance
        :rtype: str
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

