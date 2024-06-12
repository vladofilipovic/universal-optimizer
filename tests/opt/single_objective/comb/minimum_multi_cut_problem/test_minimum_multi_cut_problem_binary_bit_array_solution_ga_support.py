
import unittest
import unittest.mock as mocker
import networkx as nx

from bitstring import BitArray
from random import randint, choice

from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem import MinimumMultiCutProblem
from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution import MinimumMultiCutProblemBinaryBitArraySolution
from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution_ga_support import MinimumMultiCutProblemBinaryBitArraySolutionGaSupport


class TestMinimumMultiCutProblemBinaryBitArraySolutionGaSupport(unittest.TestCase):

    # mutation method returns True when mutation is successful
    def test_mutation_returns_true_when_randomization_is_successful(self):
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

        problem = MinimumMultiCutProblem(graph=graph, source_terminal_pairs=source_terminal_pairs)
        solution = MinimumMultiCutProblemBinaryBitArraySolution(random_seed=434343)
        solution.init_from( BitArray(length=edges), problem)
        ga_support = MinimumMultiCutProblemBinaryBitArraySolutionGaSupport()
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub)
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).ga_support = mocker.PropertyMock(return_value=ga_support)
        # Act
        result = ga_support.mutation(0.1, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)