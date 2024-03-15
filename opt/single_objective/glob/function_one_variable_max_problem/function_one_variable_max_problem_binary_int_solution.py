
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
from random import randint

from uo.problem.problem import Problem
from uo.solution.quality_of_solution import QualityOfSolution
from uo.solution.solution import Solution

from uo.utils.logger import logger

from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem \
        import FunctionOneVariableMaxProblemMax

class FunctionOneVariableMaxProblemBinaryIntSolution(Solution[int,float]):
    
    def __init__(self, domain_from:float, domain_to:float, number_of_intervals:int, random_seed:int=None, 
            evaluation_cache_is_used:bool=False, 
            evaluation_cache_max_size:int=0,
            distance_calculation_cache_is_used:bool=False,
            distance_calculation_cache_max_size:int=0)->None:
        if not isinstance(domain_from, int | float):
            raise TypeError("Parameter \'domain_from\' must be \'int\' or \'float\'.")
        if not isinstance(domain_to, int | float):
            raise TypeError("Parameter \'domain_to\' must be \'int\' or \'float\'.")
        if domain_from >= domain_to:
            raise ValueError("Parameter \'domain_from\' should be smaller than \'domain_to\'.")
        if not isinstance(number_of_intervals, int):
            raise TypeError("Parameter \'number_of_intervals\' should be integer.")
        if number_of_intervals <= 0 :
            raise ValueError("Parameter \'number_of_intervals\' should be positive.")
        super().__init__(random_seed=random_seed, fitness_value=None, 
                fitness_values=None, objective_value=None, objective_values=None,
                is_feasible=False, evaluation_cache_is_used=evaluation_cache_is_used,
                evaluation_cache_max_size=evaluation_cache_max_size,
                distance_calculation_cache_is_used=distance_calculation_cache_is_used,
                distance_calculation_cache_max_size=distance_calculation_cache_max_size)
        self.__domain_from:float|int = domain_from
        self.__domain_to:float|int = domain_to
        self.__number_of_intervals:int = number_of_intervals

    def __copy__(self):
        sol = super().__copy__()
        sol.domain_from = self.domain_from
        sol.domain_to = self.domain_to
        sol.number_of_intervals = self.number_of_intervals
        return sol

    def copy(self):
        return self.__copy__()
        
    @property
    def domain_from(self)->float:
        return self.__domain_from    

    @domain_from.setter
    def domain_from(self, value:float|int)->None:
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError('Parameter \'domain_from\' must have type \'int\' or \'float\'.')
        self.__domain_from = value

    @property
    def domain_to(self)->float:
        return self.__domain_to    

    @domain_to.setter
    def domain_to(self, value:float|int)->None:
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError('Parameter \'domain_to\' must have type \'int\' or \'float\'.')
        self.__domain_to = value

    @property
    def number_of_intervals(self)->int:
        return self.__number_of_intervals    

    @number_of_intervals.setter
    def number_of_intervals(self, value:int)->None:
        if not isinstance(value, int):
            raise TypeError('Parameter \'number_of_intervals\' must have type \'int\'.')
        self.__number_of_intervals= value

    def obtain_feasible_representation(self, problem:FunctionOneVariableMaxProblemMax):
        if self.representation is None:
            raise ValueError('Solution representation should not be None.')
        if self.representation > self.number_of_intervals:
            return self.representation % self.number_of_intervals
        if self.representation < 0:
            return (-self.representation) % self.number_of_intervals
        return self.representation

    def argument(self, representation:int)->float:
        x:float = self.domain_from + representation * (self.domain_to - self.domain_from) / self.number_of_intervals
        return x
    
    def init_random(self, problem:FunctionOneVariableMaxProblemMax)->None:
        self.representation = randint(0, self.number_of_intervals)
        self.representation = self.obtain_feasible_representation(problem)

    def init_from(self, representation:int, problem:FunctionOneVariableMaxProblemMax)->None:
        if not isinstance(representation, int):
            raise TypeError('Parameter \'representation\' must have type \'int\'.')
        self.representation = representation

    def calculate_quality_directly(self, representation:int, problem:FunctionOneVariableMaxProblemMax)->QualityOfSolution:
        arg:float = self.argument(representation) 
        res:float = eval(problem.expression, {"x":arg}) 
        return QualityOfSolution(res, None, res, None, True)

    def native_representation(self, representation_str:str)->int:
        ret:int = int(representation_str, 2)
        return ret

    def representation_distance_directly(self, solution_code_1: str, solution_code_2: str) -> float:
        """
        Calculates the distance between two binary representations of solutions.

        Args:
            solution_code_1 (str): The binary representation of the first solution.
            solution_code_2 (str): The binary representation of the second solution.

        Returns:
            float: The representation distance between the two binary solutions.
        """
        rep_1: int = self.native_representation(solution_code_1)
        rep_2: int = self.native_representation(solution_code_2)
        result = (rep_1 ^ rep_2).bit_count()
        return result

    def string_rep(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
        s = delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s += super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'string_representation()=' + str(self.string_representation())
        s += delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __repr__(self)->str:
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        return self.string_rep('\n', 0, '   ', '{', '}')


