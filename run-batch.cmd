REM c:/vlado/Courses/Matf/----universal-optimizer-app/app/max_ones_problem/solver.py -h
REM @echo -----------
REM c:/vlado/Courses/Matf/----universal-optimizer-app/app/max_ones_problem/solve.py idle -h
REM @echo -----------
c:/vlado/Courses/Matf/----universal-optimizer-app/app/max_ones_problem/solver.py vns -h
@echo -----------
c:/vlado/Courses/Matf/----universal-optimizer-app/app/max_ones_problem/solver.py vns maximization --writeToOutputFile True --outputFilePath app/max_ones_problem/outputs/dimension_25.txt --inputFilePath app/max_ones_problem/inputs/dimension_25.txt --inputFormat txt --maxNumberIterations 0  --maxTimeForExecutionSeconds 10 --randomSeed 0 --evaluationCacheIsUsed False --calculationSolutionDistanceCacheIsUsed False --keepAllSolutionCodes False  --kMin 1 --kMax 3 --maxLocalOptima 5 --localSearchType local_search_best_improvement
@echo -----------
