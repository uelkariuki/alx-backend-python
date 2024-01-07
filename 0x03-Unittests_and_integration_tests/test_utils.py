#!/usr/bin/env python3

"""Parameterize a unit test"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Any, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """
    Class with Unit tests for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping, path: Sequence,
                               expected: Any):
        """ Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
         ({}, ("a",)),
         ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test KeyError is raised for the unittest"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    class with unit tests for utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})

    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test that utils.get_json returns expected result"""
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestClass:
    """test class to be used in test_memoize"""

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """
    class with unit tests for utils.memoize
    """
    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_function):
        """Test that memoize works well"""
        test_object = TestClass()
        result1 = test_object.a_property
        result2 = test_object.a_property

        mock_function.assert_called_once()
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
