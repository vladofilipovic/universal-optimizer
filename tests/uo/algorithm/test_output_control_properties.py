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

from uo.algorithm.output_control import OutputControl

class TestOutputControlProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestOutputControlProperties\n")

    def setUp(self):
        self.write_to_output = True
        self.output_file = "some file path..."
        self.output_control = OutputControl(
                write_to_output=self.write_to_output,
                output_file=self.output_file 
        )
        return

    def test_write_to_output_should_be_as_it_is_in_constructor(self):
        self.assertEqual(self.output_control.write_to_output, self.write_to_output)

    def test_output_file_should_be_as_it_is_in_constructor(self):
        self.assertEqual(self.output_control.output_file, self.output_file)

    def test_is_output_file_should_be_same_that_it_is_set(self):
        val:str = "other file path..."
        self.output_control.output_file = val
        self.assertEqual(self.output_control.output_file, val)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestOutputControlProperties")
    
if __name__ == '__main__':
    unittest.main()