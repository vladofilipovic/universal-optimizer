
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.solution.evaluation_cache_control_statistics import EvaluationCacheControlStatistics

class TestEvaluationCacheControlStatisticsProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestEvaluationCacheControlStatisticsProperties\n")

    def setUp(self):
        return

    def test_cache_hit_count_should_be_zero_after_construction(self):
        # Arrange
        EvaluationCacheControlStatistics._instances = {}
        # Act
        eccs = EvaluationCacheControlStatistics()
        # Assert
        self.assertEqual(eccs.cache_hit_count, 0)

    def test_cache_request_count_should_be_zero_after_construction(self):
        # Arrange
        EvaluationCacheControlStatistics._instances = {}
        # Act
        eccs = EvaluationCacheControlStatistics()
        # Assert
        self.assertEqual(eccs.cache_request_count, 0)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestEvaluationCacheControlStatisticsProperties")
    
if __name__ == '__main__':
    unittest.main()