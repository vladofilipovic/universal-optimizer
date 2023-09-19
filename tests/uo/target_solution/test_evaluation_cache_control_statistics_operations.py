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

from uo.target_solution.evaluation_cache_control_statistics import EvaluationCacheControlStatistics

class TestEvaluationCacheControlStatisticsOperations(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestEvaluationCacheControlStatisticsOperations\n")

    def setUp(self):
        self.eccs = EvaluationCacheControlStatistics()
        return
    
    def test_clear_cache_should_work(self):
        self.eccs.cache.clear()
        self.assertEqual(self.eccs.cache, {})

    def test_add_to_cache_should_work(self):
        self.eccs.cache.clear()
        self.eccs.cache["key"] = "value"
        self.assertEqual(self.eccs.cache["key"], "value")

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestEvaluationCacheControlStatisticsOperations")
    
if __name__ == '__main__':
    unittest.main()