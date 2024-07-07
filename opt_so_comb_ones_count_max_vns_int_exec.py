from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_int import \
        VnsLocalSearchSupportStandardBestImprovementInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_int import \
        VnsShakingSupportStandardInt

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import \
                VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_int_solution import \
                OnesCountMaxProblemIntSolution

def main():
        dim:int = 24
        problem_to_solve:OnesCountMaxProblem = OnesCountMaxProblem.from_dimension(dimension=dim)
        solution:OnesCountMaxProblemIntSolution = OnesCountMaxProblemIntSolution()
        finish:FinishControl = FinishControl(criteria='evaluations & seconds', evaluations_max=500, seconds_max=10)
        vns_shaking_support:VnsShakingSupportStandardInt = \
                VnsShakingSupportStandardInt(dimension=dim)
        vns_ls_support:VnsLocalSearchSupportStandardBestImprovementInt = \
                VnsLocalSearchSupportStandardBestImprovementInt(dimension=dim)
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.problem = problem_to_solve
        vns_construction_params.solution_template = solution
        vns_construction_params.vns_shaking_support = vns_shaking_support
        vns_construction_params.vns_ls_support = vns_ls_support
        vns_construction_params.finish_control = finish
        vns_construction_params.random_seed = 43434343
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        bs = optimizer.optimize()
        print('Best solution representation: {}'.format(bs.representation))            
        print('Best solution code: {}'.format(bs.string_representation()))            
        print('Best solution objective:  {}'.format(bs.objective_value))
        print('Best solution fitness: {}'.format(bs.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()

