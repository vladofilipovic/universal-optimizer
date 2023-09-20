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

class TestEvaluationCacheControlStatisticsProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestEvaluationCacheControlStatisticsProperties\n")

    def setUp(self):
        self.eccs = EvaluationCacheControlStatistics()
        return

    def test_is_caching_should_be_true_as_it_is_set(self):
        self.eccs.is_caching = True
        self.assertTrue(self.eccs.is_caching)

    def test_is_caching_should_be_false_as_it_is_set(self):
        self.eccs.is_caching = False
        self.assertFalse(self.eccs.is_caching)

    def test_cache_hit_count_should_be_zero_after_construction(self):
        self.assertEqual(self.eccs.cache_hit_count, 0)

    def test_cache_request_count_should_be_zero_after_construction(self):
        self.assertEqual(self.eccs.cache_request_count, 0)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestEvaluationCacheControlStatisticsProperties")
    
if __name__ == '__main__':
    unittest.main()