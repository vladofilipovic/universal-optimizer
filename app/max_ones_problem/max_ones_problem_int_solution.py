""" 
..  _py_max_ones_problem_int_solution:

The :mod:`~app.max_ones_problem.max_ones_problem_int_solution` contains class :class:`~app.max_ones_problem.max_ones_problem_int_solution.MaxOnesProblemIntSolution`, that represents solution of the :ref:`Problem_Max_Ones`, where `int` representation of the problem has been used.
"""
class MaxOneProblemIntSolution(TargetSolution):
    
    def __init__(self)->None:
        super().__init__("MaxOneProblemIntSolution", fitness_value=None, objective_value=None, is_feasible=False)

    def __copy__(self):
        sol = deepcopy(self)
        return sol

    def copy(self):
        return self.__copy__()
        
    def copy_to(self, destination)->None:
        destination = self.__copy__()

    @property
    def representation(self)->int:
            return self.__representation

    @representation.setter
    def representation(self, value:int)->None:
        self.__representation = value

    def random_init(self, problem:TargetProblem)->None:
        self.representation = random()
        mask:int = ~0
        mask <<= 32-problem.dimension
        mask = ~mask 
        self.__representation &= mask

    def solution_code(self)->str:
        return bin(self.__representation)

    def calculate_objective_fitness_feasibility(self, problem:TargetProblem)->ObjectiveFitnessFeasibility:
        ones_count = self.representation.bit_count()
        return ObjectiveFitnessFeasibility(ones_count, ones_count, True)

    def solution_code_distance(solution_code_1:str, solution_code_2:str)->float:
        rep_1:int = int(solution_code_1, 2)
        rep_2:int = int(solution_code_2, 2)
        result = (rep_1 ^ rep_2).count(True)
        return result 

    def best_1_change(self, problem:TargetProblem)->bool:
        best_ind:int = None
        best_fv:float = self.fitness_value
        for i in range(0, problem.dimension):
            mask:int = 1 << i
            mask = ~mask
            self.representation ^= mask 
            new_fv = self.calculate_objective_fitness_feasibility(problem).fitness_value
            if new_fv > best_fv:
                best_ind = i
                best_fv = new_fv
            self.representation ^= mask 
        if best_ind is not None:
            mask:int = 1 << best_ind
            mask = ~mask
            self.representation ^= mask
            self.evaluate(problem)
            if self.fitness_value != best_fv:
                raise Exception('Fitness calculation within best_1_change function is not correct.')
            return True
        return False

    def vns_randomize(self, problem:TargetProblem, k:int, solution_codes:list[str])->bool:
        """
        Random VNS shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints 
        :param problem:TargetProblem -- problem that is solved
        :param k:int -- parameter for VNS
        :param solution_codes:list[str] -- solution codes that should be randomized
        :return: bool -- if randomization is successful 
        """    
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for i in range(0,k):
                positions.append(choice(range(k)))
            new_representation:int = self.representation
            mask:int = 0
            for p in positions:
                mask |= 1 << p
            mask = ~mask
            self.representation ^= mask
            all_ok:bool = True
            for sc in solution_codes:
                sc_representation = bin(sc,2)
                if sc_representation != 0:
                    comp_result:int = (sc_representation ^ new_representation).bit_count()
                    if comp_result > k:
                        all_ok = False
            if all_ok:
                break
        if tries < limit:
            self.representation = new_representation
            self.evaluate(problem)
            return True
        else:
            return False 

    def string_representation(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
        s = delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s += super().string_representation(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'representation=' + bin(self.__representation)
        s += delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __repr__(self)->str:
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        return self.string_representation('\n', 0, '   ', '{', '}')
