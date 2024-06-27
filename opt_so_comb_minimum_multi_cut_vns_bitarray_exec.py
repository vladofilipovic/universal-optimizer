from copy import deepcopy
from random import randint
from random import choice
from random import randint
import networkx as nx

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem import MinimumMultiCutProblem
from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution import \
                MinimumMultiCutProblemBinaryBitArraySolution
from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution_vns_support import \
                MinimumMultiCutProblemBinaryBitArraySolutionVnsShaking
from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution_vns_support import \
                MinimumMultiCutProblemBinaryBitArraySolutionVnsLocalSearchSupport

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)

        nodes = 10
        prob = 0.5

        graph: nx.Graph = nx.fast_gnp_random_graph(nodes, prob, seed=11)
        for edge in graph.edges():
                graph.edges[edge]['weight'] = randint(1,10)

        nodes = list(graph.nodes())
        num_pairs = randint(1, max(2,len(nodes)//3))
        source_terminal_pairs = []

        for _ in range(num_pairs):
            source = choice(nodes)
            terminal_candidates = [node for node in nodes if node != source]
            terminal = choice(terminal_candidates)
            source_terminal_pairs.append((source, terminal))

        problem_to_solve:MinimumMultiCutProblem = MinimumMultiCutProblem(graph, source_terminal_pairs)
        solution:MinimumMultiCutProblemBinaryBitArraySolution = MinimumMultiCutProblemBinaryBitArraySolution()
        finish:FinishControl = FinishControl(criteria='iterations', iterations_max=500)
        additional_statistics_control:AdditionalStatisticsControl = AdditionalStatisticsControl(is_active=False, keep='')
        vns_shaking_support:MinimumMultiCutProblemBinaryBitArraySolutionVnsShaking = \
                MinimumMultiCutProblemBinaryBitArraySolutionVnsShaking()
        vns_ls_support:MinimumMultiCutProblemBinaryBitArraySolutionVnsLocalSearchSupport = \
                MinimumMultiCutProblemBinaryBitArraySolutionVnsLocalSearchSupport()
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.output_control = output_control
        vns_construction_params.problem = problem_to_solve
        vns_construction_params.solution_template = solution
        vns_construction_params.finish_control = finish
        vns_construction_params.vns_shaking_support = vns_shaking_support
        vns_construction_params.vns_ls_support = vns_ls_support
        vns_construction_params.additional_statistics_control = additional_statistics_control
        vns_construction_params.random_seed = 43434343
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        vns_construction_params.local_search_type = 'localSearchBestImprovement'
        optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        optimizer.optimize()
        print('Best solution representation: {}'.format(optimizer.best_solution.representation.bin))            
        print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))            
        print('Best solution objective: {}'.format(optimizer.best_solution.objective_value))
        print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()