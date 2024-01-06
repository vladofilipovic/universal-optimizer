import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem
from uo.target_problem.target_problem_void import TargetProblemVoid

from uo.target_solution.quality_of_solution import QualityOfSolution
from uo.target_solution.target_solution import TargetSolution 
from uo.target_solution.target_solution_void_object_str import TargetSolutionVoidObjectStr