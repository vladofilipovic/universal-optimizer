""" 
The :mod:`opt.single_objective.comb.ones_count_max_problem.solver` contains programming code that optimize :ref:`Max Ones<Problem_Ones_Count_Max>` Problem with various optimization techniques.
"""
import sys

from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from random import randrange
from random import seed
from datetime import datetime

from uo.utils.files import ensure_dir 
from uo.utils.logger import logger

from typing import Optional


from opt.single_objective.comb.max_ones_count_problem.command_line import default_parameters_cl
from opt.single_objective.comb.max_ones_count_problem.command_line import parse_arguments

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_int_solution import \
        MaxOnesCountProblemIntSolution
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_bit_array_solution import \
        MaxOnesCountProblemBitArraySolution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_ilp_linopy import \
        MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_ilp_linopy import \
    MaxOnesCountProblemIntegerLinearProgrammingSolver

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support import \
        VnsShakingSupport
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_idle import \
        VnsShakingSupportIdle
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_bit_array import \
        VnsShakingSupportStandardBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_int import \
        VnsShakingSupportStandardInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support import \
        VnsLocalSearchSupport
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_idle import \
        VnsLocalSearchSupportIdle
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_bit_array import \
        VnsLocalSearchSupportStandardBestImprovementBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_fi_bit_array import \
        VnsLocalSearchSupportStandardFirstImprovementBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_int import \
        VnsLocalSearchSupportStandardBestImprovementInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_fi_int import \
        VnsLocalSearchSupportStandardFirstImprovementInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from uo.algorithm.metaheuristic.genetic_algorithm.ga_selection import GaSelection
from uo.algorithm.metaheuristic.genetic_algorithm.ga_selection_idle import GaSelectionIdle
from uo.algorithm.metaheuristic.genetic_algorithm.ga_selection_roulette import GaSelectionRoulette
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support_idle_bit_array import \
                GaCrossoverSupportIdleBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support_one_point_bit_array import \
                GaCrossoverSupportOnePointBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support_idle_bit_array import \
                GaMutationSupportIdleBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support_one_point_bit_array import \
                GaMutationSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_attraction_support_one_point_bit_array import \
                EmAttractionSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support_one_point_bit_array import \
                EmMutationSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_optimizer import EmOptimizerConstructionParameters
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_gen import GaOptimizerGenerationalConstructionParameters
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_gen import GaOptimizerGenerational
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_ss import GaOptimizerSteadyStateConstructionParameters
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_ss import GaOptimizerSteadyState

from uo.algorithm.exact.total_enumeration.te_operations_support_bit_array import\
        TeOperationsSupportBitArray
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

""" 
Solver.

Which solver will be executed depends of command-line parameter algorithm.
"""

def main():
    """ 
    This function executes solver.

    Which solver will be executed depends of command-line parameter algorithm.
    """
    try:
        logger.debug('Solver started.')    
        parameters = default_parameters_cl
        read_parameters_cl = parse_arguments()
        for param_key_value in read_parameters_cl._get_kwargs():
            key:str = param_key_value[0]
            val = param_key_value[1]
            logger.debug('key:{} value:{}'.format(key, val))
            if key is not None and val is not None:
                parameters[key] = val
        logger.debug('Execution parameters: '+ str(parameters))
        # write to output file setup
        if parameters['writeToOutputFile'] is None:
            write_to_output_file:bool = False
        else:
            write_to_output_file:bool = bool(parameters['writeToOutputFile'])
        # output file setup
        if write_to_output_file:
            if parameters['outputFileNameAppendTimeStamp'] is None:
                should_add_timestamp_to_file_name:bool = False
            else:
                should_add_timestamp_to_file_name:bool = bool(parameters['outputFileNameAppendTimeStamp'])
            if parameters['outputFilePath'] is not None and  parameters['outputFilePath'] != '':
                output_file_path_parts:list[str] = parameters['outputFilePath'].split('/')
            else:
                output_file_path_parts:list[str] = ['outputs', 'out']
            output_file_name_ext:str = output_file_path_parts[-1]
            output_file_name_parts:list[str] = output_file_name_ext.split('.')
            if len(output_file_name_parts) > 1:
                output_file_ext:str = output_file_name_parts[-1]
                output_file_name_parts.pop()
                output_file_name = '.'.join(output_file_name_parts)
            else:
                output_file_ext = 'txt'
                output_file_name = output_file_name_parts[0]
            dt = datetime.now()
            output_file_path_parts.pop()
            output_file_dir:str =  '/'.join(output_file_path_parts)
            if should_add_timestamp_to_file_name:
                output_file_path_parts.append( output_file_name +  '-maxones-'  + parameters['algorithm'] + '-' + 
                        parameters['solutionType'] + '-' + dt.strftime("%Y-%m-%d-%H-%M-%S.%f") + '.' + output_file_ext)
            else:
                output_file_path_parts.append( output_file_name +  '-maxones-' +  parameters['algorithm'] + '-' + 
                        parameters['solutionType'] + '.' + output_file_ext)
            output_file_path:str = '/'.join(output_file_path_parts)
            logger.debug('Output file path: ' + str(output_file_path))
            ensure_dir(output_file_dir)
            output_file = open(output_file_path, "w", encoding="utf-8")
        # output control setup
        output_control:Optional[OutputControl] = None
        if write_to_output_file:    
            output_fields:str = parameters['outputFields']
            output_moments:str = parameters['outputMoments']
            output_control = OutputControl(output_file=output_file,
                    fields=output_fields,
                    moments=output_moments)
        # input file setup
        input_file_path:str = parameters['inputFilePath']
        input_format:str = parameters['inputFormat']
        # random seed setup
        if( int(parameters['randomSeed']) > 0 ):
            r_seed:int = int(parameters['randomSeed'])
            logger.info('RandomSeed is predefined. Predefined seed value:  %d' % r_seed)
            if write_to_output_file:
                output_file.write('# RandomSeed is predefined. Predefined seed value:  %d\n' % r_seed)
            seed(r_seed)
        else:
            r_seed = randrange(sys.maxsize) #NOSONAR
            logger.info('RandomSeed is not predefined. Generated seed value:  %d' % r_seed)
            if write_to_output_file:
                output_file.write("# RandomSeed is not predefined. Generated seed value:  %d\n" % r_seed)
            seed(r_seed)
        # finishing criteria setup
        finish_criteria:str = parameters['finishCriteria']
        max_number_evaluations:int = parameters['finishEvaluationsMax']
        max_number_iterations:int = parameters['finishIterationsMax']
        max_time_for_execution_in_seconds = parameters['finishSecondsMax']
        finish_control:FinishControl = FinishControl(
                criteria=finish_criteria,
                evaluations_max=max_number_evaluations,
                iterations_max=max_number_iterations,
                seconds_max=max_time_for_execution_in_seconds)
        # solution evaluations and calculations cache setup
        evaluation_cache_is_used:bool = parameters['solutionEvaluationCacheIsUsed']
        evaluation_cache_max_size:int = parameters['solutionEvaluationCacheMaxSize']
        calculation_solution_distance_cache_is_used:bool = parameters['solutionDistanceCalculationCacheIsUsed']
        calculation_solution_distance_cache_max_size:int = parameters['solutionDistanceCalculationCacheMaxSize']
        # additional statistic control setup
        additional_statistics_control:Optional[AdditionalStatisticsControl] = None
        additional_statistics_is_active:bool =  parameters['additionalStatisticsIsActive']
        if additional_statistics_is_active:
            additional_statistics_keep:str =  parameters['additionalStatisticsKeep']
            max_local_optima_count = parameters['additionalStatisticsMaxLocalOptimaCount']
            additional_statistics_control = AdditionalStatisticsControl(
                keep=additional_statistics_keep, 
                max_local_optima_count=max_local_optima_count
            )
        # problem to be solved
        problem = MaxOnesCountProblem.from_input_file(input_file_path=input_file_path,input_format=input_format)
        start_time = datetime.now()
        if write_to_output_file:
            output_file.write("# {} started at: {}\n".format(parameters['algorithm'], str(start_time)) )
            output_file.write('# Execution parameters: {}\n'.format(parameters))
        # check if ILP is used and finish
        if parameters['algorithm'] == 'integer_linear_programming':
            # solver construction parameters
            ilp_construction_params = MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(
                    output_control=output_control,
                    problem=problem)
            solver:MaxOnesCountProblemIntegerLinearProgrammingSolver = \
                MaxOnesCountProblemIntegerLinearProgrammingSolver.from_construction_tuple(
                    ilp_construction_params)
        elif parameters['algorithm'] == 'variable_neighborhood_search':
            # parameters for VNS process setup
            k_min:int = parameters['kMin']
            k_max:int = parameters['kMax']
            local_search_type = parameters['localSearchType']
            # initial solution and VNS support
            solution_type:str = parameters['solutionType']
            shaking_type:str = parameters['shakingType']
            local_search_type:str = parameters['localSearchType']
            vns_shaking_support:VnsShakingSupport = None
            vns_ls_support:VnsLocalSearchSupport = None
            if solution_type=='BitArray':
                solution:MaxOnesCountProblemBitArraySolution = MaxOnesCountProblemBitArraySolution(
                    random_seed=r_seed)
                if shaking_type == 'standard':
                    vns_shaking_support =  VnsShakingSupportStandardBitArray[str](problem.dimension)
                elif shaking_type == 'idle':
                    vns_shaking_support =  VnsShakingSupportIdle[BitArray,str]() 
                else:
                    raise ValueError(("Invalid pair (solution type, shaking type) is chosen for VNS."))
                if local_search_type == 'standardBestImprovement':
                    vns_ls_support =   VnsLocalSearchSupportStandardBestImprovementBitArray[str](problem.dimension)
                elif local_search_type == 'standardFirstImprovement':
                    vns_ls_support =   VnsLocalSearchSupportStandardFirstImprovementBitArray[str](problem.dimension)
                elif local_search_type == 'idle':
                    vns_ls_support =  VnsLocalSearchSupportIdle[BitArray,str]() 
                else:
                    raise ValueError(("Invalid pair (solution type, local search type) is chosen for VNS."))                
            elif solution_type=='int':
                solution:MaxOnesCountProblemIntSolution = MaxOnesCountProblemIntSolution(r_seed)
                if shaking_type == 'standard':
                    vns_shaking_support =  VnsShakingSupportStandardInt[str](problem.dimension)
                elif shaking_type == 'idle':
                    vns_shaking_support =  VnsShakingSupportIdle[int,str]() 
                else:
                    raise ValueError(("Invalid pair (solution type, shaking type) is chosen for VNS."))
                if local_search_type == 'standardBestImprovement':
                    vns_ls_support =   VnsLocalSearchSupportStandardBestImprovementInt[str](problem.dimension)
                elif local_search_type == 'standardFirstImprovement':
                    vns_ls_support =   VnsLocalSearchSupportStandardFirstImprovementInt[str](problem.dimension)
                elif local_search_type == 'idle':
                    vns_ls_support =  VnsLocalSearchSupportIdle[int,str]() 
                else:
                    raise ValueError(("Invalid pair (solution type, local search type) is chosen for VNS."))                
            else:
                raise ValueError("Invalid solution/representation type is chosen for VNS.")
            # solver construction parameters
            vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
            vns_construction_params.output_control = output_control
            vns_construction_params.problem = problem
            vns_construction_params.solution_template = solution
            vns_construction_params.finish_control = finish_control
            vns_construction_params.random_seed = r_seed
            vns_construction_params.additional_statistics_control = additional_statistics_control
            vns_construction_params.vns_shaking_support = vns_shaking_support
            vns_construction_params.vns_ls_support = vns_ls_support
            vns_construction_params.k_min = k_min
            vns_construction_params.k_max = k_max
            vns_construction_params.local_search_type = local_search_type
            solver:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        elif parameters['algorithm'] == 'genetic_algorithm':
            # parameters for GA process setup
            selection_type:str = parameters['selectionType']
            ga_selection = None
            if selection_type=='Roulette':
                ga_selection:GaSelection = GaSelectionRoulette()
            elif selection_type=='Idle':
                ga_selection:GaSelection = GaSelectionIdle()
            else:
                raise ValueError("Invalid solution/representation type is chosen for GA.")
            # initial solution
            solution_type:str = parameters['solutionType']
            if solution_type=='BitArray':
                solution:MaxOnesCountProblemBitArraySolution = MaxOnesCountProblemBitArraySolution(
                    random_seed=r_seed)
            else:
                raise ValueError("Invalid solution/representation type is chosen for GA.")
            ga_crossover_support = None
            crossover_type:str = parameters['crossoverType']
            if crossover_type=='OnePoint' and solution_type=='BitArray':
                crossover_probability:float = parameters['crossoverProbability']
                ga_crossover_support = GaCrossoverSupportOnePointBitArray[str](
                    crossover_probability=crossover_probability)
            elif crossover_type=='Idle':
                ga_crossover_support = GaCrossoverSupportIdleBitArray[str]()
            else:
                raise ValueError("Invalid pair (crossover type, representation type) is chosen for GA.")
            ga_mutation_support = None
            mutation_type:str = parameters['mutationType']
            if mutation_type=='OnePoint' and solution_type=='BitArray':
                mutation_probability:float = parameters['mutationProbability']
                ga_mutation_support = GaMutationSupportOnePointBitArray[str](
                    mutation_probability=mutation_probability)
            elif mutation_type=='Idle':
                ga_mutation_support = GaMutationSupportIdleBitArray[str]()
            else:
                raise ValueError("Invalid pair (mutation type, representation type) is chosen for GA.")
            population_size:int = parameters['populationSize']
            elite_count:int = parameters['eliteCount']
            population_replacement_policy:str = parameters['populationReplacementPolicy']
            if population_replacement_policy=='Generational':
                ga_construction_params:GaOptimizerGenerationalConstructionParameters = \
                    GaOptimizerGenerationalConstructionParameters()
                ga_construction_params.output_control = output_control
                ga_construction_params.problem = problem
                ga_construction_params.solution_template = solution
                ga_construction_params.finish_control = finish_control
                ga_construction_params.random_seed = r_seed
                ga_construction_params.additional_statistics_control = additional_statistics_control
                ga_construction_params.ga_selection = ga_selection
                ga_construction_params.ga_crossover_support = ga_crossover_support
                ga_construction_params.ga_mutation_support = ga_mutation_support
                ga_construction_params.population_size = population_size
                ga_construction_params.elite_count = elite_count
                solver:GaOptimizerGenerational = GaOptimizerGenerational.from_construction_tuple(ga_construction_params) 
            elif population_replacement_policy=='SteadyState':
                ga_construction_params:GaOptimizerSteadyStateConstructionParameters = \
                    GaOptimizerSteadyStateConstructionParameters()
                ga_construction_params.output_control = output_control
                ga_construction_params.problem = problem
                ga_construction_params.solution_template = solution
                ga_construction_params.finish_control = finish_control
                ga_construction_params.random_seed = r_seed
                ga_construction_params.additional_statistics_control = additional_statistics_control
                ga_construction_params.ga_selection = ga_selection
                ga_construction_params.ga_crossover_support = ga_crossover_support
                ga_construction_params.ga_mutation_support = ga_mutation_support
                ga_construction_params.population_size = population_size
                ga_construction_params.elite_count = elite_count
                solver:GaOptimizerSteadyState = GaOptimizerSteadyState.from_construction_tuple(ga_construction_params) 
            else:
                raise ValueError("Invalid population replacement policy is chosen for GA.")
        elif parameters['algorithm'] == 'total_enumeration':
            # initial solution and te support
            solution_type:str = parameters['solutionType']
            te_operations_support = None
            if solution_type=='BitArray':
                solution:MaxOnesCountProblemBitArraySolution = MaxOnesCountProblemBitArraySolution(r_seed, 
                            evaluation_cache_is_used=evaluation_cache_is_used,
                            evaluation_cache_max_size=evaluation_cache_max_size,
                            distance_calculation_cache_is_used=calculation_solution_distance_cache_is_used,
                            distance_calculation_cache_max_size=calculation_solution_distance_cache_max_size)
                te_operations_support = TeOperationsSupportBitArray[str]()
            else:
                raise ValueError("Invalid solution/representation type is chosen for TE.")
            # solver construction parameters
            te_construction_params:TeOptimizerConstructionParameters = TeOptimizerConstructionParameters()
            te_construction_params.output_control = output_control
            te_construction_params.problem = problem
            te_construction_params.solution_template = solution
            te_construction_params.te_operations_support = te_operations_support
            solver:TeOptimizer = TeOptimizer.from_construction_tuple(te_construction_params)
        else:
            raise ValueError('Invalid optimization algorithm is chosen.')
        bs = solver.optimize()
        logger.debug('Method -{}- execution finished.'.format(parameters['algorithm'])) 
        logger.info('Best solution code: {}'.format(bs.string_representation()))            
        logger.info('Best solution objective: {}, fitness: {}'.format(bs.objective_value,
                bs.fitness_value))
        logger.info('Number of iterations: {}, evaluations: {}'.format(solver.iteration, 
                solver.evaluation))  
        logger.info('Execution: {} - {}'.format(solver.execution_started, solver.execution_ended))          
        logger.debug('Solver ended.')    
        return
    except Exception as exp:
        if hasattr(exp, 'message'):
            logger.exception('Exception: %s\n' % exp.message)
        else:
            logger.exception('Exception: %s\n' % str(exp))
        
# This means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()


