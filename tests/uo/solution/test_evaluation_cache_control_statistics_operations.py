
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.solution.evaluation_cache_control_statistics import EvaluationCacheControlStatistics

class TestEvaluationCacheControlStatisticsOperations(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestEvaluationCacheControlStatisticsOperations\n")

    def setUp(self):
        self.eccs = EvaluationCacheControlStatistics()
    
    def test_clear_cache_should_work_0(self):
        self.eccs.cache.clear()
        self.assertEqual(self.eccs.cache, {})

    def test_clear_cache_should_work_0a(self):
        self.eccs.cache.clear()
        self.assertEqual(len(self.eccs.cache), 0)

    def test_add_to_cache_should_work_1(self):
        self.eccs.cache.clear()
        self.eccs.cache["key"] = "value"
        self.assertEqual(self.eccs.cache["key"], "value")

    def test_add_to_cache_should_work_1a(self):
        self.eccs.cache.clear()
        self.eccs.cache["key"] = "value"
        self.eccs.cache["key"] = "value2"
        self.assertEqual(self.eccs.cache["key"], "value2")

    def test_add_to_cache_should_work_2(self):
        self.eccs.cache.clear()
        self.eccs.cache["key"] = "value"
        self.eccs.cache["key2"] = "value2"
        self.assertEqual( len(self.eccs.cache), 2)

    def test_add_to_cache_should_work_2a(self):
        self.eccs.cache.clear()
        self.eccs.cache["key"] = "value"
        self.eccs.cache["key2"] = "value2"
        self.assertEqual( self.eccs.cache, {"key":"value", "key2":"value2"})

    def test_cache_hit_count_should_be_one_after_increment(self):
        self.eccs.increment_cache_hit_count()
        self.assertEqual(self.eccs.cache_hit_count, 1)

    def test_cache_request_count_should_be_one_after_increment(self):
        self.eccs.increment_cache_request_count()
        self.assertEqual(self.eccs.cache_request_count, 1)


    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestEvaluationCacheControlStatisticsOperations")
    
if __name__ == '__main__':
    unittest.main()