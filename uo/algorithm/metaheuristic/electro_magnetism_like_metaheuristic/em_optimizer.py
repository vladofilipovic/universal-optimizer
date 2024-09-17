""" 
..  _py_em_optimizer:

The :mod:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.electro_magnetism_like_metaheuristic` contains class :class:`~.uo.metaheuristic.electro_magnetism_like_metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizer`, that represents implements algorithm :ref:`EM<Electro_magnetism_like_metaheuristic>`.
"""

from pathlib import Path

directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy

from random import choice

from abc import ABCMeta, abstractmethod
from typing import Optional

from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.population_based_metaheuristic import PopulationBasedMetaheuristic
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_attraction_support import EmAttractionSupport
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support import EmMutationSupport
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_direction_support import EmDirectionSupport

class EmOptimizer(PopulationBasedMetaheuristic, metaclass=ABCMeta):
    """
    Instance of the class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizer` encapsulate 
    :ref:`Electro_magnetism_like_metaheuristic` optimization algorithm.
    """
    
    def __init__(self,
            em_attraction_support:EmAttractionSupport,
            em_mutation_support:EmMutationSupport,
            em_direction_support:EmDirectionSupport,
            population_size: int,
            finish_control:FinishControl,
            problem:Problem,
            solution_template:Optional[Solution],
            output_control:Optional[OutputControl],
            random_seed:Optional[int],
            additional_statistics_control:AdditionalStatisticsControl
        )->None:
        """
        Create new instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizer`. 
        That instance implements :ref:`EM<Electro_magnetism_like_metaheuristic>` algorithm. 

        :param `EmAttractionSupport` em_attraction_support: placeholder for additional methods, specific for EM attraction 
        execution, which depend of precise solution type 
        :param `EmMutationSupport` em_mutation_support: placeholder for additional methods, specific for EM mutation 
        execution, which depend of precise solution type 
        :param `EmDirectionSupport` em_direction_support: calculates direction of a particle
        :param `int` population_size: size of the population
        :param `FinishControl` finish_control: structure that control finish criteria for metaheuristic execution
        :param `Problem` problem: problem to be solved
        :param `Optional[Solution]` solution_template: initial solution of the problem
        :param `Optional[OutputControl]` output_control: structure that controls output
        :param Optional[int] random_seed: random seed for metaheuristic execution
        :param `Optional[AdditionalStatisticsControl]` additional_statistics_control: structure that controls additional
        statistics obtained during population-based metaheuristic execution
        """
        if not isinstance(em_attraction_support, EmAttractionSupport):
                raise TypeError('Parameter \'em_attraction_support\' must be \'EmAttractionSupport\'.')
        if not isinstance(em_mutation_support, EmMutationSupport):
                raise TypeError('Parameter \'em_mutation_support\' must be \'EmMutationSupport\'.')
        if not isinstance(em_direction_support, EmDirectionSupport):
                #print(type(em_direction_support))
                raise TypeError('Parameter \'em_direction_support\' must be \'EmDirectionSupport\'.')
        if not isinstance(population_size, int):
                raise TypeError('Parameter \'population_size\' must be \'int\'.')
        if population_size <= 0:
                raise ValueError('Parameter \'population_size\' must be positive.')
        super().__init__( 
                finish_control=finish_control,
                problem=problem,
                solution_template=solution_template,                
                name='em',
                output_control=output_control,
                random_seed=random_seed,
                additional_statistics_control=additional_statistics_control)
        self.__em_attraction_support:EmAttractionSupport = em_attraction_support
        self.__em_mutation_support:EmMutationSupport = em_mutation_support
        self.__em_direction_support:EmDirectionSupport = em_direction_support
        self.__population_size:int = population_size
        self.__current_population = [self.solution_template.copy() for _ in range(self.population_size)]
    def __copy__(self):
        """
        Internal copy of the current instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizer`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizer` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizer`        
        """
        em_opt = deepcopy(self)
        return em_opt

    def copy(self):
        """
        Copy the current instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizer`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizer` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizer`        
        """
        return self.__copy__()

    @property
    def population_size(self)->int:
        """
        Property getter for the `population_size` of the EM

        :return: `population_size` of the EM
        :rtype: int
        """
        return self.__population_size

    @property
    def current_population(self)->list[Solution]:
        """
        Property getter for the `current_population` of the EM

        :return: `current_population` of the EM
        :rtype: list[Solution]
        """
        return self.__current_population
    
    @current_population.setter
    def current_population(self, value:list[Solution])->None:
        """
        Property setter for the finish criteria property
        """
        if not isinstance(value, list):
            raise TypeError('Parameter \'current_population\' must have type \'list\'.')
        self.__population_size = len(value)
        self.__current_population = value
        

    @property
    def em_attraction_support(self)->EmAttractionSupport:
        """
        Property getter for the attraction support of EM
        
        :return: Attraction support of the EM 
        :rtype: `EmAttractionSupport`
        """
        return self.__em_attraction_support

    @property
    def em_mutation_support(self)->EmMutationSupport:
        """
        Property getter for the mutation support of EM
        
        :return: Mutation support of the EM 
        :rtype: `EmMutationSupport`
        """
        return self.__em_mutation_support

    @property
    def em_direction_support(self)->EmDirectionSupport:
        """
        Property getter for the direction support of EM
        
        :return: Direction support of the EM 
        :rtype: `EmDirectionSupport`
        """
        return self.__em_direction_support
    
    def index_of_best_in_population(self):
        pos:int = 0

        for i in range(1, self.population_size):
            if self.__current_population[i].fitness_value < self.__current_population[pos].fitness_value:
                pos = i
        print("Pos:", pos)
        return pos

    def init(self)->None:
        """
        Initialization of the EM algorithm
        """
        for i in range(self.population_size):
            self.__current_population[i].init_random(self.problem)
            self.evaluation = 1
            self.__current_population[i].evaluate(self.problem)
        print(self.__current_population)
        self.best_solution = min(self.__current_population, key=lambda individual: individual.fitness_value)

    @abstractmethod
    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the EM algorithm
        """
        raise NotImplementedError
    
    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='',group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the `EmOptimizer` instance

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
        s = super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += 'current_population: ' + group_start
        if self.__current_population is not None:
            for individual in self.__current_population:
                s += individual.string_rep(delimiter, indentation + 1, 
                    indentation_symbol, group_start, group_end) + delimiter
            s += group_end
        else:
            s += 'current_population=None' + delimiter
        s += 'population_size=' + str(self.population_size) + delimiter
        s += '__em_attraction_support=' + self.__em_attraction_support.string_rep(delimiter, 
                indentation + 1, indentation_symbol, group_start, group_end) + delimiter 
        for _ in range(0, indentation):
            s += indentation_symbol
        s += '__em_mutation_support=' + self.__em_mutation_support.string_rep(delimiter, 
                indentation + 1, indentation_symbol, group_start, group_end) + delimiter 
        s += '__em_direction_support=' + self.__em_direction_support.string_rep(delimiter, 
                indentation + 1, indentation_symbol, group_start, group_end) + delimiter 
        for _ in range(0, indentation):
            s += indentation_symbol
        for _ in range(0, indentation):
            s += indentation_symbol
        s += group_end
        return s

    def __str__(self)->str:
        """
        String representation of the `EmOptimizer` instance

        :return: string representation of the `EmOptimizer` instance
        :rtype: str
        """
        s = self.string_rep('|')
        return s

    def __repr__(self)->str:
        """
        String representation of the `EmOptimizer` instance

        :return: string representation of the `EmOptimizer` instance
        :rtype: str
        """
        s = self.string_rep('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the EmOptimizer instance

        :param spec: str -- format specification 
        :return: formatted `EmOptimizer` instance
        :rtype: str
        """
        return self.string_rep('\n',0,'   ','{', '}')
