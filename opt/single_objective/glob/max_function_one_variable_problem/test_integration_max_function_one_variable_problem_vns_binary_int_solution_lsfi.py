
import unittest   
import unittest.mock as mocker

from random import seed

from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_int import \
        VnsShakingSupportStandardInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_int import \
        VnsLocalSearchSupportStandardBestImprovementInt
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import \
        VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.glob.max_function_one_variable_problem.max_function_one_variable_problem import \
        MaxFunctionOneVariableMaxProblem
from opt.single_objective.glob.max_function_one_variable_problem.max_function_one_variable_problem_int_solution \
        import FunctionOneVariableMaxProblemIntSolution

class TestIntegrationMaxFunctionOneVariableMaxProblemIntSolutionLsfi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationFunctionOneVariableMaxProblemIntSolutionLsbi\n")

    def setUp(self):
        # Arrange
        self.problem_to_solve:MaxFunctionOneVariableMaxProblem = MaxFunctionOneVariableMaxProblem(
                expression='7-x*x',
                domain_low=-3,
                domain_high=3 )
        self.solution:FunctionOneVariableMaxProblemIntSolution = FunctionOneVariableMaxProblemIntSolution(
                domain_from=self.problem_to_solve.domain_low, domain_to=self.problem_to_solve.domain_high, 
                number_of_intervals=600, random_seed=43434343)
        seed(self.solution.random_seed)
        self.solution.init_random(problem=self.problem_to_solve)
        self.solution.evaluate(self.problem_to_solve)           
        self.finish_control:FinishControl = FinishControl(criteria='evaluations & seconds', evaluations_max=10000, 
                seconds_max=100)
        self.vns_shaking_support:VnsShakingSupportStandardInt = \
                VnsShakingSupportStandardInt(self.solution.number_of_intervals)
        self.vns_ls_support:VnsLocalSearchSupportStandardBestImprovementInt = \
                VnsLocalSearchSupportStandardBestImprovementInt(self.solution.number_of_intervals)
        self.vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        self.vns_construction_params.problem = self.problem_to_solve
        self.vns_construction_params.solution_template = self.solution
        self.vns_construction_params.vns_shaking_support = self.vns_shaking_support
        self.vns_construction_params.vns_ls_support = self.vns_ls_support
        self.vns_construction_params.finish_control =self.finish_control
        self.vns_construction_params.random_seed = 43434343
        self.vns_construction_params.k_min = 1
        self.vns_construction_params.k_max = 3
        self.optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(self.vns_construction_params)
        self.bs = self.optimizer.optimize()

    def test_best_solution_after_optimization_should_be_all_optimal(self):
        # Act
        result = 0.0
        arg = self.optimizer.best_solution.argument(self.optimizer.best_solution.representation)
        # Assert
        self.assertLessEqual(abs( arg-result), 0.5)

    def test_best_solution_after_optimization_should_have_optimal_objective_value(self):
        result = 7.0
        self.assertLessEqual(abs(self.optimizer.best_solution.objective_value - result), 0.3 )

    def test_best_solution_after_optimization_should_have_optimal_fitness_value(self):
        result = 7.0
        self.assertLessEqual(abs(self.optimizer.best_solution.fitness_value - result), 0.3)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestIntegrationFunctionOneVariableMaxProblemIntSolutionLsbi")
    
if __name__ == '__main__':
    unittest.main()