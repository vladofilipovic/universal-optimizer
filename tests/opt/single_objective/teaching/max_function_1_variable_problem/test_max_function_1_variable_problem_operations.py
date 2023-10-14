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
import unittest.mock as mock

from copy import deepcopy

from opt.single_objective.teaching.max_function_1_variable_problem.max_function_1_variable_problem import \
        MaxFunction1VariableProblem


class TestMaxFunction1VariableProblemOperations(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestMaxFunction1VariableProblemOperations\n")

    def setUp(self):
        self.expression = "7-x*x"
        self.domain_low = -2
        self.domain_high = 2
        self.problem = MaxFunction1VariableProblem(
                expression = self.expression,
                domain_low = self.domain_low,
                domain_high = self.domain_high
        )
        return
    
    def test_create_with_invalid_local_search_type_should_raise_value_exception_with_proper_message(self):
        with self.assertRaises(ValueError) as context:
            self.problem.__load_from_file__(file_path='xxx', data_format='xxx')
        self.assertEqual("Value for data format 'xxx' is not supported", context.exception.args[0])

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestMaxFunction1VariableProblemOperations")
    
if __name__ == '__main__':
    unittest.main()