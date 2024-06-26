"""
The :mod:`~uo.algorithm.metaheuristic.genetic_algorithm.problem_solution_ga_support` module describes the class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.problem_solution_ga_support.ProblemSolutionGaSupport`.
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

from uo.problem.problem import Problem
from uo.solution.solution import Solution
from uo.algorithm.algorithm import Algorithm

R_co = TypeVar("R_co", covariant=True)
A_co = TypeVar("A_co", covariant=True)

class GaMutationSupport(Generic[R_co,A_co], metaclass=ABCMeta):
    
    @abstractmethod
    def mutation(self, mutation_probability:float, problem:Problem, solution:Solution[R_co,A_co], optimizer:Algorithm)->bool:
        """
        GA individual mutation based on some probability

        :param float mutation_probability: float parameter for mutation probability
        :param `Problem` problem: problem that is solved
        :param `Solution[R_co,A_co]` solution: individual that should be mutated
        :param `Algorithm` optimizer: optimizer that is executed
        :return: if mutation is successful
        :rtype: bool
        """
        raise NotImplementedError
    