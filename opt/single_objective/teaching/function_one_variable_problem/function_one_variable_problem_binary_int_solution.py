
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

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import QualityOfSolution
from uo.target_solution.target_solution import TargetSolution

from uo.utils.logger import logger

from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem \
        import FunctionOneVariableProblem

class FunctionOneVariableProblemBinaryIntSolution(TargetSolution[int,float]):
    
    def __init__(self, domain_from:float, domain_to:float, number_of_intervals:int, random_seed:int=None, 
            evaluation_cache_is_used:bool=False, 
            evaluation_cache_max_size:int=0,
            distance_calculation_cache_is_used:bool=False,
            distance_calculation_cache_max_size:int=0)->None:
        super().__init__("FunctionOneVariableProblemBinaryIntSolution", random_seed=random_seed, fitness_value=None, 
                objective_value=None, is_feasible=False, evaluation_cache_is_used=evaluation_cache_is_used,
                evaluation_cache_max_size=evaluation_cache_max_size,
                distance_calculation_cache_is_used=distance_calculation_cache_is_used,
                distance_calculation_cache_max_size=distance_calculation_cache_max_size)
        self.__domain_from:float = domain_from
        self.__domain_to:float = domain_to
        self.__number_of_intervals:int = number_of_intervals

    def __copy__(self):
        sol = super().__copy__()
        sol.domain_from = self.domain_from
        sol.domain_to = self.domain_to
        sol.number_of_intervals = self.number_of_intervals
        return sol

    def copy(self):
        return self.__copy__()
        
    def copy_to(self, destination)->None:
        destination = self.__copy__()

    @property
    def domain_from(self)->float:
        return self.__domain_from    

    @domain_from.setter
    def domain_from(self, value:float)->None:
        self.__domain_from = value

    @property
    def domain_to(self)->float:
        return self.__domain_to    

    @domain_to.setter
    def domain_to(self, value:float)->None:
        self.__domain_to = value

    @property
    def number_of_intervals(self)->int:
        return self.__number_of_intervals    

    @number_of_intervals.setter
    def number_of_intervals(self, value:int)->None:
        self.__number_of_intervals= value

    def __make_to_be_feasible_helper__(self, problem:FunctionOneVariableProblem):
        if self.representation > self.number_of_intervals:
            self.representation = self.number_of_intervals

    def argument(self, representation:int)->float:
        return self.domain_from + representation * (self.domain_to - self.domain_from) / self.number_of_intervals

    def init_random(self, problem:FunctionOneVariableProblem)->None:
        self.representation = randint(0, self.number_of_intervals)
        self.__make_to_be_feasible_helper__(problem)

    def init_from(self, representation:int, problem:FunctionOneVariableProblem)->None:
        self.representation = representation

    def calculate_quality_directly(self, representation:int, problem:FunctionOneVariableProblem)->QualityOfSolution:
        arg:float = self.argument(representation) 
        res:float = eval(problem.expression, {"x":arg})
        return QualityOfSolution(res, res, True)

    def native_representation(self, representation_str:str)->int:
        ret:int = int(representation_str, 2)
        return ret

    def representation_distance_directly(solution_code_1:str, solution_code_2:str)->float:
        rep_1:int = self.native_representation(solution_code_1)
        rep_2:int = self.native_representation(solution_code_2)
        result = (rep_1 ^ rep_2).count(True)
        return result 

    def string_rep(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
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
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __repr__(self)->str:
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        return self.string_rep('\n', 0, '   ', '{', '}')
