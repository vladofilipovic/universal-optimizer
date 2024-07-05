from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from datetime import datetime

from uo.utils.logger import logger
from uo.algorithm.output_control import OutputControl
from uo.problem.problem import Problem
from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.solution.solution import Solution
from uo.solution.solution_void_representation_int import SolutionVoidRepresentationInt


from uo.algorithm.optimizer import Optimizer
from uo.algorithm.algorithm import Algorithm

class AlgorithmVoid(Algorithm):
    def __init__(self, 
            problem:Problem=ProblemVoidMinSO(), 
            solution_template:Solution=SolutionVoidRepresentationInt(),            
            name:str="algorithm_void", 
            output_control:OutputControl=None
            )->None:
        super().__init__(name=name, 
                    output_control=output_control, 
                    problem=problem, 
                    solution_template=solution_template)

    def __copy__(self):
        return super().__copy__()

    def copy(self):
        return self.__copy__()

    def init(self):
        return

    def optimize(self)->Solution:
        return None
        
    def __str__(self)->str:
        return super().__str__()

    def __repr__(self)->str:
        return super().__repr__()

    def __format__(self, spec:str)->str:
        return super().__format__(spec)

