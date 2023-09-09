""" 
.. _py_max_ones_problem_int_solution:

The :mod:`~app.max_ones_problem.max_ones_problem_binary_int_solution` contains class :class:`~app.max_ones_problem.max_ones_problem_binary_int_solution.MaxOnesProblemBinaryIntSolution`, that represents solution of the :ref:`Problem_Max_Ones`, where `int` representation of the problem has been used.
"""

import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy
from random import choice
from random import randint

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import ObjectiveFitnessFeasibility
from uo.target_solution.target_solution import TargetSolution

from app.utils.logger import logger

class MaxOnesProblemBinaryIntSolution(TargetSolution):
    
    def __init__(self)->None:
        super().__init__("MaxOnesProblemBinaryIntSolution", fitness_value=None, objective_value=None, is_feasible=False)

    def __copy__(self):
        sol = deepcopy(self)
        return sol

    def copy(self):
        return self.__copy__()
        
    def copy_to(self, destination)->None:
        destination = self.__copy__()

    @property
    def representation(self)->int:
            return self.__representation

    @representation.setter
    def representation(self, value:int)->None:
        self.__representation = value

    def make_to_be_feasible(self, problem:TargetProblem):
        mask:int = ~0
        mask <<= 32-problem.dimension
        mask = ~mask 
        self.__representation &= mask

    def random_init(self, problem:TargetProblem)->None:
        if problem.dimension is None:
            raise ValueError("Problem dimension should not be None!")
        if problem.dimension <= 0:
            raise ValueError("Problem dimension should be positive!")
        if problem.dimension >= 32:
            raise ValueError("Problem dimension should be less than 32!")
        self.representation = randint(0, 2^problem.dimension-1)
        self.make_to_be_feasible(problem)

    def solution_code(self)->str:
        return bin(self.__representation)

    def calculate_objective_fitness_feasibility(self, problem:TargetProblem)->ObjectiveFitnessFeasibility:
        ones_count = self.representation.bit_count()
        return ObjectiveFitnessFeasibility(ones_count, ones_count, True)

    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        rep_1:int = int(solution_code_1, 2)
        rep_2:int = int(solution_code_2, 2)
        result = (rep_1 ^ rep_2).count(True)
        return result 

    def best_1_change_full(self, problem:TargetProblem)->bool:
        best_ind:int = None
        best_fv:float = self.fitness_value
        for i in range(0, problem.dimension):
            mask:int = 1 << i
            mask = ~mask
            self.representation ^= mask 
            new_fv = self.calculate_objective_fitness_feasibility(problem).fitness_value
            if new_fv > best_fv:
                best_ind = i
                best_fv = new_fv
            self.representation ^= mask 
        if best_ind is not None:
            mask:int = 1 << best_ind
            mask = ~mask
            self.representation ^= mask
            self.evaluate(problem)
            if self.fitness_value != best_fv:
                raise Exception('Fitness calculation within best_1_change_full function is not correct.')
            return True
        return False

    def best_1_change_first(self, problem:TargetProblem)->bool:
        best_ind:int = None
        best_fv:float = self.fitness_value
        for i in range(0, problem.dimension):
            mask:int = 1 << i
            mask = ~mask
            self.representation ^= mask 
            new_fv = self.calculate_objective_fitness_feasibility(problem).fitness_value
            if new_fv > best_fv:
                best_ind = i
                best_fv = new_fv
                mask:int = 1 << best_ind
                mask = ~mask
                self.representation ^= mask
                self.evaluate(problem)
                if self.fitness_value != best_fv:
                    raise Exception('Fitness calculation within best_1_change_first function is not correct.')
                return True
        return False

    def string_representation(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
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
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __repr__(self)->str:
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        return self.string_representation('\n', 0, '   ', '{', '}')
