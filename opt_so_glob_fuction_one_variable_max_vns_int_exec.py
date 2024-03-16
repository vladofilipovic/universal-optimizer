from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem import \
                FunctionOneVariableMaxProblemMax
from opt.single_objective.glob.function_one_variable_max_problem.function_one_variable_max_problem_binary_int_solution \
                import FunctionOneVariableMaxProblemBinaryIntSolution
from opt.single_objective.glob.function_one_variable_max_problem.\
                function_one_variable_max_problem_binary_int_solution_vns_support \
                import FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport

def main():
        problem_to_solve:FunctionOneVariableMaxProblemMax = FunctionOneVariableMaxProblemMax.from_input_file(
                input_file_path='./opt/single_objective/glob/function_one_variable_max_problem/inputs/(7-x2)[-3,3].txt',
                input_format='txt')
        print('Problem: {}'.format(problem_to_solve))            
        solution:FunctionOneVariableMaxProblemBinaryIntSolution = FunctionOneVariableMaxProblemBinaryIntSolution(
                domain_from=problem_to_solve.domain_low, domain_to=problem_to_solve.domain_high, 
                number_of_intervals=6000, random_seed=43434343)
        solution.init_random(problem=problem_to_solve)
        solution.evaluate(problem_to_solve)           
        print('Solution: {}'.format(solution))
        finish:FinishControl = FinishControl(criteria='evaluations & seconds', evaluations_max=5000, seconds_max=10)
        vns_support:FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport = \
                FunctionOneVariableMaxProblemBinaryIntSolutionVnsSupport()
        output_control:OutputControl = OutputControl(write_to_output=False)
        additional_statistics_control:AdditionalStatisticsControl = AdditionalStatisticsControl(is_active=False)
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.output_control = output_control
        vns_construction_params.problem = problem_to_solve
        vns_construction_params.solution_template = solution
        vns_construction_params.problem_solution_vns_support = vns_support
        vns_construction_params.finish_control = finish
        vns_construction_params.random_seed = 43434343
        vns_construction_params.additional_statistics_control = additional_statistics_control
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        vns_construction_params.local_search_type = 'localSearchBestImprovement'
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