import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.target_solution.distance_calculation_cache_control_statistics import DistanceCalculationCacheControlStatistics

class TestDistanceCalculationCacheControlStatistics(unittest.TestCase):

    # Creating a new instance of DistanceCalculationCacheControlStatistics with valid parameters sets the is_caching and max_cache_size properties correctly
    def test_valid_parameters_set_properties_correctly(self):
        # Arrange
        is_caching = True
        max_cache_size = 100
        # Act
        cache_control_stats = DistanceCalculationCacheControlStatistics(is_caching, max_cache_size)
        # Assert
        self.assertEqual(cache_control_stats.is_caching, is_caching)
        self.assertEqual(cache_control_stats.max_cache_size, max_cache_size)

    # The cache property returns an empty dictionary when no cache has been set
    def test_cache_property_returns_empty_dictionary_when_no_cache_set(self):
        # Arrange
        cache_control_stats = DistanceCalculationCacheControlStatistics(True, 100)
        # Act
        cache = cache_control_stats.cache
        # Assert
        self.assertEqual(cache, {})

    # The cache property returns the dictionary set by the cache setter method
    def test_cache_property_returns_set_dictionary(self):
        # Arrange
        cache_control_stats = DistanceCalculationCacheControlStatistics(True, 100)
        cache = {(1, 2): 10, (3, 4): 20}
        # Act
        cache_control_stats.cache = cache
        returned_cache = cache_control_stats.cache
        # Assert
        self.assertEqual(returned_cache, cache)

    # The increment_cache_hit_count method increments the cache_hit_count property by 1
    def test_increment_cache_hit_count_increments_cache_hit_count_property(self):
        # Arrange
        cache_control_stats = DistanceCalculationCacheControlStatistics(True, 100)
        initial_cache_hit_count = cache_control_stats.cache_hit_count
        # Act
        cache_control_stats.increment_cache_hit_count()
        incremented_cache_hit_count = cache_control_stats.cache_hit_count
        # Assert
        self.assertEqual(incremented_cache_hit_count, initial_cache_hit_count + 1)

    # The increment_cache_request_count method increments the cache_request_count property by 1
    def test_increment_cache_request_count_increments_cache_request_count_property(self):
        # Arrange
        cache_control_stats = DistanceCalculationCacheControlStatistics(True, 100)
        initial_cache_request_count = cache_control_stats.cache_request_count
        # Act
        cache_control_stats.increment_cache_request_count()
        incremented_cache_request_count = cache_control_stats.cache_request_count
        # Assert
        self.assertEqual(incremented_cache_request_count, initial_cache_request_count + 1)

    # Creating a new instance of DistanceCalculationCacheControlStatistics with invalid parameters raises a TypeError
    def test_invalid_parameters_raises_type_error(self):
        # Arrange
        invalid_is_caching = "True"
        invalid_max_cache_size = "100"
        # Act & Assert
        with self.assertRaises(TypeError):
            DistanceCalculationCacheControlStatistics(invalid_is_caching, invalid_max_cache_size)
    
    # Setting the is_caching property with an invalid value raises a TypeError
    def test_setting_invalid_is_caching_raises_type_error(self):
        # Arrange
        cache_control_stats = DistanceCalculationCacheControlStatistics(True, 100)
        invalid_is_caching = "True"
        # Act & Assert
        with self.assertRaises(TypeError):
            cache_control_stats.is_caching = invalid_is_caching

    # Setting the cache property with an invalid value raises a TypeError
    def test_setting_invalid_cache_raises_type_error(self):
        # Arrange
        cache_control_stats = DistanceCalculationCacheControlStatistics(True, 100)
        invalid_cache = "cache"
        # Act & Assert
        with self.assertRaises(TypeError):
            cache_control_stats.cache = invalid_cache

    # The string_rep method returns a string representation of the instance with the specified delimiter, indentation, indentation_symbol, group_start, and group_end values
        # Arrange
        cache_control_stats = DistanceCalculationCacheControlStatistics(True, 100)
        delimiter = ","
        indentation = 2
        indentation_symbol = " "
        group_start = "["
        group_end = "]"
        # Act
        string_rep = cache_control_stats.string_rep(delimiter, indentation, indentation_symbol, group_start, group_end)

        # Assert
        expected_string_rep = '__is_caching=True'
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = '__cache_hit_count=0'
        self.assertIn(expected_string_rep, string_rep)
        expected_string_rep = '__cache_requests_count=0'
        self.assertIn(expected_string_rep, string_rep)

    # The __format__ method returns a formatted string representation of the cache control and statistics structure with the specified format specification
    def test_format_returns_formatted_string_representation_with_specified_format_specification2(self):
        # Arrange
        cache_control_stats = DistanceCalculationCacheControlStatistics(True, 100)
        format_specification = "d"
        # Act
        formatted_string = cache_control_stats.__format__(format_specification)
        # Assert
        expected_string_rep = '__is_caching=True'
        self.assertIn(expected_string_rep, formatted_string)
        expected_string_rep = '__cache_hit_count=0'
        self.assertIn(expected_string_rep, formatted_string)
        expected_string_rep = '__cache_requests_count=0'
        self.assertIn(expected_string_rep, formatted_string)
