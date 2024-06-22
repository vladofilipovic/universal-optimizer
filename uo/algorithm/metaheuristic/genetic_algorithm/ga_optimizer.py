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
from uo.algorithm.metaheuristic.genetic_algorithm.problem_solution_ga_support import ProblemSolutionGaSupport

@dataclass
class GaOptimizerConstructionParameters:
        """
        Instance of the class :class:`~uo.algorithm.metaheuristic.genetic_algorithm_constructor_parameters.
        GaOptimizerConstructionParameters` represents constructor parameters for GA algorithm.
        """
        finish_control: FinishControl = None
        output_control: OutputControl = None
        problem: Problem = None
        solution_template: list[Solution] = None
        problem_solution_ga_support: ProblemSolutionGaSupport = None
        random_seed: Optional[int] = None
        additional_statistics_control: AdditionalStatisticsControl = None
        mutation_probability: Optional[float] = None
        selection_type: Optional[str] = None
        tournament_size: Optional[int] = None
        population_size: Optional[int] = None
        elitism_size: Optional[int] = None

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
            problem_solution_ga_support:ProblemSolutionGaSupport,
            mutation_probability: Optional[float],
            selection_type: str,
            tournament_size: Optional[int],
            population_size: int,
            elitism_size: Optional[int])->None:
        """
        Create new instance of class :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer`. 
        That instance implements :ref:`GA<Genetic_Algorithm>` algorithm. 

        :param `FinishControl` finish_control: structure that control finish criteria for metaheuristic execution
        :param int random_seed: random seed for metaheuristic execution
        :param `AdditionalStatisticsControl` additional_statistics_control: structure that controls additional
        statistics obtained during population-based metaheuristic execution
        :param `OutputControl` output_control: structure that controls output
        :param `Problem` problem: problem to be solved
        :param `list[Solution]` solution_template: initial solution of the problem
        :param `ProblemSolutionGaSupport` problem_solution_ga_support: placeholder for additional methods, specific for GA
        execution, which depend of precise solution type 
        :param `float` mutation_probability: probability of mutation
        :param `Optional[int]` tournament_size: size of the tournament if tournament selection is implemented
        :param `int` population_size: size of the population
        :param `Optional[int]` elitism_size: elitism size
        :param `str` selection_type: str, possible values: 'selectionTournament', 'selectionRoulette', 'selectionRangRoulette' 
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
        if not isinstance(problem_solution_ga_support, ProblemSolutionGaSupport):
                raise TypeError('Parameter \'problem_solution_ga_support\' must be \'ProblemSolutionGaSupport\'.')
        if not isinstance(mutation_probability, float) and mutation_probability <= 1 and mutation_probability >=0:
                raise TypeError('Parameter \'mutation_probability\' must be \'float\' and between 0 and 1.')
        if not isinstance(selection_type, str):
                raise TypeError('Parameter \'selection_type\' must be \'str\'.')
        if not isinstance(tournament_size, Optional[int]) and tournament_size > 0:
                raise TypeError('Parameter \'tournament_size\' must be \'int\' and greater than 0.')
        if not isinstance(population_size, int) and tournament_size > 1:
                raise TypeError('Parameter \'population_size\' must be \'int\' and greater than 1.')
        if not isinstance(elitism_size, Optional[int]) and elitism_size > 0:
                raise TypeError('Parameter \'elitism_size\' must be \'int\' and greater than 0.')
        super().__init__( name='ga',
                finish_control=finish_control,
                random_seed=random_seed,
                additional_statistics_control=additional_statistics_control,
                output_control=output_control,
                problem=problem,
                solution_template=solution_template)
        self.__problem_solution_ga_support:ProblemSolutionGaSupport = problem_solution_ga_support
        self.__mutation_probability:float = mutation_probability
        self.__tournament_size:int = tournament_size
        self.__population_size:int = population_size
        self.__elitism_size:int = elitism_size
        self.__selection_type = selection_type
        self.__problem_solution_ga_support:ProblemSolutionGaSupport = problem_solution_ga_support
        self.__implemented_selection_methods:dict[str,function] = {
            'selectionTournament':  self.__problem_solution_ga_support.selection_tournament,
            'selectionRoulette':  self.__problem_solution_ga_support.selection_roulette,
            'selectionRangRoulette':  self.__problem_solution_ga_support.selection_rang_roulette,
        }
        if( self.__selection_type not in self.__implemented_selection_methods.keys()):
            raise ValueError( 'Value \'{}\' for GA selection_type is not supported'.format(self.__selection_type))
        self.__selection_method = self.__implemented_selection_methods[self.__selection_type]
        self.__crossover_method = self.__problem_solution_ga_support.crossover
        self.__mutation_method = self.__problem_solution_ga_support.mutation

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
            construction_tuple.problem_solution_ga_support,
            construction_tuple.mutation_probability,
            construction_tuple.selection_type,
            construction_tuple.tournament_size,
            construction_tuple.population_size,
            construction_tuple.elitism_size)

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
    def mutation_probability(self)->float:
        """
        Property getter for the `mutation_probability` parameter for GA

        :return: `mutation_probability` parameter for GA
        :rtype: float
        """
        return self.__mutation_probability
    
    @property
    def selection_type(self)->str:
        """
        Property getter for the `selection_type` parameter for GA

        :return: `selection_type` parameter for GA
        :rtype: str
        """
        return self.__selection_type
    
    @property
    def population_size(self)->int:
        """
        Property getter for the `population_size` parameter for GA

        :return: `population_size` parameter for GA
        :rtype: int
        """
        return self.__population_size
    
    @property
    def tournament_size(self)->int:
        """
        Property getter for the `tournament_size` parameter for GA

        :return: `tournament_size` parameter for GA
        :rtype: int
        """
        return self.__tournament_size
    
    @property
    def elitism_size(self)->int:
        """
        Property getter for the `elitism_size` parameter for GA

        :return: `elitism_size` parameter for GA
        :rtype: int
        """
        return self.__elitism_size
    
    @property
    def elitism_size(self)->int:
        """
        Property getter for the `elitism_size` parameter for GA

        :return: `elitism_size` parameter for GA
        :rtype: int
        """
        return self.__elitism_size

    def init(self)->None:
        """
        Initialization of the GA algorithm
        """
        self.__current_population = [self.solution_template.copy() for _ in range(self.__population_size)]
        for i in range(self.__population_size):
            self.__current_population[i].init_random(self.problem)
            self.evaluation = 1
            self.__current_population[i].evaluate(self.problem)
        self.best_solution = min(self.__current_population, key=lambda individual: individual.objective_value)
    
    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the GA algorithm
        """
        self.iteration += 1
        new_solution:list[Solution] = [self.solution_template.copy() for _ in range(self.__population_size)]
        new_solution[:self.__elitism_size] = self.__current_population[:self.__elitism_size].copy()
        for i in range(0,len(self.__current_population), 2):
            if i+1 == len(self.__current_population):
                 break

            self.write_output_values_if_needed("before_step_in_iteration", "selection")
            if self.__selection_type == 'selectionTournament':
                parent1:Solution = self.__selection_method(self.problem, self.__current_population, self.__tournament_size, self)
                parent2:Solution = self.__selection_method(self.problem, self.__current_population, self.__tournament_size, self)
                if parent1 is None or parent2 is None:
                    self.write_output_values_if_needed("after_step_in_iteration", "selection")
                    return
            else:
                parent1:Solution = self.__selection_method(self.problem, self.__current_population, self)
                parent2:Solution = self.__selection_method(self.problem, self.__current_population, self)
                if parent1 is None or parent2 is None:
                    self.write_output_values_if_needed("after_step_in_iteration", "selection")
                    return

            self.write_output_values_if_needed("after_step_in_iteration", "selection")
            
            self.write_output_values_if_needed("before_step_in_iteration", "crossover")
            self.__crossover_method(self.problem, parent1, parent2, new_solution[i], new_solution[i+1], self)
            self.write_output_values_if_needed("after_step_in_iteration", "crossover")

            self.write_output_values_if_needed("before_step_in_iteration", "mutation1")
            self.__mutation_method(self.__mutation_probability, self.problem, new_solution[i], self)
            self.write_output_values_if_needed("after_step_in_iteration", "mutation1")

            self.write_output_values_if_needed("before_step_in_iteration", "mutation2")
            self.__mutation_method(self.__mutation_probability, self.problem, new_solution[i+1], self)
            self.write_output_values_if_needed("after_step_in_iteration", "mutation2")

        self.__current_population = new_solution
        for i in range(self.__population_size):
            self.__current_population[i].evaluate(self.problem)

        self.__current_population.sort(key=lambda individual: individual.objective_value)
        self.best_solution = min(self.best_solution, self.__current_population[0].copy(), key=lambda individual: individual.objective_value)

        self.update_additional_statistics_if_required(self.__current_population)

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
        for _ in range(0, indentation):
            s += indentation_symbol
        s += 'selection_type=' + self.__selection_type + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol
        s += 'population_size=' + str(self.population_size) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol
        s += 'mutation_probability=' + str(self.mutation_probability) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol
        if self.__tournament_size is not None:
            s += 'tournament_size=' + str(self.tournament_size) + delimiter
            for _ in range(0, indentation):
                s += indentation_symbol
        s += '__problem_solution_ga_support=' + self.__problem_solution_ga_support.string_rep(delimiter, 
                indentation + 1, indentation_symbol, group_start, group_end) + delimiter 
        for _ in range(0, indentation):
            s += indentation_symbol
        s += 'elitism_size=' + str(self.__elitism_size) + delimiter
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
