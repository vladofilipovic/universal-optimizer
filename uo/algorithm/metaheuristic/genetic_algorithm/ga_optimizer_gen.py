""" 
..  _py_ga_optimizer:

The :mod:`~uo.algorithm.metaheuristic.genetic_algorithm.genetic_algorithm` contains class :class:`~.uo.metaheuristic.genetic_algorithm.genetic_algorithm.GaOptimizerGenerational`, that represents implements algorithm :ref:`GA<Genetic_Algorithm>`.
"""

from pathlib import Path

directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy

from random import choice

from typing import Optional

from dataclasses import dataclass

from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.genetic_algorithm.ga_selection import GaSelection
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support import GaCrossoverSupport
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support import GaMutationSupport
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizer


@dataclass
class GaOptimizerGenerationalConstructionParameters:
        """
        Instance of the class :class:`~uo.algorithm.metaheuristic.genetic_algorithm_constructor_parameters.
        GaOptimizerConstructionParameters` represents constructor parameters for GA algorithm.
        """
        ga_crossover_support: GaCrossoverSupport = None
        ga_mutation_support: GaMutationSupport = None
        ga_selection: GaSelection = None
        population_size: Optional[int] = None
        elite_count:Optional[int] = None
        finish_control: Optional[FinishControl] = None
        problem: Problem = None
        solution_template: Optional[Solution] = None
        output_control: Optional[OutputControl] = None
        random_seed: Optional[int] = None
        additional_statistics_control: Optional[AdditionalStatisticsControl] = None



class GaOptimizerGenerational(GaOptimizer):
    """
    Instance of the class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational` encapsulate 
    :ref:`Genetic_Algorithm` optimization algorithm.
    """
    
    def __init__(self,
            ga_crossover_support:GaCrossoverSupport,
            ga_mutation_support:GaMutationSupport,
            ga_selection: GaSelection,
            population_size: int,
            elite_count:int,
            finish_control:FinishControl,
            problem:Problem,
            solution_template:Optional[Solution],
            output_control:OutputControl=None,
            random_seed:Optional[int]=None,
            additional_statistics_control:Optional[AdditionalStatisticsControl]=None
        )->None:
        """
        Create new instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational`. 
        That instance implements :ref:`GA<Genetic_Algorithm>` algorithm. 

        :param `GaCrossoverSupport` ga_crossover_support: placeholder for additional methods, specific for GA crossover 
        execution, which depend of precise solution type 
        :param `GaMutationSupport` ga_mutation_support: placeholder for additional methods, specific for GA mutation 
        execution, which depend of precise solution type 
        :param `GaSelection` ga_selection: structure that controls GA selection
        :param `int` population_size: size of the population
        :param `int` elite_count: Count of the elite individuals within population
        :param `FinishControl` finish_control: structure that control finish criteria for metaheuristic execution
        :param `Problem` problem: problem to be solved
        :param `Optional[Solution]` solution_template: initial solution of the problem
        :param `Optional[OutputControl]` output_control: structure that controls output
        :param Optional[int] random_seed: random seed for metaheuristic execution
        :param `Optional[AdditionalStatisticsControl]` additional_statistics_control: structure that controls additional
        statistics obtained during population-based metaheuristic execution
        """
        super().__init__( 
                finish_control=finish_control,
                random_seed=random_seed,
                additional_statistics_control=additional_statistics_control,
                output_control=output_control,
                problem=problem,
                solution_template=solution_template,
                ga_selection=ga_selection,
                ga_crossover_support=ga_crossover_support,
                ga_mutation_support=ga_mutation_support,
                population_size=population_size,
                elite_count=elite_count
        )

    @classmethod
    def from_construction_tuple(cls, construction_tuple:GaOptimizerGenerationalConstructionParameters):
        """
        Additional constructor, that creates new instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational`. 

        :param `GaOptimizerConstructionParameters` construction_tuple: tuple with all constructor parameters
        """
        return cls(
            construction_tuple.ga_crossover_support,
            construction_tuple.ga_mutation_support,
            construction_tuple.ga_selection,
            construction_tuple.population_size,
            construction_tuple.elite_count,
            construction_tuple.finish_control,
            construction_tuple.problem,
            construction_tuple.solution_template,
            construction_tuple.output_control,
            construction_tuple.random_seed,
            construction_tuple.additional_statistics_control
        )

    def __copy__(self):
        """
        Internal copy of the current instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational`        
        """
        ga_opt = deepcopy(self)
        return ga_opt

    def copy(self):
        """
        Copy the current instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational`        
        """
        return self.__copy__()

    def init(self)->None:
        """
        Initialization of the generational GA algorithm
        """
        super().init()

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
        indices_for_selection:list[int] = [sel_ind for sel_ind in range(l_lim, self.population_size)]
        while True:
            if len(indices_for_selection) == 0:
                break
            if len(indices_for_selection) == 1:
                sel_ind: int = indices_for_selection[0]
                new_population[sel_ind] = self.current_population[sel_ind]
                indices_for_selection.remove(sel_ind)
                break
            sel_ind1:int = choice(indices_for_selection)
            indices_for_selection.remove(sel_ind1)
            sel_ind2:int = choice(indices_for_selection)
            indices_for_selection.remove(sel_ind2)            
            self.ga_crossover_support.crossover(self.problem, self.current_population[sel_ind1], 
                            self.current_population[sel_ind2], 
                            new_population[sel_ind1], new_population[sel_ind2], self)
        self.write_output_values_if_needed("after_step_in_iteration", "crossover")
        self.write_output_values_if_needed("before_step_in_iteration", "mutation")
        for i in range(l_lim, len(self.current_population)):
            self.ga_mutation_support.mutation(self.problem, new_population[i], self)
        self.write_output_values_if_needed("after_step_in_iteration", "mutation")
        self.current_population = new_population
        self.best_solution = self.current_population[self.index_of_best_in_population()]
        self.update_additional_statistics_if_required(self.current_population)

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='',group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the `GaOptimizerGenerational` instance

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
        s += group_end
        return s

    def __str__(self)->str:
        """
        String representation of the `GaOptimizerGenerational` instance

        :return: string representation of the `GaOptimizerGenerational` instance
        :rtype: str
        """
        s = self.string_rep('|')
        return s

    def __repr__(self)->str:
        """
        String representation of the `GaOptimizerGenerational` instance

        :return: string representation of the `GaOptimizerGenerational` instance
        :rtype: str
        """
        s = self.string_rep('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the GaOptimizerGenerational instance

        :param spec: str -- format specification 
        :return: formatted `GaOptimizerGenerational` instance
        :rtype: str
        """
        return self.string_rep('\n',0,'   ','{', '}')
