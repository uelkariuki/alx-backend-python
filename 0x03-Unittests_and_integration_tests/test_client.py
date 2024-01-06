#!/usr/bin/env python3

"""Parameterize a unit test"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """
    Class with Unit tests for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2,)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any):
        """ Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)