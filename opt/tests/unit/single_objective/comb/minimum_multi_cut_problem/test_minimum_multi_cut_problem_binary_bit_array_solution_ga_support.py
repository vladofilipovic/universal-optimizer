
import unittest
import unittest.mock as mocker
import networkx as nx

from bitstring import BitArray
from random import randint, choice

from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support_one_point_bit_array import \
    GaCrossoverSupportOnePointBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support_one_point_bit_array import \
    GaMutationSupportOnePointBitArray

from opt.single_objective.comb.min_multi_cut_problem.min_multi_cut_problem import MinMultiCutProblem
from opt.single_objective.comb.min_multi_cut_problem.min_multi_cut_problem_bit_array_solution import \
    MinMultiCutProblemBitArraySolution


class TestMinMultiCutProblemBitArraySolutionGaSupport(unittest.TestCase):

    # mutation method returns True when mutation is successful
    def test_mutation_returns_none(self):
        # Arrange
        nodes = 10
        prob = 0.5
        graph: nx.Graph = nx.fast_gnp_random_graph(nodes, prob)
        for edge in graph.edges():
                graph.edges[edge]['weight'] = randint(1,10)
        nodes = list(graph.nodes())
        num_pairs = randint(1, max(2,len(nodes)//3))
        source_terminal_pairs = []
        edges = len(graph.edges())
        for _ in range(num_pairs):
            source = choice(nodes)
            terminal_candidates = [node for node in nodes if node != source]
            terminal = choice(terminal_candidates)
            source_terminal_pairs.append((source, terminal))

        problem = MinMultiCutProblem(graph=graph, source_terminal_pairs=source_terminal_pairs)
        solution = MinMultiCutProblemBitArraySolution(random_seed=434343)
        solution.init_from( BitArray(length=edges), problem)
        ga_cross_support = GaCrossoverSupportOnePointBitArray(0.995)
        ga_mut_support = GaMutationSupportOnePointBitArray(0.005)
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub)
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).ga_support_crossover = mocker.PropertyMock(return_value=ga_cross_support)
        # Act
        result = ga_mut_support.mutation(problem, solution, optimizer_stub)
        # Assert
        self.assertIsNone(result)