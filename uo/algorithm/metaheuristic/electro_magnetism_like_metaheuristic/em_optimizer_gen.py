""" 
..  _py_em_optimizer:

The :mod:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.electro_magnetism_like_metaheuristic` contains class :class:`~.uo.metaheuristic.electro_magnetism_like_metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational`, that represents implements algorithm :ref:`EM<Electro_magnetism_like_metaheuristic>`.
"""

from pathlib import Path

directory = Path(__file__).resolve()
import sys
import numpy as np
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy

from random import choice

from bitstring import BitArray

from typing import Optional

from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_attraction_support import EmAttractionSupport
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support import EmMutationSupport
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_direction_support import EmDirectionSupport
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_optimizer import EmOptimizer
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_optimizer import EmOptimizerConstructionParameters


class EmOptimizerGenerational(EmOptimizer):
    """
    Instance of the class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational` encapsulate 
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
            output_control:OutputControl=None,
            random_seed:Optional[int]=None,
            additional_statistics_control:Optional[AdditionalStatisticsControl]=None
        )->None:
        """
        Create new instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational`. 
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
        super().__init__( 
                finish_control=finish_control,
                random_seed=random_seed,
                additional_statistics_control=additional_statistics_control,
                output_control=output_control,
                problem=problem,
                solution_template=solution_template,
                em_attraction_support=em_attraction_support,
                em_mutation_support=em_mutation_support,
                em_direction_support=em_direction_support,
                population_size=population_size
        )

    @classmethod
    def from_construction_tuple(cls, construction_tuple:EmOptimizerConstructionParameters):
        """
        Additional constructor, that creates new instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational`. 

        :param `EmOptimizerConstructionParameters` construction_tuple: tuple with all constructor parameters
        """
        return cls(
            construction_tuple.em_attraction_support,
            construction_tuple.em_mutation_support,
            construction_tuple.em_direction_support,
            construction_tuple.population_size,
            construction_tuple.finish_control,
            construction_tuple.problem,
            construction_tuple.solution_template,
            construction_tuple.output_control,
            construction_tuple.random_seed,
            construction_tuple.additional_statistics_control
        )

    def __copy__(self):
        """
        Internal copy of the current instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational`        
        """
        em_opt = deepcopy(self)
        return em_opt

    def copy(self):
        """
        Copy the current instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational`

        :return: new instance of class :class:`~uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational` with the same properties
        :rtype: :class:`uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.EmOptimizerGenerational`        
        """
        return self.__copy__()

    def init(self)->None:
        """
        Initialization of the generational EM algorithm
        """
        super().init()

    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the EM algorithm
        """
        self.iteration += 1
        new_population:list[Solution] = [self.solution_template.copy() for _ in range(self.population_size)]
        self.write_output_values_if_needed("before_step_in_iteration", "charge_calculation")

        self.__charges = []
        # Calculate charges for the current population based on their objective values
        # POSTO JE PRVI KORAK ZA CHARGE 1/FITNESS, TREBA DA VIDIM KAKO DA DODJEM DO FITNESSA
        for individual in self.current_population:
            selected_subsets = [self.problem.subsets[i] for i in range(individual.representation.len) if individual.representation[i] == 1]
            covered_elements = set().union(*selected_subsets)
            uncovered_elements = self.problem.universe - covered_elements 
            num_selected_subsets = sum(individual.representation)
            self.__charges.append(1/(num_selected_subsets + 1e-6))
        self.write_output_values_if_needed("after_step_in_iteration", "charge_calculation")
    
        # Apply attraction and repulsion forces between solutions
        self.write_output_values_if_needed("before_step_in_iteration", "attraction_repulsion")
        for i in range(self.population_size):
            for j in range(self.population_size):
                if i != j:
                    # MOZDA I OVO BUDE TREBALO DA SE MENJA
                    attraction = self.em_attraction_support.attraction(self.problem, self.current_population[i], self.current_population[j], self.__charges[i], self.__charges[j], self)
                    direction = self.em_direction_support.direction(self.problem, self.current_population[i], self.current_population[j], self)
                    self.__charges[i] = attraction * direction
    
        self.write_output_values_if_needed("after_step_in_iteration", "attraction_repulsion")

        # Update positions of the solutions based on the calculated forces
        self.write_output_values_if_needed("before_step_in_iteration", "movement_update")
        for i in range(self.population_size):
            binary_representation = [int(bit) for bit in self.current_population[i].representation.bin]
            # Convert to a numpy array and perform the addition
            #new_particle = np.clip(np.array(binary_representation) + np.sign(self.__charges[i]), 0, 1).astype(int)
            new_particle = self.current_population[i]
            new_particle.representation = BitArray(self.current_population[i].representation.len)
            for j in range(self.current_population[i].representation.len):
                new_particle.representation.set(self.current_population[i].representation[j] + np.sign(self.__charges[i]), j)
            new_population[i] = new_particle

        self.write_output_values_if_needed("after_step_in_iteration", "movement_update")
        self.write_output_values_if_needed("before_step_in_iteration", "mutation")
        for i in range(len(self.current_population)):
            self.em_mutation_support.mutation(self.problem, new_population[i], self)
        self.write_output_values_if_needed("after_step_in_iteration", "mutation")
        self.current_population = new_population
        #self.best_solution = float('inf')
        self.curr_best = self.current_population[self.index_of_best_in_population()]
        if self.curr_best.fitness_value < self.best_solution.fitness_value:
            self.best_solution = self.curr_best
            self.update_additional_statistics_if_required(self.current_population)

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='',group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the `EmOptimizerGenerational` instance

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
        String representation of the `EmOptimizerGenerational` instance

        :return: string representation of the `EmOptimizerGenerational` instance
        :rtype: str
        """
        s = self.string_rep('|')
        return s

    def __repr__(self)->str:
        """
        String representation of the `EmOptimizerGenerational` instance

        :return: string representation of the `EmOptimizerGenerational` instance
        :rtype: str
        """
        s = self.string_rep('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the EmOptimizerGenerational instance

        :param spec: str -- format specification 
        :return: formatted `EmOptimizerGenerational` instance
        :rtype: str
        """
        return self.string_rep('\n',0,'   ','{', '}')