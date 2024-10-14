cd opt/single_objective/glob/max_function_one_variable_problem
@echo -----------
python solver.py -h
@echo -----------
python solver.py idle -h
@echo -----------
python solver.py variable_neighborhood_search -h
@echo -----------
python solver.py variable_neighborhood_search --writeToOutputFile True --outputFilePath outputs/(7-x2)[-3,3].csv --inputFilePath inputs/(7-x2)[-3,3].txt --inputFormat txt --finishCriteria evaluations --finishEvaluationsMax 500 --finishIterationsMax 0 --finishSecondsMax 0 --randomSeed 0 --solutionEvaluationCacheIsUsed False --solutionDistanceCalculationCacheIsUsed False  --additionalStatisticsIsActive False --additionalStatisticsKeep none  --additionalStatisticsMaxLocalOptimaCount 5 --kMin 1 --kMax 3 --shakingType standard --localSearchType standardBestImprovement --solutionType int --solutionNumberOfIntervals 2000

