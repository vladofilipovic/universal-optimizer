

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

from uo.utils.logger import logger
from uo.utils.complex_counter_uniform_distinct import ComplexCounterUniformAscending

from uo.target_solution.target_solution import QualityOfSolution
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import \
        ProblemSolutionVnsSupport

from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem import \
        FunctionOneVariableProblem
from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem_binary_int_solution \
        import FunctionOneVariableProblemBinaryIntSolution

class FunctionOneVariableProblemBinaryIntSolutionVnsSupport(ProblemSolutionVnsSupport[int,float]):
    
    def __init__(self)->None:
        return

    def __copy__(self):
        sup = deepcopy(self)
        return sup

    def copy(self):
        return self.__copy__()
        
    def shaking(self, k:int, problem:FunctionOneVariableProblem, solution:FunctionOneVariableProblemBinaryIntSolution, 
            optimizer:Algorithm)->bool:
        if optimizer.finish_control.check_evaluations and \
                optimizer.evaluation > optimizer.finish_control.evaluations_max:
            return False
        tries:int = 0
        limit:int = 10000
        representation_length:int = 32
        while tries < limit:
            positions:list[int] = []
            for i in range(0,k):
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
            optimizer.evaluation += 1
            if optimizer.finish_control.check_evaluations and \
                    optimizer.evaluation > optimizer.finish_control.evaluations_max:
                return False
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            return True
        else:
            return False 

    def local_search_best_improvement(self, k:int, problem:FunctionOneVariableProblem, 
            solution:FunctionOneVariableProblemBinaryIntSolution, 
            optimizer: Algorithm)->FunctionOneVariableProblemBinaryIntSolution:
        representation_length:int = 32
        if optimizer.finish_control.check_evaluations and \
                optimizer.evaluation > optimizer.finish_control.evaluations_max:
            return solution
        if k < 1 or k > representation_length:
            return solution
        best_rep:int = None
        best_triplet:QualityOfSolution =  QualityOfSolution(solution.objective_value,
                solution.fitness_value, solution.is_feasible)
        # initialize indexes
        indexes:ComplexCounterUniformAscending = ComplexCounterUniformAscending(k,representation_length)
        in_loop:boolean = indexes.reset()
        while in_loop:
            # collect positions for inversion from indexes
            positions:list[int] = indexes.current_state()
            # invert and compare, switch of new is better
            mask:int = 0
            for i in positions:
                mask |= 1 << i
            solution.representation ^= mask 
            optimizer.evaluation += 1
            if optimizer.finish_control.check_evaluations and \
                    optimizer.evaluation > optimizer.finish_control.evaluations_max:
                return solution
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            new_triplet = solution.calculate_quality(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            if new_triplet.fitness_value > best_triplet.fitness_value:
                best_triplet = new_triplet
                best_rep = solution.representation
            solution.representation ^= mask 
            # increment indexes and set in_loop accordingly
            in_loop = indexes.progress()
        if best_rep is not None:
            solution.representation = best_rep
            solution.objective_value = best_triplet.objective_value
            solution.fitness_value = best_triplet.fitness_value
            solution.is_feasible = best_triplet.is_feasible
            return solution
        return solution

    def local_search_first_improvement(self, k:int, problem:FunctionOneVariableProblem, 
            solution:FunctionOneVariableProblemBinaryIntSolution, 
            optimizer: Algorithm)->FunctionOneVariableProblemBinaryIntSolution:
        representation_length:int = 32
        if optimizer.finish_control.check_evaluations and \
                optimizer.evaluation > optimizer.finish_control.evaluations_max:
            return solution
        if k < 1 or k > representation_length:
            return solution
        best_fv:float = solution.fitness_value
        # initialize indexes
        indexes:ComplexCounterUniformAscending = ComplexCounterUniformAscending(k,representation_length)
        in_loop:boolean = indexes.reset()
        while in_loop:
            # collect positions for inversion from indexes
            positions:list[int] = indexes.current_state()
            # invert and compare, switch and exit if new is better
            mask:int = 0
            for i in positions:
                mask |= 1 << i
            solution.representation ^= mask 
            optimizer.evaluation += 1
            if optimizer.finish_control.check_evaluations and \
                    optimizer.evaluation > optimizer.finish_control.evaluations_max:
                return solution
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            new_triplet = solution.calculate_quality(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            if new_triplet.fitness_value > best_fv:
                solution.fitness_value = new_triplet.fitness_value
                solution.objective_value = new_triplet.objective_value
                solution.is_feasible = new_triplet.is_feasible
                return solution
            solution.representation ^= mask
            # increment indexes and set in_loop accordingly
            in_loop = indexes.progress()
        return solution

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        return 'FunctionOneVariableProblemBinaryIntSolutionVnsSupport'

    def __str__(self)->str:
        return self.string_rep('|')

    def __repr__(self)->str:
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        return self.string_rep('|')
