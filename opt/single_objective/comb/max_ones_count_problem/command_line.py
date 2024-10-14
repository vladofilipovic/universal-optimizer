""" 
The :mod:`~opt.single_objective.comb.ones_count_max_problem.command_line` module is used for obtaining execution parameters for execution of the optimizers for max ones problem.
"""
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

import os
import logging
import datetime as dt
from argparse import ArgumentParser

default_parameters_cl = {
        'algorithm': 'variable_neighborhood_search', 
        'writeToOutputFile': True,
        'outputFilePath':'opt/single_objective/comb/ones_count_problem/outputs/dimension_77.csv', 
        'outputFileNameAppendTimeStamp': False,
        'outputFields': "iteration, evaluation, best_solution.fitness_value, best_solution.string_representation()",
        'outputMoments': "after_algorithm, after_evaluation",
        'inputFilePath': 'opt/single_objective/comb/ones_count_problem/inputs/dimension_77.txt', 
        'inputFormat': 'txt', 
        'finishCriteria':'evaluations & seconds',
        'finishEvaluationsMax': 300, 
        'finishIterationsMax': 0, 
        'finishSecondsMax': 0, 
        'randomSeed': 0,
        'solutionEvaluationCacheIsUsed': False,
        'solutionEvaluationCacheMaxSize': 0,
        'solutionDistanceCalculationCacheIsUsed': False,
        'solutionDistanceCalculationCacheMaxSize': 0,
        'additionalStatisticsIsActive' : False,
        'additionalStatisticsKeep': 'none',
        'additionalStatisticsMaxLocalOptimaCount':7,
        'kMin': 1,
        'kMax': 3,
        "shakingType":'standard',
        "localSearchType":'standardBestImprovement',
        'solutionType': ''
}


def parse_arguments():
        """ The `parse_arguments` function parses execution parameters for execution of the optimizers for max 
                ones problem.
        """        
        parser = ArgumentParser()

        subparsers = parser.add_subparsers(dest='algorithm')

        parser_vns = subparsers.add_parser('variable_neighborhood_search', help='Execute VNS metaheuristic for ones_count_max_problem.')
        parser_vns.add_argument('--writeToOutputFile', type=bool, default=True, 
                help=("Should results of metaheuristic execution be written to output file.") )        
        parser_vns.add_argument('--outputFilePath', type=str, default='output/out.txt', 
                help=("File path of the output file. " 
                "File path '' means that it is within 'outputs' folder."))
        parser_vns.add_argument('--outputFileNameAppendTimeStamp', type=bool, default=False, 
                help=("Should timestamp be automatically added to the name of the output file.") )        
        parser_vns.add_argument('--outputFields', type=str, 
                default='iteration, evaluation, self.best_solution.string_representation()', 
                help=("Comma-separated list of fields whose values will be outputted during algorithm execution. " 
                "Fields 'iteration, evaluation' means that current iterations and current evaluation will be outputted."))
        parser_vns.add_argument('--outputMoments', type=str, default='after_algorithm, after_iteration', 
                help=("Comma-separated list of moments when values will be outputted during algorithm execution. " 
                "List contains of following elements: 'before_algorithm', 'after_algorithm', 'before_iteration', "
                "'after_iteration', 'before_evaluation', 'after_evaluation', 'before_step_in_iteration', "
                "'after_step_in_iteration'"
                "Moments 'after_algorithm' means that result will be outputted after algorithm."))
        parser_vns.add_argument('--inputFilePath', type=str, default='inputs/ones_count_problem/dim_25.txt', 
                help='Input file path for the instance of the problem. ')
        parser_vns.add_argument('--inputFormat', type=str, choices=['txt', 'idle'], default = 'txt',
                help='Input file format. ')    
        parser_vns.add_argument('--finishCriteria', type=str, 
                default='evaluations & seconds', 
                help=("Finish criteria - list of fields separated by '&'. " 
                "Currently, fields can be: 'evaluations', 'iterations', 'seconds'."))
        parser_vns.add_argument('--finishEvaluationsMax', type=int, default=0, 
                help=("Maximum numbers of evaluations during VNS execution. " 
                "Value 0 means that there is no limit on number of evaluations.") )        
        parser_vns.add_argument('--finishIterationsMax', type=int, default=0, 
                help=("Maximum numbers of iterations during VNS execution. " 
                "Value 0 means that there is no limit on number of iterations.") )        
        parser_vns.add_argument('--finishSecondsMax', type=int, default=0, 
                help=("Maximum time for execution (in seconds).\n " 
                "Value 0 means that there is no limit on execution time.") )    
        parser_vns.add_argument('--randomSeed', type=int, default=0, 
                help=("Random seed for the VNS execution. " 
                "Value 0 means that random seed will be obtained from system timer.") )        
        parser_vns.add_argument('--solutionEvaluationCacheIsUsed', type=bool, default=False, 
                help=("Should caching be used during evaluation.") )        
        parser_vns.add_argument('--solutionEvaluationCacheMaxSize', type=int, default=0, 
                help=("Maximum cache size for cache used in solutions evaluation. " 
                "Value 0 means that there is no limit on cache size.") )        
        parser_vns.add_argument('--solutionDistanceCalculationCacheIsUsed', type=bool, default=False, 
                help=("Should caching be used during distance calculations for solution individual.") )        
        parser_vns.add_argument('--solutionDistanceCalculationCacheMaxSize', type=int, default=0, 
                help=("Maximum cache size for cache used in distance calculations between two solutions. " 
                "Value 0 means that there is no limit on cache size.") )        
        parser_vns.add_argument('--additionalStatisticsIsActive', type=bool, default=False, 
                help=("Should gathering of additional statistics be active, or not.") )        
        parser_vns.add_argument('--additionalStatisticsKeep', type=str, 
                default='none', 
                help=("Comma-separated list of statistical data will be calculated and keep during solving. " 
                "Currently, data within list can be: 'all_solution_code', 'distance_among_solutions'."))
        parser_vns.add_argument('--additionalStatisticsMaxLocalOptimaCount', type=int, default=3, 
                help=("Parameter maximum number of local optima kept during execution.") )    
        parser_vns.add_argument('--kMin', type=int, default=1, 
                help=("VNS parameter k min.") )    
        parser_vns.add_argument('--kMax', type=int, default=3, 
                help=("VNS parameter k max.") )    
        parser_vns.add_argument('--shakingType', type=str, 
                choices=['standard', 'idle'],  
                default='standard', 
                help=("VNS parameter that determines shaking type."))
        parser_vns.add_argument('--localSearchType', type=str, 
                choices=['standardBestImprovement', 'standardFirstImprovement', 'idle'],  
                default='standardBestImprovement', 
                help=("VNS parameter that determines local search type."))
        parser_vns.add_argument('--solutionType', type=str, 
                choices=['BitArray', 'int'],  
                default='BitArray', 
                help=("VNS parameter that determines solution (representation) type."))
        parser_vns.add_argument( "--log", default="warning", help=("Provide logging level. "
                "Example --log debug', default='warning'") )

        parser_ga = subparsers.add_parser('genetic_algorithm', help='Execute GA metaheuristic for ones_count_max_problem.')
        parser_ga.add_argument('--writeToOutputFile', type=bool, default=True, 
                help=("Should results of metaheuristic execution be written to output file.") )        
        parser_ga.add_argument('--outputFilePath', type=str, default='output/out.txt', 
                help=("File path of the output file. " 
                "File path '' means that it is within 'outputs' folder."))
        parser_ga.add_argument('--outputFileNameAppendTimeStamp', type=bool, default=False, 
                help=("Should timestamp be automatically added to the name of the output file.") )        
        parser_ga.add_argument('--outputFields', type=str, 
                default='iteration, evaluation, self.best_solution.string_representation()', 
                help=("Comma-separated list of fields whose values will be outputted during algorithm execution. " 
                "Fields 'iteration, evaluation' means that current iterations and current evaluation will be outputted."))
        parser_ga.add_argument('--outputMoments', type=str, default='after_algorithm, after_iteration', 
                help=("Comma-separated list of moments when values will be outputted during algorithm execution. " 
                "List contains of following elements: 'before_algorithm', 'after_algorithm', 'before_iteration', "
                "'after_iteration', 'before_evaluation', 'after_evaluation', 'before_step_in_iteration', "
                "'after_step_in_iteration'"
                "Moments 'after_algorithm' means that result will be outputted after algorithm."))
        parser_ga.add_argument('--inputFilePath', type=str, default='inputs/ones_count_problem/dim_25.txt', 
                help='Input file path for the instance of the problem. ')
        parser_ga.add_argument('--inputFormat', type=str, choices=['txt', 'idle'], default = 'txt',
                help='Input file format. ')    
        parser_ga.add_argument('--finishCriteria', type=str, 
                default='evaluations & seconds', 
                help=("Finish criteria - list of fields separated by '&'. " 
                "Currently, fields can be: 'evaluations', 'iterations', 'seconds'."))
        parser_ga.add_argument('--finishEvaluationsMax', type=int, default=0, 
                help=("Maximum numbers of evaluations during VNS execution. " 
                "Value 0 means that there is no limit on number of evaluations.") )        
        parser_ga.add_argument('--finishIterationsMax', type=int, default=0, 
                help=("Maximum numbers of iterations during VNS execution. " 
                "Value 0 means that there is no limit on number of iterations.") )        
        parser_ga.add_argument('--finishSecondsMax', type=int, default=0, 
                help=("Maximum time for execution (in seconds).\n " 
                "Value 0 means that there is no limit on execution time.") )    
        parser_ga.add_argument('--randomSeed', type=int, default=0, 
                help=("Random seed for the GA execution. " 
                "Value 0 means that random seed will be obtained from system timer.") )        
        parser_ga.add_argument('--solutionEvaluationCacheIsUsed', type=bool, default=False, 
                help=("Should caching be used during evaluation.") )        
        parser_ga.add_argument('--solutionEvaluationCacheMaxSize', type=int, default=0, 
                help=("Maximum cache size for cache used in solutions evaluation. " 
                "Value 0 means that there is no limit on cache size.") )        
        parser_ga.add_argument('--solutionDistanceCalculationCacheIsUsed', type=bool, default=False, 
                help=("Should caching be used during distance calculations for solution individual.") )        
        parser_ga.add_argument('--solutionDistanceCalculationCacheMaxSize', type=int, default=0, 
                help=("Maximum cache size for cache used in distance calculations between two solutions. " 
                "Value 0 means that there is no limit on cache size.") )        
        parser_ga.add_argument('--additionalStatisticsIsActive', type=bool, default=False, 
                help=("Should gathering of additional statistics be active, or not.") )        
        parser_ga.add_argument('--additionalStatisticsKeep', type=str, 
                default='none', 
                help=("Comma-separated list of statistical data will be calculated and keep during solving. " 
                "Currently, data within list can be: 'all_solution_code', 'distance_among_solutions'."))
        parser_ga.add_argument('--additionalStatisticsMaxLocalOptimaCount', type=int, default=3, 
                help=("Parameter maximum number of local optima kept during execution.") )    
        parser_ga.add_argument('--populationReplacementPolicy', type=str, 
                choices=['Generational', 'SteadyState'],  
                default='Generational', 
                help=("GA population replacement policy."))
        parser_ga.add_argument('--selectionType', type=str, 
                choices=['Roulette', 'Idle'],  
                default='Roulette', 
                help=("GA selection type."))
        parser_ga.add_argument('--solutionType', type=str, 
                choices=['BitArray'],  
                default='BitArray', 
                help=("GA parameter that determines solution (representation) type."))
        parser_ga.add_argument('--crossoverType', type=str, 
                choices=['OnePoint','Idle'],  
                default='OnePoint', 
                help=("GA crossover type."))
        parser_ga.add_argument('--crossoverProbability', type=float, default=1, 
                help=("GA crossover probability.") )    
        parser_ga.add_argument('--mutationType', type=str, 
                choices=['OnePoint','Idle'],  
                default='OnePoint', 
                help=("GA mutation type."))
        parser_ga.add_argument('--mutationProbability', type=float, default=1, 
                help=("GA mutation probability.") )    
        parser_ga.add_argument('--populationSize', type=int, default=10, 
                help=("Size of GA population.") )    
        parser_ga.add_argument('--eliteCount', type=int, default=1, 
                help=("GA elite count.") )    
        parser_ga.add_argument( "--log", default="warning", help=("Provide logging level. "
                "Example --log debug', default='warning'") )

        parser_te = subparsers.add_parser('total_enumeration', help='Execute total enumeration algorithm for ones_count_max_problem.')
        parser_te.add_argument('--writeToOutputFile', type=bool, default=True, 
                help=("Should results of metaheuristic execution be written to output file.") )        
        parser_te.add_argument('--outputFilePath', type=str, default='output/out.txt', 
                help=("File path of the output file. " 
                "File path '' means that it is within 'outputs' folder."))
        parser_te.add_argument('--outputFileNameAppendTimeStamp', type=bool, default=False, 
                help=("Should timestamp be automatically added to the name of the output file.") )        
        parser_te.add_argument('--outputFields', type=str, 
                default='iteration, evaluation, self.best_solution.string_representation()', 
                help=("Comma-separated list of fields whose values will be outputted during algorithm execution. " 
                "Fields 'iteration, evaluation' means that current iterations and current evaluation will be outputted."))
        parser_te.add_argument('--outputMoments', type=str, default='after_algorithm, after_iteration', 
                help=("Comma-separated list of moments when values will be outputted during algorithm execution. " 
                "List contains of following elements: 'before_algorithm', 'after_algorithm', 'before_iteration', "
                "'after_iteration', 'before_evaluation', 'after_evaluation', 'before_step_in_iteration', "
                "'after_step_in_iteration'"
                "Moments 'after_algorithm' means that result will be outputted after algorithm."))
        parser_te.add_argument('--inputFilePath', type=str, default='inputs/ones_count_problem/dim_25.txt', 
                help='Input file path for the instance of the problem. ')
        parser_te.add_argument('--inputFormat', type=str, choices=['txt', 'idle'], default = 'txt',
                help='Input file format. ')    
        parser_te.add_argument('--solutionType', type=str, 
                choices=['BitArray', 'int'],  
                default='BitArray', 
                help=("TE parameter that determines solution (representation) type."))
        parser_te.add_argument( "--log", default="warning", help=("Provide logging level. "
                "Example --log debug', default='warning'") )

        parser_ilp = subparsers.add_parser('integer_linear_programming', help='Execute ILP solver for ones_count_max_problem.')
        parser_ilp.add_argument('--writeToOutputFile', type=bool, default=True, 
                help=("Should results of metaheuristic execution be written to output file.") )        
        parser_ilp.add_argument('--outputFilePath', type=str, default='output/out.txt', 
                help=("File path of the output file. " 
                "File path '' means that it is within 'outputs' folder."))
        parser_ilp.add_argument('--outputFileNameAppendTimeStamp', type=bool, default=False, 
                help=("Should timestamp be automatically added to the name of the output file.") )        
        parser_ilp.add_argument('--outputFields', type=str, 
                default='iteration, evaluation, self.best_solution.string_representation()', 
                help=("Comma-separated list of fields whose values will be outputted during algorithm execution. " 
                "Fields 'iteration, evaluation' means that current iterations and current evaluation will be outputted."))
        parser_ilp.add_argument('--outputMoments', type=str, default='after_algorithm, after_iteration', 
                help=("Comma-separated list of moments when values will be outputted during algorithm execution. " 
                "List contains of following elements: 'before_algorithm', 'after_algorithm', 'before_iteration', "
                "'after_iteration', 'before_evaluation', 'after_evaluation', 'before_step_in_iteration', "
                "'after_step_in_iteration'"
                "Moments 'after_algorithm' means that result will be outputted after algorithm."))
        parser_ilp.add_argument('--inputFilePath', type=str, default='inputs/ones_count_problem/dim_25.txt', 
                help='Input file path for the instance of the problem. ')
        parser_ilp.add_argument('--inputFormat', type=str, choices=['txt', 'idle'], default = 'txt',
                help='Input file format. ')    
        parser_ilp.add_argument( "--log", default="warning", help=("Provide logging level. "
                "Example --log debug', default='warning'") )

        parser_idle = subparsers.add_parser('idle', help='Execute idle algorithm for ones_count_max_problem.')

        return parser.parse_args()

