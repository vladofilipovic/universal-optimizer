from copy import deepcopy
from random import randint
from random import choice

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import ObjectiveFitnessFeasibility
from uo.target_solution.target_solution import TargetSolution

from uo.algorithm.algorithm import Algorithm
from uo.algorithm.output_control import OutputControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer_constructor_parameters import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import ProblemSolutionVnsSupport

class MaxOnesProblem(TargetProblem):

    def __init__(self, dim:int)->None:
        if dim <= 0:
            raise ValueError("Problem dimension should be positive!")
        if dim > 31:
            raise ValueError("Problem dimension should be less than 32")
        super().__init__("MaxOnesProblem", is_minimization=False, file_path=None, dimension=dim)   

    def __copy__(self):
        pr = deepcopy(self)
        return pr

    def copy(self):
        return self.__copy__()

    def load_from_file(self, data_format:str='txt')->None:
        return

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        return ''

    def __str__(self)->str:
        return ''
    def __repr__(self)->str:
        return ''

    def __format__(self, spec:str)->str:
        return ''


class MaxOnesProblemBinaryIntSolution(TargetSolution[int]):
    
    def __init__(self, random_seed:int=None)->None:
        super().__init__("MaxOnesProblemBinaryIntSolution", random_seed, fitness_value=None, objective_value=None, 
                is_feasible=False)

    def __copy__(self):
        sol = deepcopy(self)
        return sol

    def copy(self):
        return self.__copy__()
        
    def copy_to(self, destination)->None:
        destination = self.__copy__()

    def __make_to_be_feasible_helper__(self, problem:TargetProblem):
        mask:int = ~0
        mask <<= 32-problem.dimension
        mask = (mask % 0x100000000) >> (32-problem.dimension) 
        self.representation &= mask

    def init_random(self, problem:TargetProblem)->None:
        if problem.dimension is None:
            raise ValueError("Problem dimension should not be None!")
        if problem.dimension <= 0:
            raise ValueError("Problem dimension should be positive!")
        if problem.dimension >= 32:
            raise ValueError("Problem dimension should be less than 32!")
        self.representation = randint(0, 2^problem.dimension-1)
        self.__make_to_be_feasible_helper__(problem)

    def init_from(self, representation:int, problem:TargetProblem)->None:
        self.representation = representation

    def string_rep(self)->str:
        return bin(self.representation)

    def calculate_objective_fitness_feasibility_directly(self, representation:int, 
            problem:TargetProblem)->ObjectiveFitnessFeasibility:
        ones_count = representation.bit_count()
        return ObjectiveFitnessFeasibility(ones_count, ones_count, True)

    def native_representation(self, representation_str:str)->int:
        ret:int = int(representation_str, 2)
        return ret

    def representation_distance(solution_code_1:str, solution_code_2:str)->float:
        rep_1:int = self.native_representation(solution_code_1)
        rep_2:int = self.native_representation(solution_code_2)
        result = (rep_1 ^ rep_2).count(True)
        return result 

    def string_representation(self)->str:
        return bin(self.representation)

    def string_rep(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
        return ''

    def __str__(self)->str:
        return ''

    def __repr__(self)->str:
        return ''

    def __format__(self, spec:str)->str:
        return ''

class MaxOnesProblemBinaryIntSolutionVnsSupport(ProblemSolutionVnsSupport[int]):
    
    def __init__(self)->None:
        return

    def __copy__(self):
        sup = deepcopy(self)
        return sup

    def copy(self):
        return self.__copy__()
        
    def shaking(self, k:int, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryIntSolution, 
            optimizer:Algorithm)->bool:
        if optimizer.finish_control.evaluations_max > 0 and optimizer.evaluation > optimizer.finish_control.evaluations_max:
            return False
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for i in range(0,k):
                positions.append(choice(range(problem.dimension)))
            new_representation:int = solution.representation
            mask:int = 0
            for p in positions:
                mask |= 1 << p
            solution.representation ^= mask
            all_ok:bool = True
            if solution.representation.bit_count() > problem.dimension:
                all_ok = False
            if all_ok:
                break
        if tries < limit:
            optimizer.evaluation += 1
            solution.evaluate(problem)
            return True
        else:
            return False 

    def local_search_best_improvement(self, k:int, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryIntSolution, 
            optimizer: Algorithm)->MaxOnesProblemBinaryIntSolution:
        if optimizer.finish_control.evaluations_max > 0 and optimizer.evaluation > optimizer.finish_control.evaluations_max:
            return solution
        if k<1:
            return solution
        # ls_bi for k==1
        best_ind:int = None
        best_fv:float = solution.fitness_value
        for i in range(0, problem.dimension):
            mask:int = 1 << i
            solution.representation ^= mask 
            optimizer.evaluation +=1 
            new_triplet:ObjectiveFitnessFeasibility = solution.calculate_objective_fitness_feasibility(problem)
            if new_triplet.fitness_value > best_fv:
                best_ind = i
                best_fv = new_triplet.fitness_value
            solution.representation ^= mask 
        if best_ind is not None:
            mask:int = 1 << best_ind
            solution.representation ^= mask
            optimizer.evaluation += 1
            solution.evaluate(problem)
            if solution.fitness_value != best_fv:
                raise Exception('Fitness calculation within `local_search_best_improvement` function is not correct.')
        return solution

    def local_search_first_improvement(self, k:int, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryIntSolution, 
            optimizer: Algorithm)->MaxOnesProblemBinaryIntSolution:
        if optimizer.finish_control.evaluations_max > 0 and optimizer.evaluation > optimizer.finish_control.evaluations_max:
            return solution
        if k<1:
            return solution
        # ls_fi for k==1
        best_fv:float = solution.fitness_value
        for i in range(0, problem.dimension):
            mask:int = 1 << i
            solution.representation ^= mask 
            optimizer.evaluation += 1
            new_triplet:ObjectiveFitnessFeasibility = solution.calculate_objective_fitness_feasibility(problem)
            if new_triplet.fitness_value > best_fv:
                solution.objective_value = new_triplet.objective_value
                solution.fitness_value = new_triplet.fitness_value
                solution.is_feasible = new_triplet.is_feasible
                return solution
            solution.representation ^= mask
        return solution

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        return 'MaxOnesProblemBinaryIntSolutionVnsSupport'

    def __str__(self)->str:
        return self.string_rep('|')

    def __repr__(self)->str:
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        return self.string_rep('|')

def main():
    output_control:OutputControl = OutputControl(write_to_output=False)
    problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=24)
    solution:MaxOnesProblemBinaryIntSolution = MaxOnesProblemBinaryIntSolution()
    vns_support:MaxOnesProblemBinaryIntSolutionVnsSupport = MaxOnesProblemBinaryIntSolutionVnsSupport()
    vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
    vns_construction_params.output_control = output_control
    vns_construction_params.target_problem = problem_to_solve
    vns_construction_params.initial_solution = solution
    vns_construction_params.problem_solution_vns_support = vns_support
    vns_construction_params.evaluations_max = 500
    vns_construction_params.iterations_max = 0
    vns_construction_params.seconds_max= 10
    vns_construction_params.random_seed = 43434343
    vns_construction_params.keep_all_solution_codes = False
    vns_construction_params.distance_calculation_cache_is_used = False
    vns_construction_params.k_min = 1
    vns_construction_params.k_max = 3
    vns_construction_params.max_local_optima = 10
    vns_construction_params.local_search_type = 'local_search_first_improvement'
    optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
    optimizer.optimize()
    print('Best solution representation: {}'.format(optimizer.best_solution.representation))            
    print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))            
    print('Best solution objective:  {}'.format(optimizer.best_solution.objective_value))
    print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
    print('Number of iterations: {}'.format(optimizer.iteration))            
    print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()
