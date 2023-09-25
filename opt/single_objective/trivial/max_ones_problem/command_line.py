""" 
The :mod:`~opt.single_objective.trivial.max_ones_problem.command_line` module is used for obtaining execution parameters for execution of the optimizers for max ones problem.
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
        'optimization_type': 'maximization', 
        'writeToOutputFile': True,
        'outputFilePath':'opt/single_objective/trivial/max_ones_problem/outputs/dimension_77.csv', 
        'outputFileNameAppendTimeStamp': False,
        'outputFields': "iteration, evaluation, best_solution.fitness_value, best_solution.string_representation()",
        'outputMoments': "after_algorithm, after_evaluation",
        'inputFilePath': 'opt/single_objective/trivial/max_ones_problem/inputs/dimension_77.txt', 
        'inputFormat': 'txt', 
        'maxNumberEvaluations': 1000, 
        'maxTimeForExecutionSeconds': 0, 
        'randomSeed': 0,
        'evaluationCacheIsUsed': False,
        'calculationSolutionDistanceCacheIsUsed': False,
        'keepAllSolutionCodes': False,
        'kMin': 1,
        'kMax': 3,
        'maxLocalOptima':7,
        'localSearchType': 'local_search_best_improvement',
        'solutionType': 'BitArray'
}


def parse_arguments():
        """ The `parse_arguments` function parses execution parameters for execution of the optimizers for max 
                ones problem.
        """        
        parser = ArgumentParser()

        subparsers = parser.add_subparsers(dest='algorithm')

        parser_vns = subparsers.add_parser('variable_neighborhood_search', help='Execute VNS metaheuristic for max_ones_problem.')
        parser_vns.add_argument('optimization_type', help='Decide if minimization or maximization will be executed.'
                , nargs='?', choices=('minimization', 'maximization'))
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
        parser_vns.add_argument('--inputFilePath', type=str, default='inputs/max_ones_problem/dim_25.txt', 
                help='Input file path for the instance of the problem. ')
        parser_vns.add_argument('--inputFormat', type=str, choices=['txt', 'idle'], default = 'txt',
                help='Input file format. ')    
        parser_vns.add_argument('--maxNumberEvaluations', type=int, default=0, 
                help=("Maximum numbers of evaluations during VNS execution. " 
                "Value 0 means that there is no limit on number of evaluations.") )        
        parser_vns.add_argument('--maxTimeForExecutionSeconds', type=int, default=10, 
                help=("Maximum time for execution (in seconds).\n " 
                "Value 0 means that there is no limit on execution time.") )    
        parser_vns.add_argument('--randomSeed', type=int, default=0, 
                help=("Random seed for the VNS execution. " 
                "Value 0 means that random seed will be obtained from system timer.") )        
        parser_vns.add_argument('--evaluationCacheIsUsed', type=bool, default=False, 
                help=("Should caching be used during evaluation.") )        
        parser_vns.add_argument('--calculationSolutionDistanceCacheIsUsed', type=bool, default=False, 
                help=("Should caching be used during distance calculations for solution individual.") )        
        parser_vns.add_argument('--keepAllSolutionCodes', type=bool, default=False, 
                help=("Should all solution codes be keep during metaheuristic execution.") )        
        parser_vns.add_argument('--kMin', type=int, default=1, 
                help=("VNS parameter k min.") )    
        parser_vns.add_argument('--kMax', type=int, default=3, 
                help=("VNS parameter k max.") )    
        parser_vns.add_argument('--maxLocalOptima', type=int, default=3, 
                help=("VNS parameter maximum number of local optima kept during execution.") )    
        parser_vns.add_argument('--localSearchType', type=str, 
                choices=['local_search_best_improvement', 'local_search_first_improvement'],  
                default='local_search_best_improvement', 
                help=("VNS parameter that determines local search type."))
        parser_vns.add_argument('--solutionType', type=str, 
                choices=['BitArray', 'int'],  
                default='BitArray', 
                help=("VNS parameter that determines solution (representation) type."))
        parser_vns.add_argument( "--log", default="warning", help=("Provide logging level. "
                "Example --log debug', default='warning'") )

        parser_te = subparsers.add_parser('total_enumeration', help='Execute total enumeration algorithm for max_ones_problem.')
        parser_te.add_argument('optimization_type', help='Decide if minimization or maximization will be executed.'
                , nargs='?', choices=('minimization', 'maximization'))
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
        parser_te.add_argument('--inputFilePath', type=str, default='inputs/max_ones_problem/dim_25.txt', 
                help='Input file path for the instance of the problem. ')
        parser_te.add_argument('--inputFormat', type=str, choices=['txt', 'idle'], default = 'txt',
                help='Input file format. ')    
        parser_te.add_argument('--solutionType', type=str, 
                choices=['BitArray', 'int'],  
                default='BitArray', 
                help=("VNS parameter that determines solution (representation) type."))
        parser_te.add_argument( "--log", default="warning", help=("Provide logging level. "
                "Example --log debug', default='warning'") )

        parser_idle = subparsers.add_parser('idle', help='Execute idle algorithm for max_ones_problem.')

        return parser.parse_args()

