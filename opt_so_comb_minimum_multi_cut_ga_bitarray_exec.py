from random import randint
from random import choice
from random import randint
import networkx as nx

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizer
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizerConstructionParameters

from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution_ga_support import MinimumMultiCutProblemBinaryBitArraySolutionGaSupport

from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem import MinimumMultiCutProblem
from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution import MinimumMultiCutProblemBinaryBitArraySolution

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)

        nodes = 10
        prob = 0.5

        G: nx.Graph = nx.fast_gnp_random_graph(nodes, prob)
        for edge in G.edges():
                G.edges[edge]['weight'] = randint(1,10)

        nodes = list(G.nodes())
        num_pairs = randint(1, max(2,len(nodes)//3))
        source_terminal_pairs = []

        for _ in range(num_pairs):
            source = choice(nodes)
            terminal_candidates = [node for node in nodes if node != source]
            terminal = choice(terminal_candidates)
            source_terminal_pairs.append((source, terminal))

        problem_to_solve:MinimumMultiCutProblem = MinimumMultiCutProblem(G, source_terminal_pairs)
        solution:MinimumMultiCutProblemBinaryBitArraySolution = MinimumMultiCutProblemBinaryBitArraySolution()
        finish:FinishControl = FinishControl(criteria='iterations', iterations_max=500)
        additional_statistics_control:AdditionalStatisticsControl = AdditionalStatisticsControl(is_active=False, keep='')

        ga_support:MinimumMultiCutProblemBinaryBitArraySolutionGaSupport = MinimumMultiCutProblemBinaryBitArraySolutionGaSupport()
        ga_construction_params:GaOptimizerConstructionParameters = GaOptimizerConstructionParameters()
        ga_construction_params.output_control = output_control
        ga_construction_params.problem = problem_to_solve
        ga_construction_params.solution_template = solution
        ga_construction_params.finish_control = finish
        ga_construction_params.problem_solution_ga_support = ga_support
        ga_construction_params.additional_statistics_control = additional_statistics_control
        ga_construction_params.random_seed = 43434343
        ga_construction_params.selection_type = 'selectionRoulette'
        ga_construction_params.problem = problem_to_solve
        ga_construction_params.mutation_probability = 0.1
        ga_construction_params.population_size = 100
        ga_construction_params.elitism_size = 10
        optimizer:GaOptimizer = GaOptimizer.from_construction_tuple(ga_construction_params)
        optimizer.optimize()

        print('Best solution representation: {}'.format(optimizer.best_solution.representation.bin))
        print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))
        print('Best solution objective: {}'.format(optimizer.best_solution.objective_value))
        print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))
        print('Number of evaluations: {}'.format(optimizer.evaluation))

if __name__ == '__main__':
        main()