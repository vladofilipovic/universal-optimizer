import sys
import networkx as nx
import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from opt.single_objective.comb.min_multi_cut_problem.min_multi_cut_problem import MinMultiCutProblem

class TestMinMultiCutProblem(unittest.TestCase):

    # Creating a new instance of MinMultiCutProblem with a specified graph and st pairs sets both properies correctly
    def test_new_instance_with_graph_and_st_pairs_sets_both_properties(self):
        # Arrange
        nodes = 10
        prob = 0.5
        G: nx.Graph = nx.fast_gnp_random_graph(nodes, prob)
        source_terminal_pairs = [(1,2),(3,4)]
    
        # Act
        problem = MinMultiCutProblem(G, source_terminal_pairs)
    
        # Assert
        self.assertEqual(problem.graph, G)
        self.assertEqual(problem.source_terminal_pairs, source_terminal_pairs)

    # The string representation of an instance of MinMultiCutProblem includes the source terminal pairs
    def test_string_representation_includes_st_pairs(self):
        # Arrange
        nodes = 10
        prob = 0.5
        G: nx.Graph = nx.fast_gnp_random_graph(nodes, prob)
        source_terminal_pairs = [(1,2),(3,4)]
        problem = MinMultiCutProblem(G, source_terminal_pairs)
    
        # Act
        string_rep = str(problem)
    
        # Assert
        self.assertIn('source_terminal_pairs=' + str(source_terminal_pairs), string_rep)

    # Copying an instance of MinMultiCutProblem creates a new instance with the same properties
    def test_copy_creates_new_instance_with_same_properties(self):
        # Arrange
        nodes = 10
        prob = 0.5
        G: nx.Graph = nx.fast_gnp_random_graph(nodes, prob)
        source_terminal_pairs = [(1,2),(3,4)]
        problem = MinMultiCutProblem(G, source_terminal_pairs)
    
        # Act
        copy_problem = problem.copy()
    
        # Assert
        self.assertIsNot(problem, copy_problem)
        self.assertEqual(problem.source_terminal_pairs, copy_problem.source_terminal_pairs)

    # The MinMultiCutProblem class can be instantiated without source terminal paramater
    def test_instantiation_without_st_parameter(self):
        # Arrange
        nodes = 10
        prob = 0.5
        G: nx.Graph = nx.fast_gnp_random_graph(nodes, prob)
        source_terminal_pairs = None

        # Act & Assert
        with self.assertRaises(TypeError):
            problem = MinMultiCutProblem(G, source_terminal_pairs)

    # The from_graph_and_source_terminal_pairs method of MinMultiCutProblem creates a new instance with the specified parameters
    def test_from_graph_and_st_pairs_creates_new_instance_with_specified_parameteres(self):
        # Arrange
        nodes = 10
        prob = 0.5
        G: nx.Graph = nx.fast_gnp_random_graph(nodes, prob)
        source_terminal_pairs = [(1,2),(3,4)]
    
        # Act
        problem = MinMultiCutProblem.from_graph_and_source_terminal_pairs(G, source_terminal_pairs)
    
        # Assert
        self.assertEqual(problem.source_terminal_pairs, source_terminal_pairs)
        self.assertTrue(problem.graph.__eq__(G))


if __name__ == '__main__':
    unittest.main()