from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent.parent.parent)

import unittest   
import unittest.mock as mocker

from copy import deepcopy

from opt.single_objective.teaching.function_one_variable_problem.function_one_variable_problem import \
        FunctionOneVariableProblem 


class TestFunctionOneVariableProblemProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestFunctionOneVariableProblemProperties\n")

    def setUp(self):
        self.expression = "7-x*x"
        self.domain_low = -2
        self.domain_high = 2
        self.problem = FunctionOneVariableProblem(
                expression = self.expression,
                domain_low = self.domain_low,
                domain_high = self.domain_high,
        )
        return
    
    def test_expression_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.expression, self.expression)

    def test_domain_low_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.domain_low, self.domain_low)

    def test_domain_high_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.domain_high, self.domain_high)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestFunctionOneVariableProblemProperties")
    
if __name__ == '__main__':
    unittest.main()