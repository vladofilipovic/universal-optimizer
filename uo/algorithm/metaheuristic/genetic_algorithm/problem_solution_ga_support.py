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

class ProblemSolutionGaSupport(Generic[R_co,A_co], metaclass=ABCMeta):
    
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

    @abstractmethod
    def crossover(self, crossover_probability:float, problem:Problem, 
                solution1:Solution[R_co,A_co], solution2:Solution[R_co,A_co], 
                child1:Solution[R_co,A_co], child2:Solution[R_co,A_co], optimizer:Algorithm):
        """
        GA crossover on two parents

        :param float crossover_probability: float parameter for crossover probability
        :param `Problem` problem: problem that is solved
        :param `Solution[R_co,A_co]` solution1: first parent
        :param `Solution[R_co,A_co]` solution2: second parent
        :param `Solution[R_co,A_co]` child1: first child that is created
        :param `Solution[R_co,A_co]` child2: second child that is created
        :param `Algorithm` optimizer: optimizer that is executed
        """
        raise NotImplementedError
    
    @abstractmethod
    def selection_tournament(self, problem:Problem, solution:list[Solution[R_co,A_co]], tournament_size:int, optimizer:Algorithm)->Solution[R_co,A_co]:
        """
        GA tournament selection

        :param `Problem` problem: problem that is solved
        :param `list[Solution[R_co,A_co]]` solution: list of individuals in a generation
        :param `int` tournament_size: size of the tournament
        :param `Algorithm` optimizer: optimizer that is executed
        :return: selected individual
        :rtype: Solution[R_co,A_co]
        """
        raise NotImplementedError
    
    @abstractmethod
    def selection_roulette(self, problem:Problem, solution:list[Solution[R_co,A_co]], optimizer:Algorithm)->Solution[R_co,A_co]:
        """
        GA roulette selection

        :param `Problem` problem: problem that is solved
        :param `list[Solution[R_co,A_co]]` solution: list of individuals in a generation
        :param `Algorithm` optimizer: optimizer that is executed
        :return: selected individual
        :rtype: Solution[R_co,A_co]
        """
        raise NotImplementedError
    
    @abstractmethod
    def selection_rang_roulette(self, problem:Problem, solution:list[Solution[R_co,A_co]], optimizer:Algorithm)->Solution[R_co,A_co]:
        """
        GA rang roulette selection

        :param `Problem` problem: problem that is solved
        :param `list[Solution[R_co,A_co]]` solution: list of individuals in a generation
        :param `Algorithm` optimizer: optimizer that is executed
        :return: selected individual
        :rtype: Solution[R_co,A_co]
        """
        raise NotImplementedError
