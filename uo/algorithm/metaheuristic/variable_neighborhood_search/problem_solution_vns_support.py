""" 
The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support` module describes the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support.ProblemSolutionVnsSupport`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from abc import ABCMeta, abstractmethod
from typing import TypeVar
from typing import Generic

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.algorithm import Algorithm

R_co = TypeVar("R_co", covariant=True) 
A_co = TypeVar("A_co", covariant=True)

class ProblemSolutionVnsSupport(Generic[R_co,A_co], metaclass=ABCMeta):
    
    @abstractmethod
    def shaking(self, k:int, problem:TargetProblem, solution:TargetSolution[R_co,A_co], optimizer:Algorithm)->bool:
        """
        Random VNS shaking of several parts such that new solution code does not differ more than supplied from all 
        solution codes inside collection

        :param int k: int parameter for VNS
        :param `TargetProblem` problem: problem that is solved
        :param `TargetSolution[R_co,A_co]` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :param `list[R_co]` solution_representations: solution representations that should be shaken
        :return: if shaking is successful
        :rtype: bool
        """        
        raise NotImplementedError

    @abstractmethod
    def local_search_best_improvement(self, k:int, problem:TargetProblem, solution:TargetSolution[R_co,A_co], 
            optimizer:Algorithm)->bool:
        """
        Executes "best improvement" variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `TargetProblem` problem: problem that is solved
        :param `TargetSolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: result of the local search procedure 
        :rtype: if local search is successful
        """
        raise NotImplementedError

    @abstractmethod
    def local_search_first_improvement(self, k:int, problem:TargetProblem, solution:TargetSolution[R_co,A_co], 
            optimizer:Algorithm)->bool:
        """
        Executes "first improvement" variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `TargetProblem` problem: problem that is solved
        :param `TargetSolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: result of the local search procedure 
        :rtype: if local search is successful
        """
        raise NotImplementedError
