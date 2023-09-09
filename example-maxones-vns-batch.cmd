cd app/max_ones_problem
@echo -----------
solver.py -h
@echo -----------
solver.py idle -h
@echo -----------
solver.py vns -h
@echo -----------
solver.py vns maximization --writeToOutputFile True --outputFilePath outputs/dimension_25.txt --inputFilePath inputs/dimension_25.txt --inputFormat txt --maxNumberIterations 50  --maxTimeForExecutionSeconds 0 --randomSeed 0 --evaluationCacheIsUsed False --calculationSolutionDistanceCacheIsUsed False --keepAllSolutionCodes False  --kMin 1 --kMax 3 --maxLocalOptima 5 --localSearchType local_search_best_improvement --solutionType BitArray
@echo -----------
solver.py vns maximization --writeToOutputFile True --outputFilePath outputs/dimension_25.txt --inputFilePath inputs/dimension_25.txt --inputFormat txt --maxNumberIterations 50  --maxTimeForExecutionSeconds 0 --randomSeed 0 --evaluationCacheIsUsed False --calculationSolutionDistanceCacheIsUsed False --keepAllSolutionCodes False  --kMin 1 --kMax 3 --maxLocalOptima 5 --localSearchType local_search_best_improvement --solutionType int
