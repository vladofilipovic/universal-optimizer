""" 
..  _py_minimum_multi_cut_problem:

"""

import sys
from pathlib import Path
from typing import Optional
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy
import networkx as nx
import json

from uo.problem.problem import Problem
from uo.utils.logger import logger

class MinMultiCutProblem(Problem):
    """
    Class representing the Minimum Multi Cut Problem.

    This class inherits from the Problem class and is used to define and solve the Minimum Multi Cut Problem. The problem is defined by a graph and a list of source terminal pairs.

    Attributes:
        graph (nx.Graph): Graph.
        source_terminal_pairs (list[tuple[int,int]]): list of pairs that represent source and terminal nodes

    Methods:
        __init__(graph: nx.Graph, source_terminal_pairs: list): Initializes a new instance of the MinMultiCutProblem class.
        
        __load_from_files__(graph_file_path: str, source_terminal_pairs_file_path: str) -> tuple: Static function that reads problem data from files.
        from_input_files(graph_file_path: str, source_terminal_pairs_file_path: str): Creates a new MinMultiCutProblem instance when the input file and input format are specified.
        __copy__() -> MinMultiCutProblem: Internal copy of the MinMultiCutProblem problem.
        copy() -> MinMultiCutProblem: Copy the MinMultiCutProblem problem.
        graph() -> nx.Graph: Property getter for the graph of the target problem.
        source_terminal_pairs() -> list[tuple[int,int]]: Property getter for the source_terminal_pairs of the target problem.
        string_rep(delimiter: str, indentation: int = 0, indentation_symbol: str = '', group_start: str = '{', group_end: str = '}') -> str: String representation of the MinMultiCutProblem instance.
        __str__() -> str: String representation of the MinMultiCutProblem structure.
        __repr__() -> str: Representation of the MinMultiCutProblem instance.
        __format__() -> str: Formatted MinMultiCutProblem instance.
    """
    
    def __init__(self, graph:nx.Graph, source_terminal_pairs:list[tuple[int,int]])->None:
        """
        Create new `MinMultiCutProblem` instance

        :param nx.Graph graph: graph of the problem
        :param list[tuple[int,int]] source_terminal_pairs: source_terminal_pairs of the problem
        """
        if not isinstance(graph, nx.Graph):
            raise TypeError('Parameter \'graph\' for  MinMultiCutProblem should be \'nx.Graph\'.')
        if not isinstance(source_terminal_pairs, list):
            raise TypeError('Parameter \'source_terminal_pairs\' for  MinMultiCutProblem should be \'list\'.')
        super().__init__(name="MinMultiCutProblem", is_minimization=True, is_multi_objective=False)
        self.__graph = graph
        self.__source_terminal_pairs = source_terminal_pairs
        
    @classmethod
    def from_graph_and_source_terminal_pairs(cls, graph:nx.Graph, source_terminal_pairs:list):
        """
        Additional constructor. Create new `MinMultiCutProblem` instance when graph and source_terminal_pairs are specified

        :param nx.Graph graph: graph of the problem
        :param list[tuple[int,int]] source_terminal_pairs: source_terminal_pairs of the problem
        """
        return cls(graph, source_terminal_pairs)

    @classmethod
    def __load_from_files__(cls,graph_file_path: str, source_terminal_pairs_file_path: str)->tuple:
        """
        Static function that read problem data from file

        :param str graph_file_path: path of the file with problem graph
        :param str source_terminal_pairs_file_path: path of the file with problem source_terminal_pairs

        :return: all data that describe problem
        :rtype: tuple
        """
        logger.debug("Load parameters: graph file path=" + str(graph_file_path) + ",  source terminal pairs file path=" + str(source_terminal_pairs_file_path))
        graph = nx.read_gml(graph_file_path)
        with open(source_terminal_pairs_file_path, 'r') as file:
            source_terminal_pairs = json.load(file)

        return graph, source_terminal_pairs

    @classmethod
    def from_input_files(cls, graph_file_path: str, source_terminal_pairs_file_path: str)->'MinMultiCutProblem':
        """
        Additional constructor. Create new `MinMultiCutProblem` instance when input file and input format are specified

        :param str input_file_path: path of the input file with problem graph
        :param str source_terminal_pairs_file_path: path of the input file with problem source_terminal_pairs

        :return: class instance
        :rtype: MinMultiCutProblem
        """
        result:tuple = MinMultiCutProblem.__load_from_file__(graph_file_path, source_terminal_pairs_file_path)
        graph:nx.Graph = result[0]
        source_terminal_pairs:list[tuple[int,int]] = result[1]

        return cls(graph=graph,source_terminal_pairs=source_terminal_pairs)

    def __copy__(self)->'MinMultiCutProblem':
        """
        Internal copy of the `MinMultiCutProblem` problem

        :return: new `MinMultiCutProblem` instance with the same properties
        :rtype: `MinMultiCutProblem`
        """
        pr = deepcopy(self)
        return pr

    def copy(self)->'MinMultiCutProblem':
        """
        Copy the `MinMultiCutProblem` problem

        :return: new `MinMultiCutProblem` instance with the same properties
        :rtype: MinMultiCutProblem
        """
        return self.__copy__()

    @property
    def graph(self)->nx.Graph:
        """
        Property getter for graph of the target problem

        :return: graph of the target problem instance 
        :rtype: nx.Graph
        """
        return self.__graph
    
    @property
    def source_terminal_pairs(self)->list[tuple[int,int]]:
        """
        Property getter for source_terminal_pairs of the target problem

        :return: source_terminal_pairs of the target problem instance 
        :rtype: list
        """
        return self.__source_terminal_pairs

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the `MinMultiCutProblem` instance

        :param delimiter: delimiter between fields
        :type delimiter: str
        :param indentation: level of indentation
        :type indentation: int, optional, default value 0
        :param indentation_symbol: indentation symbol
        :type indentation_symbol: str, optional, default value ''
        :param group_start: group start string 
        :type group_start: str, optional, default value '{'
        :param group_end: group end string 
        :type group_end: str, optional, default value '}'
        :return: string representation of instance that controls output
        :rtype: str
        """          
        s = delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s+= super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s+= delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'graph=' + str(self.__graph) + delimiter
        s += 'source_terminal_pairs=' + str(self.__source_terminal_pairs) + delimiter
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the minimum multi cut problem structure

        :return: string representation of the minimum multi cut problem structure
        :rtype: str
        """
        return self.string_rep('|', 0, '', '{', '}')


    def __repr__(self)->str:
        """
        Representation of the minimum multi cut problem instance
        :return: str -- string representation of the minimum multi cut problem instance
        """
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self)->str:
        """
        Formatted the minimum multi cut problem instance
        :return: str -- formatted minimum multi cut problem instance
        """
        return self.string_rep('|')


