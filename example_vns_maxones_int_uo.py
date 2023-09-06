from copy import deepcopy
from random import randint
from random import choice

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import ObjectiveFitnessFeasibility
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

class MaxOneProblem(TargetProblem):

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

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        return ''

    def __str__(self)->str:
        return ''
    def __repr__(self)->str:
        return ''

    def __format__(self, spec:str)->str:
        return ''


class MaxOneProblemIntSolution(TargetSolution):
    
    def __init__(self)->None:
        super().__init__("MaxOneProblemIntSolution", fitness_value=None, objective_value=None, is_feasible=False)
        self.__representation = 42

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

    def random_init(self, problem:TargetProblem)->None:
        limit:int = (1 << problem.dimension)-1
        self.representation = randint(1, limit)
        # make solution feasible 
        mask:int = ~0
        mask <<= 32-problem.dimension
        mask = ~mask 
        self.__representation &= mask

    def solution_code(self)->str:
        return bin(self.__representation)

    def calculate_objective_fitness_feasibility(self, problem:TargetProblem)->ObjectiveFitnessFeasibility:
        ones_count = bin(self.representation).count("1")
        return ObjectiveFitnessFeasibility(ones_count, ones_count, True)

    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        rep_1:int = int(solution_code_1, 2)
        rep_2:int = int(solution_code_2, 2)
        result = (rep_1 ^ rep_2).count(True)
        return result 

    def best_1_change(self, problem:TargetProblem)->bool:
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
                raise Exception('Fitness calculation within best_1_change function is not correct.')
            return True
        return False

    def vns_randomize(self, problem:TargetProblem, k:int, solution_codes:list[str])->bool:
        """
        Random VNS shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints 
        :param problem:TargetProblem -- problem that is solved
        :param k:int -- parameter for VNS
        :param solution_codes:list[str] -- solution codes that should be randomized
        :return: bool -- if randomization is successful 
        """    
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for i in range(0,k):
                positions.append(choice(range(k)))
            new_representation:int = self.representation
            mask:int = 0
            for p in positions:
                mask |= 1 << p
            mask = ~mask
            self.representation ^= mask
            all_ok:bool = True
            for sc in solution_codes:
                sc_representation = int(sc,2)
                if sc_representation != 0:
                    comp_result:int = (sc_representation ^ new_representation).bit_count()
                    if comp_result > k:
                        all_ok = False
            if all_ok:
                break
        if tries < limit:
            self.representation = new_representation
            self.evaluate(problem)
            return True
        else:
            return False 

    def string_representation(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
        return ''

    def __str__(self)->str:
        return ''

    def __repr__(self)->str:
        return ''

    def __format__(self, spec:str)->str:
        return ''


problem_to_solve:MaxOneProblem = MaxOneProblem(dim=10)
initial_solution:MaxOneProblemIntSolution = MaxOneProblemIntSolution()
initial_solution.random_init(problem_to_solve)
optimizer:VnsOptimizer = VnsOptimizer(target_problem=problem_to_solve, 
        initial_solution=initial_solution, 
        evaluations_max=0, 
        seconds_max=10, 
        random_seed=None, 
        keep_all_solution_codes=False, 
        k_min=1, 
        k_max=3, 
        max_local_optima=10, 
        local_search_type='first_improvement')
optimizer.solution_code_distance_cache_cs.is_caching = False
optimizer.output_control.write_to_output_file = False
optimizer.optimize()
print('Best solution: {}'.format(optimizer.best_solution.solution_code()))            
print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value()))
print('Number of iterations: {}'.format(optimizer.iteration))            
