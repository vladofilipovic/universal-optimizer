from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from abc import ABCMeta, abstractmethod

from uo.target_problem.target_problem import TargetProblem

class VnsSupportForTargetSolution(metaclass=ABCMeta):
    
    @abstractmethod
    def vns_randomize(k:int, problem:TargetProblem, solution_codes:list[str])->bool:
        """
        Random VNS shaking of several parts such that new solution code does not differ more than supplied from all solution codes inside collection

        :param TargetProblem problem: problem that is solved
        :param int k: int parameter for VNS
        :param `list[str]` solution_codes: solution codes that should be randomized
        :return: if randomization is successful
        :rtype: bool

        """        
        raise NotImplemented

