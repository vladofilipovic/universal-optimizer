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

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution

class ProblemSolutionVnsSupport(metaclass=ABCMeta):
    
    @abstractmethod
    def randomize(self, k:int, problem:TargetProblem, solution:TargetSolution, solution_codes:list[str])->bool:
        """
        Random VNS shaking of several parts such that new solution code does not differ more than supplied from all 
        solution codes inside collection

        :param int k: int parameter for VNS
        :param `TargetProblem` problem: problem that is solved
        :param `TargetSolution` solution: solution used for the problem that is solved
        :param `list[str]` solution_codes: solution codes that should be randomized
        :return: if randomization is successful
        :rtype: bool
        """        
        raise NotImplementedError

    @abstractmethod
    def local_search_best_improvement(self, k:int, problem:TargetProblem, solution:TargetSolution)->TargetSolution:
        """
        Executes best improvement variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `TargetProblem` problem: problem that is solved
        :param `TargetSolution` solution: solution used for the problem that is solved
        :return: result of the local search procedure 
        :rtype: TargetSolution
        """
        raise NotImplementedError

    @abstractmethod
    def local_search_first_improvement(self, k:int, problem:TargetProblem, solution:TargetSolution)->TargetSolution:
        """
        Executes best improvement variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `TargetProblem` problem: problem that is solved
        :param `TargetSolution` solution: solution used for the problem that is solved
        :return: result of the local search procedure 
        :rtype: TargetSolution
        """
        raise NotImplementedError
