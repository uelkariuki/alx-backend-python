#!/usr/bin/env python3

"""Unittests for client.GithubOrgClient class"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient, get_json
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
	"""Unittests for GithubOrgClient class"""

	@parameterized.expand([
		("google",),
		("abc",)
	])
	@patch('client.get_json', return_value={"key":"value"})
	def test_org(self, org_name, mock_get_json):
		"""Method to ensure org method works as expected"""
		test_client = GithubOrgClient(org_name)
		result = test_client.org
		self.assertEqual(result, {"key":"value"})
		mock_get_json.assert_called_once()

