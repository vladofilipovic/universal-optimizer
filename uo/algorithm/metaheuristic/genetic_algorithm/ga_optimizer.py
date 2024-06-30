""" 
..  _py_ga_optimizer:

The :mod:`~uo.algorithm.metaheuristic.genetic_algorithm.genetic_algorithm` contains class :class:`~.uo.metaheuristic.genetic_algorithm.genetic_algorithm.GaOptimizer`, that represents implements algorithm :ref:`GA<Genetic_Algorithm>`.
"""

from pathlib import Path

directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy

from typing import Optional

from dataclasses import dataclass

from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.population_based_metaheuristic import PopulationBasedMetaheuristic
from uo.algorithm.metaheuristic.genetic_algorithm.selection import Selection
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support import GaCrossoverSupport
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support import GaMutationSupport

@dataclass
class GaOptimizerConstructionParameters:
        """
        Instance of the class :class:`~uo.algorithm.metaheuristic.genetic_algorithm_constructor_parameters.
        GaOptimizerConstructionParameters` represents constructor parameters for GA algorithm.
        """
        finish_control: FinishControl = None
        random_seed: Optional[int] = None
        additional_statistics_control: AdditionalStatisticsControl = None
        output_control: OutputControl = None
        problem: Problem = None
        solution_template: Solution = None
        ga_selection: Selection = None
        ga_crossover_support: GaCrossoverSupport = None
        ga_mutation_support: GaMutationSupport = None
        population_size: int = None
        elite_count:Optional[int] = None

class GaOptimizer(PopulationBasedMetaheuristic):
    """
    Instance of the class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer` encapsulate 
    :ref:`Genetic_Algorithm` optimization algorithm.
    """
    
    def __init__(self,
            finish_control:FinishControl,
            random_seed:Optional[int],
            additional_statistics_control:AdditionalStatisticsControl,
            output_control:OutputControl,
            problem:Problem,
            solution_template:Solution,
            ga_selection: Selection,
            ga_crossover_support:GaCrossoverSupport,
            ga_mutation_support:GaMutationSupport,
            population_size: int,
            elite_count:Optional[int]
        )->None:
        """
        Create new instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer`. 
        That instance implements :ref:`GA<Genetic_Algorithm>` algorithm. 

        :param `FinishControl` finish_control: structure that control finish criteria for metaheuristic execution
        :param int random_seed: random seed for metaheuristic execution
        :param `AdditionalStatisticsControl` additional_statistics_control: structure that controls additional
        statistics obtained during population-based metaheuristic execution
        :param `OutputControl` output_control: structure that controls output
        :param `Problem` problem: problem to be solved
        :param `Solution` solution_template: initial solution of the problem
        :param `GaCrossoverSupport` ga_crossover_support: placeholder for additional methods, specific for GA crossover 
        execution, which depend of precise solution type 
        :param `GaMutationSupport` ga_mutation_support: placeholder for additional methods, specific for GA mutation 
        execution, which depend of precise solution type 
        :param `float` mutation_probability: probability of mutation
        :param `int` population_size: size of the population
        """
        if not isinstance(finish_control, FinishControl):
                raise TypeError('Parameter \'finish_control\' must be \'FinishControl\'.')
        if not isinstance(random_seed, Optional[int]):
                raise TypeError('Parameter \'random_seed\' must be \'int\' or \'None\'.')
        if not isinstance(additional_statistics_control, AdditionalStatisticsControl):
                raise TypeError('Parameter \'additional_statistics_control\' must be \'AdditionalStatisticsControl\'.')
        if not isinstance(output_control, OutputControl):
                raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
        if not isinstance(problem, Problem):
                raise TypeError('Parameter \'problem\' must be \'Problem\'.')
        if not isinstance(ga_selection, Selection):
                raise TypeError('Parameter \'ga_selection\' must be \'Selection\'.')
        if not isinstance(ga_crossover_support, GaCrossoverSupport):
                raise TypeError('Parameter \'ga_crossover_support\' must be \'GaCrossoverSupport\'.')
        if not isinstance(ga_mutation_support, GaMutationSupport):
                raise TypeError('Parameter \'ga_mutation_support\' must be \'GaMutationSupport\'.')
        if not isinstance(population_size, int):
                raise TypeError('Parameter \'population_size\' must be \'int\'.')
        if population_size < 0:
                raise ValueError('Parameter \'population_size\' must be positive.')
        super().__init__( name='ga',
                finish_control=finish_control,
                random_seed=random_seed,
                additional_statistics_control=additional_statistics_control,
                output_control=output_control,
                problem=problem,
                solution_template=solution_template)
        self.__ga_selection = ga_selection 
        self.__ga_crossover_support:GaCrossoverSupport = ga_crossover_support
        self.__crossover_method = self.__ga_crossover_support.crossover
        self.__ga_mutation_support:GaMutationSupport = ga_mutation_support
        self.__mutation_method = self.__ga_mutation_support.mutation
        self.__population_size:int = population_size
        self.__elite_count:Optional[int] = elite_count

    @classmethod
    def from_construction_tuple(cls, construction_tuple:GaOptimizerConstructionParameters):
        """
        Additional constructor, that creates new instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer`. 

        :param `GaOptimizerConstructionParameters` construction_tuple: tuple with all constructor parameters
        """
        return cls(
            construction_tuple.finish_control,
            construction_tuple.random_seed,
            construction_tuple.additional_statistics_control,
            construction_tuple.output_control,
            construction_tuple.problem,
            construction_tuple.solution_template,
            construction_tuple.ga_selection,
            construction_tuple.ga_crossover_support,
            construction_tuple.ga_mutation_support,
            construction_tuple.population_size,
            construction_tuple.elite_count)

    def __copy__(self):
        """
        Internal copy of the current instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer`        
        """
        ga_opt = deepcopy(self)
        return ga_opt

    def copy(self):
        """
        Copy the current instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer`        
        """
        return self.__copy__()

    @property
    def elite_count(self)->Optional[int]:
        """
        Property getter for elitist count 
        
        :return: count of elite number
        :rtype: Optional[int]
        """
        return self.__elite_count

    @elite_count.setter
    def elite_count(self, value:Optional[int])->None:
        """
        Property setter for elitist count 
        """
        self.__elite_count = value

    @property
    def population_size(self)->int:
        """
        Property getter for the `population_size` of the GA

        :return: `population_size` of the GA
        :rtype: int
        """
        return self.__population_size

    @property
    def current_population(self)->list[Solution]:
        """
        Property getter for the `current_population` of the GA

        :return: `current_population` of the GA
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
        self.__current_population = value
        
    @property
    def ga_selection(self)->Selection:
        """
        Property getter for the ga_selection of GA
        
        :return: Selection of the GA 
        :rtype: `Selection`
        """
        return self.__ga_selection

    def init(self)->None:
        """
        Initialization of the GA algorithm
        """
        self.current_population = [self.solution_template.copy() for _ in range(self.population_size)]
        for i in range(self.population_size):
            self.current_population[i].init_random(self.problem)
            self.evaluation = 1
            self.current_population[i].evaluate(self.problem)
        self.best_solution = max(self.__current_population, key=lambda individual: individual.fitness_value)
        if self.elite_count is None:
            return
        if not isinstance(self.elite_count, int): 
            return
        if self.elite_count > 0:
            for i in range(self.elite_count):
                sub_range:list[Solution] = self.current_population[i:self.population_size]
                max_sub_range:Solution = max(sub_range, key=lambda individual: individual.fitness_value)
                for j, v in enumerate(sub_range):
                    if v == max_sub_range:
                        temp:Solution = self.current_population[i]
                        self.current_population[i] = self.current_population[j]
                        self.current_population[j] = temp

    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the GA algorithm
        """
        self.iteration += 1
        self.write_output_values_if_needed("before_step_in_iteration", "selection")
        self.ga_selection.selection(self)
        self.write_output_values_if_needed("after_step_in_iteration", "selection")
        n_e:Optional[int] = self.elite_count
        if n_e is None or not isinstance(n_e, int):
            l_lim:int = 0
        else:
            l_lim:int = n_e
        self.write_output_values_if_needed("before_step_in_iteration", "crossover")
        new_population:list[Solution] = [self.solution_template.copy() for _ in range(self.population_size)]
        for i in range(l_lim):
            new_population[i] = self.current_population[i]
        for i in range(l_lim,len(self.current_population), 2):
            if i+1 == len(self.current_population):
                break
            parent1:Solution = self.current_population[i]
            parent2:Solution = self.current_population[i+1]
            self.__crossover_method(self.problem, parent1, parent2, new_population[i], new_population[i+1], self)
        self.write_output_values_if_needed("after_step_in_iteration", "crossover")
        self.write_output_values_if_needed("before_step_in_iteration", "mutation")
        for i in range(l_lim, len(self.current_population)):
            self.__mutation_method(self.problem, new_population[i], self)
        self.write_output_values_if_needed("after_step_in_iteration", "mutation")
        self.current_population = new_population
        pos:int = 0
        for i in range(1, self.population_size):
            if self.current_population[i].is_better(self.current_population[pos], self.problem):
                pos = i
        self.best_solution = self.current_population[pos]
        self.update_additional_statistics_if_required(self.current_population)

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='',group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the `GaOptimizer` instance

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
        s += '__ga_crossover_support=' + self.__ga_crossover_support.string_rep(delimiter, 
                indentation + 1, indentation_symbol, group_start, group_end) + delimiter 
        for _ in range(0, indentation):
            s += indentation_symbol
        s += '__ga_mutation_support=' + self.__ga_mutation_support.string_rep(delimiter, 
                indentation + 1, indentation_symbol, group_start, group_end) + delimiter 
        for _ in range(0, indentation):
            s += indentation_symbol
        s += 'elite_count=' + str(self.__elite_count) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol
        s += group_end
        return s

    def __str__(self)->str:
        """
        String representation of the `GaOptimizer` instance

        :return: string representation of the `GaOptimizer` instance
        :rtype: str
        """
        s = self.string_rep('|')
        return s

    def __repr__(self)->str:
        """
        String representation of the `GaOptimizer` instance

        :return: string representation of the `GaOptimizer` instance
        :rtype: str
        """
        s = self.string_rep('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the GaOptimizer instance

        :param spec: str -- format specification 
        :return: formatted `GaOptimizer` instance
        :rtype: str
        """
        return self.string_rep('\n',0,'   ','{', '}')
