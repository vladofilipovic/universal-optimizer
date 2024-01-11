
import unittest   
import unittest.mock as mocker

from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import \
        VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem import \
        FunctionOneVariableProblem
from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem_binary_int_solution \
    import FunctionOneVariableProblemBinaryIntSolution
from opt.single_objective.teaching.function_one_variable_problem.\
    function_one_variable_problem_binary_int_solution_vns_support import \
        FunctionOneVariableProblemBinaryIntSolutionVnsSupport

class TestMaxFunctionOneVariableProblemBinaryIntSolutionLsfi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationFunctionOneVariableProblemBinaryIntSolutionLsbi\n")

    def setUp(self):
        # Arrange
        self.output_control:OutputControl = OutputControl(write_to_output=False)
        self.problem_to_solve:FunctionOneVariableProblem = FunctionOneVariableProblem(
                expression='7-x*x',
                domain_low=-3,
                domain_high=3 )
        self.solution:FunctionOneVariableProblemBinaryIntSolution = FunctionOneVariableProblemBinaryIntSolution(
                domain_from=self.problem_to_solve.domain_low, domain_to=self.problem_to_solve.domain_high, 
                number_of_intervals=600, random_seed=43434343)
        self.solution.init_random(problem=self.problem_to_solve)
        self.solution.evaluate(self.problem_to_solve)           
        self.finish_control:FinishControl = FinishControl(criteria='evaluations & seconds', evaluations_max=10000, 
                seconds_max=100)
        self.vns_support:FunctionOneVariableProblemBinaryIntSolutionVnsSupport = \
                FunctionOneVariableProblemBinaryIntSolutionVnsSupport()
        self.additional_statistics_control:AdditionalStatisticsControl = AdditionalStatisticsControl(keep='')
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.output_control = self.output_control
        vns_construction_params.target_problem = self.problem_to_solve
        vns_construction_params.solution_template = self.solution
        vns_construction_params.problem_solution_vns_support = self.vns_support
        vns_construction_params.finish_control =self.finish_control
        vns_construction_params.random_seed = 43434343
        vns_construction_params.additional_statistics_control = self.additional_statistics_control
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        vns_construction_params.local_search_type = 'localSearchBestImprovement'
        self.optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        self.optimizer.optimize()
    
    def test_best_solution_after_optimization_should_be_all_optimal(self):
        # Act
        result = 0.0
        arg = self.optimizer.best_solution.argument(self.optimizer.best_solution.representation)
        # Assert
        self.assertLessEqual(abs( arg-result), 0.1)

    def test_best_solution_after_optimization_should_have_optimal_objective_value(self):
        result = 7.0
        self.assertLessEqual(abs(self.optimizer.best_solution.objective_value - result), 0.01 )

    def test_best_solution_after_optimization_should_have_optimal_fitness_value(self):
        result = 7.0
        self.assertLessEqual(abs(self.optimizer.best_solution.fitness_value - result), 0.1)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestIntegrationFunctionOneVariableProblemBinaryIntSolutionLsbi")
    
if __name__ == '__main__':
    unittest.main()