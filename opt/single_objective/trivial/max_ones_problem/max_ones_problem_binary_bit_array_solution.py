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

from bitstring import Bits, BitArray, BitStream, pack

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import ObjectiveFitnessFeasibility
from uo.target_solution.target_solution import TargetSolution

from uo.utils.logger import logger

class MaxOnesProblemBinaryBitArraySolution(TargetSolution[BitArray]):
    
    def __init__(self, random_seed:int=None)->None:
        """
        Create new `MaxOnesProblemBinaryBitArraySolution` instance
        """
        super().__init__("MaxOnesProblemBinaryBitArraySolution", random_seed, fitness_value=None, 
                objective_value=None, is_feasible=False)

    def __copy__(self):
        """
        Internal copy of the `MaxOnesProblemBinaryBitArraySolution`

        :return: new `MaxOnesProblemBinaryBitArraySolution` instance with the same properties
        :rtype: MaxOnesProblemBinaryBitArraySolution
        """
        sol = super().__copy__()
        sol.representation = BitArray(bin=self.representation.bin)
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

    def string_representation(self)->str:
        """
        Solution code of the target solution

        :return: solution code
        :rtype: str 
        """
        return self.representation.bin

    def init_random(self, problem:TargetProblem)->None:
        """
        Random initialization of the solution

        :param `TargetProblem` problem: problem which is solved by solution
        """
        #logger.debug('Solution: ' + str(self))
        self.representation = BitArray(problem.dimension)
        for i in range(problem.dimension):
            if random() > 0.5:
                self.representation[i] = True

    def calculate_objective_fitness_feasibility_directly(self, representation:BitArray, 
            problem:TargetProblem)->ObjectiveFitnessFeasibility:
        """
        Fitness calculation of the max ones binary BitArray solution

        :param BitArray representation: native representation of solution whose fitness is calculated
        :param TargetProblem problem: problem that is solved
        :return: objective value, fitness value and feasibility of the solution instance  
        :rtype: `ObjectiveFitnessFeasibility`
        """
        ones_count = representation.count(True)
        return ObjectiveFitnessFeasibility(ones_count, ones_count, True)

    def native_representation(self, representation_str:str)->BitArray:
        """
        Obtain `BitArray` representation from string representation of the BitArray binary solution of the Max Ones problem 

        :param str representation_str: solution's representation as string
        :return: solution's representation as BitArray
        :rtype: `BitArray`
        """
        ret:BitArray = BitArray(bin=representation_str)
        return ret

    def representation_distance(solution_code_1:str, solution_code_2:str)->float:
        """
        Calculating distance between two solutions determined by its code

        :param str solution_code_1: solution code for the first solution
        :param str solution_code_2: solution code for the second solution
        :return: distance between two solutions represented by its code
        :rtype: float
        """
        rep_1:BitArray = self.native_representation(solution_code_1)
        rep_2:BitArray = self.native_representation(solution_code_2)
        result = (rep_1 ^ rep_2).count(True)
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
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s += super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'string_representation()=' + str(self.string_representation())
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

