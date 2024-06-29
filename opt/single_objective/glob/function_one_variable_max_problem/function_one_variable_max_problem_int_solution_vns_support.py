

import sys
from pathlib import Path
from typing import Optional
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy
from random import choice
from random import randint

from uo.utils.logger import logger
from uo.utils.complex_counter_uniform_ascending import ComplexCounterUniformAscending

from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support import VnsShakingSupport
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support import VnsLocalSearchSupport

from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem import \
        FunctionOneVariableMaxProblemMax
from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem_int_solution \
        import FunctionOneVariableMaxProblemIntSolution

class FunctionOneVariableMaxProblemIntSolutionVnsShakingSupport(VnsShakingSupport[int,float]):
    
    def __init__(self)->None:
        return

    def __copy__(self):
        sup = deepcopy(self)
        return sup

    def copy(self):
        return self.__copy__()
        
    def shaking(self, k:int, problem:FunctionOneVariableMaxProblemMax, solution:FunctionOneVariableMaxProblemIntSolution, 
            optimizer:Metaheuristic)->bool:
        if k <= 0:
            return False
        if optimizer.should_finish():
            return False
        tries:int = 0
        limit:int = 10000
        representation_length:int = 32
        while tries < limit:
            positions:list[int] = []
            for _ in range(0,k):
                positions.append(choice(range(representation_length)))
            mask:int = 0
            for p in positions:
                mask |= 1 << p
            solution.representation ^= mask
            all_ok:bool = True
            if solution.representation.bit_count() > representation_length:
                all_ok = False
            if all_ok:
                break
        if tries < limit:
            solution.representation = solution.obtain_feasible_representation(problem)
            if optimizer.should_finish():
                return False
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            return True
        else:
            return False 

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        return 'FunctionOneVariableMaxProblemIntSolutionVnsShakingSupport'

    def __str__(self)->str:
        return self.string_rep('|')

    def __repr__(self)->str:
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        return self.string_rep('|')

class FunctionOneVariableMaxProblemIntSolutionVnsLocalSearchSupport(VnsLocalSearchSupport[int,float]):
    
    def __init__(self)->None:
        return

    def __copy__(self):
        sup = deepcopy(self)
        return sup

    def copy(self):
        return self.__copy__()
        

    def local_search_best_improvement(self, k:int, problem:FunctionOneVariableMaxProblemMax, 
            solution:FunctionOneVariableMaxProblemIntSolution, 
            optimizer: Metaheuristic)->bool:
        representation_length:int = 32
        if optimizer.should_finish():
            return False
        if k < 1:
            return False
        start_sol:FunctionOneVariableMaxProblemIntSolution = solution.copy()
        best_sol:FunctionOneVariableMaxProblemIntSolution = solution.copy()
        better_sol_found:bool = False
        # initialize indexes
        indexes:ComplexCounterUniformAscending = ComplexCounterUniformAscending(k,representation_length)
        in_loop:bool = indexes.reset()
        while in_loop:
            # collect positions for inversion from indexes
            positions:list[int] = indexes.current_state()
            # invert and compare, switch of new is better
            mask:int = 0
            for i in positions:
                mask |= 1 << i
            solution.representation ^= mask 
            if optimizer.should_finish():
                solution.copy_from(best_sol)
                return False
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            if solution.is_better(best_sol, problem):
                better_sol_found = True
                best_sol.copy_from(solution)
            solution.representation ^= mask 
            # increment indexes and set in_loop accordingly
            in_loop = indexes.progress()
        if better_sol_found:
            solution.copy_from(best_sol)
            return True
        solution.copy_from(start_sol)
        return False

    def local_search_first_improvement(self, k:int, problem:FunctionOneVariableMaxProblemMax, 
            solution:FunctionOneVariableMaxProblemIntSolution, 
            optimizer: Metaheuristic)->bool:
        representation_length:int = 32
        if optimizer.should_finish():
            return False
        if k < 1:
            return False
        start_sol:FunctionOneVariableMaxProblemIntSolution = solution.clone()
        # initialize indexes
        indexes:ComplexCounterUniformAscending = ComplexCounterUniformAscending(k,representation_length)
        in_loop:bool = indexes.reset()
        while in_loop:
            # collect positions for inversion from indexes
            positions:list[int] = indexes.current_state()
            # invert and compare, switch and exit if new is better
            mask:int = 0
            for i in positions:
                mask |= 1 << i
            solution.representation ^= mask 
            if optimizer.should_finish():
                solution.copy_from(start_sol)
                return False
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            if solution.is_better(start_sol, problem):
                return True
            solution.representation ^= mask
            # increment indexes and set in_loop accordingly
            in_loop = indexes.progress()
        solution.copy_from(start_sol)
        return False

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        return 'FunctionOneVariableMaxProblemIntSolutionVnsLocalSearchSupport'

    def __str__(self)->str:
        return self.string_rep('|')

    def __repr__(self)->str:
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        return self.string_rep('|')



