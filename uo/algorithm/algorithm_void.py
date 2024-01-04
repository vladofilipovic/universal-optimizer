from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from datetime import datetime

from uo.utils.logger import logger
from uo.algorithm.output_control import OutputControl
from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution

from uo.algorithm.optimizer import Optimizer
from uo.algorithm.algorithm import Algorithm

class AlgorithmVoid(Algorithm):
    def __init__(self, name:str, output_control:OutputControl,
            target_problem:TargetProblem)->None:
        super().__init__(name, output_control, target_problem)

    def __copy__(self):
        return super().__copy__()

    def copy(self):
        return self.__copy__()

    def init(self):
        return

    def optimize(self):
        return
        
    def __str__(self)->str:
        return super().__str__()

    def __repr__(self)->str:
        return super().__repr__()

    def __format__(self, spec:str)->str:
        return super().__format__(spec)

