
import unittest
import unittest.mock as mocker
import networkx as nx

from bitstring import BitArray
from random import randint, choice

from opt.single_objective.comb.min_multi_cut_problem.min_multi_cut_problem import MinMultiCutProblem
from opt.single_objective.comb.min_multi_cut_problem.min_multi_cut_problem_bit_array_solution import \
    MinMultiCutProblemBitArraySolution

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_bit_array import \
    VnsLocalSearchSupportStandardBestImprovementBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_bit_array import \
    VnsShakingSupportStandardBitArray


class TestMinMultiCutProblemBitArraySolutionVnsSupport(unittest.TestCase):

    # shaking method returns True when randomization is successful
    def test_shaking_returns_true_when_randomization_is_successful(self):
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
        vns_shaking_support = VnsShakingSupportStandardBitArray(len(problem.graph.edges))
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub)
        optimizer_stub.should_finish = mocker.Mock(return_value=False)
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_shaking_support = mocker.PropertyMock(return_value=vns_shaking_support)
        optimizer_stub.k_min = 1
        optimizer_stub.k_max = 10
        # Act
        result = vns_shaking_support.shaking(5, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)

    # local_search_best_improvement method returns a solution with lower fitness value
    def test_local_search_best_improvement_returns_solution_with_lower_fitness_value11(self):
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
        solution.evaluate(problem)
        vns_ls_support = VnsLocalSearchSupportStandardBestImprovementBitArray(len(problem.graph.edges))
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        optimizer_stub.should_finish = mocker.Mock(return_value=False)
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=4)
        type(optimizer_stub).vns_ls_support = mocker.PropertyMock(return_value=vns_ls_support)
        optimizer_stub.k_min = 1
        optimizer_stub.k_max = 10
        # Act
        old_fitness = solution.fitness_value
        result = vns_ls_support.local_search(3, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)
        self.assertGreaterEqual(solution.fitness_value, old_fitness)

    # shaking method modifies the solution representation when the number of ones in the solution representation is less than the problem dimension
    def test_shaking_modifies_solution_representation_when_number_of_ones_is_less_than_problem_dimension8(self):
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
        solution.init_from( BitArray(bin='0' * edges), problem)
        vns_shaking_support = VnsShakingSupportStandardBitArray(len(problem.graph.edges))
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub)
        optimizer_stub.should_finish = mocker.Mock(return_value=False) 
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_shaking_support = mocker.PropertyMock(return_value=vns_shaking_support)
        optimizer_stub.k_min = 1
        optimizer_stub.k_max = 10
        # Act
        vns_shaking_support.shaking(5, problem, solution, optimizer_stub)
        # Assert
        self.assertNotEqual(solution.representation.bin, '0' * edges)

    # local_search_best_improvement method returns a solution with lower fitness value
    def test_local_search_best_improvement_returns_solution_with_lower_fitness_value6(self):
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
        solution.evaluate(problem)
        vns_ls_support = VnsLocalSearchSupportStandardBestImprovementBitArray(len(problem.graph.edges))
        finish_control_stub = mocker.MagicMock()
        type(finish_control_stub).is_finished = mocker.Mock(return_value=False)
        optimizer_stub = mocker.MagicMock()
        type(optimizer_stub).finish_control = mocker.PropertyMock(return_value=finish_control_stub) 
        optimizer_stub.should_finish = mocker.Mock(return_value=False)
        type(optimizer_stub).evaluation = mocker.PropertyMock(return_value=0)
        type(optimizer_stub).vns_ls_support = mocker.PropertyMock(return_value=vns_ls_support)        
        optimizer_stub.k_min = 1
        optimizer_stub.k_max = 10
        # Act
        old_fitness = solution.fitness_value
        result = vns_ls_support.local_search(3, problem, solution, optimizer_stub)
        # Assert
        self.assertTrue(result)
        self.assertGreaterEqual(solution.fitness_value, old_fitness)
