""" 
..  _py_max_ones_problem_bit_array_solution:

The :mod:`~app.max_ones_problem.max_ones_problem_bit_array_solution` contains class :class:`~app.max_ones_problem.max_ones_problem_bit_array_solution.MaxOnesProblemBitArraySolution`, that represents solution of the :ref:`Problem_Max_Ones`, where `BitArray` representation of the problem has been used.
"""
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

from copy import deepcopy
from random import choice
from random import random
from bitstring import BitArray

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import ObjectiveFitnessFeasibility
from uo.target_solution.target_solution import TargetSolution

from app.utils.logger import logger
from app.max_ones_problem.max_ones_problem import MaxOnesProblem


class MaxOnesProblemBitArraySolution(TargetSolution):
    
    def __init__(self)->None:
        """
        Create new MaxOnesProblemBitArraySolution instance
        """
        super().__init__("MaxOnesProblemBitArraySolution", fitness_value=None, objective_value=None, is_feasible=False)
        self.__representation:BitArray = BitArray()

    def __copy__(self):
        """
        Internal copy of the MaxOnesProblemBitArraySolution
        :return: MaxOnesProblemBitArraySolution -- new MaxOnesProblemBitArraySolution instance with the same properties
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the MaxOnesProblemBitArraySolution
        :return: MaxOnesProblemBitArraySolution -- new MaxOnesProblemBitArraySolution instance with the same properties
        """
        return self.__copy__()
        
    def copy_to(self, destination)->None:
        """
        Copy the MaxOnesProblemBitArraySolution to the already existing destination MaxOnesProblemBitArraySolution
        :param destination:MaxOnesProblemBitArraySolution -- destination MaxOnesProblemBitArraySolution
        """
        destination = self.__copy__()

    @property
    def representation(self)->BitArray:
        """
        Property getter for the target solution representation
        :return: BitArray -- the target solution instance representation
        """
        return self.__representation

    @representation.setter
    def representation(self, value:BitArray)->None:
        """
        Property setter for representation of the target solution
        :param value:BitArray -- representation of the target solution
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
        :return: str -- solution code 
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
        Fitness calculation of the max ones solution
        :param problem:TargetProblem -- problem that is solved
        :return: ObjectiveFitnessFeasibility -- objective value, fitness value and feasibility of the solution instance  
        """
        ones_count = 0
        for i in range(problem.dimension):
            if self.representation[i]:
                ones_count += 1
        return ObjectiveFitnessFeasibility(ones_count, ones_count, True)

    def representation_string_to_bit_array(self, representation_str:str)->BitArray:
        """
        Obtain BitArray representation from string representation
        :param representation_str:str -- solution's representation as string
        :return: BitArray -- solution's representation as BitArray
        """
        ret:BitArray(bin=representation_str)

    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        """
        Calculating distance between two solutions determined by its code
        :param solution_code_1:str -- solution code for the first solution
        :param solution_code_2:str -- solution code for the second solution
        """
        rep_1:BitArray = self.__representation_string_to_bit_array__(solution_code_1)
        rep_2:BitArray = self.__representation_string_to_bit_array__(solution_code_2)
        result = (rep_1 ^ rep_2).count(True)
        return result 

    def best_1_change_full(self, problem:TargetProblem)->bool:
        """
        Change the best one within solution, by trying "best improvement" approach 

        :param TargetProblem problem: problem that is solved
        :return: bool -- if the best one is changed, or not
        """        
        best_ind:int = None
        best_fv:float = self.fitness_value
        for i in range(0, len(self.representation)):
            self.representation.invert(i) 
            new_fv = self.calculate_objective_fitness_feasibility(problem).fitness_value
            if new_fv > best_fv:
                best_ind = i
                best_fv = new_fv
            self.representation.invert(i)
        if best_ind is not None:
            self.representation.invert(best_ind)
            self.evaluate(problem)
            if self.fitness_value != best_fv:
                raise Exception('Fitness calculation within best_1_change_full function is not correct.')
            return True
        return False

    def best_1_change_first(self, problem:TargetProblem)->bool:
        """
        Change the best one within solution, by trying "first improvement" approach 

        :param TargetProblem problem: problem that is solved
        :return: bool -- if the best one is changed, or not
        """        
        best_ind:int = None
        best_fv:float = self.fitness_value
        for i in range(0, len(self.representation)):
            self.representation.invert(i) 
            new_fv = self.calculate_objective_fitness_feasibility(problem).fitness_value
            if new_fv > best_fv:
                best_ind = i
                best_fv = new_fv
                self.evaluate(problem)
                if self.fitness_value != best_fv:
                    raise Exception('Fitness calculation within best_1_change_first function is not correct.')
                return True
        return False


    def string_representation(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- delimiter between fields
        :param indentation:int -- level of indentation
        :param indentation_symbol:str -- indentation symbol
        :param group_start -- group start string 
        :param group_end -- group end string 
        :return: str -- string representation of target solution instance
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
        :return: str -- string representation of the target solution instance
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __repr__(self)->str:
        """
        Representation of the target solution instance
        :return: str -- string representation of the solution instance
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the target solution instance
        :param spec: str -- format specification
        :return: str -- formatted target solution instance
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

