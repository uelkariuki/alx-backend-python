#!/usr/bin/env python3

"""Unittests for client.GithubOrgClient class"""

import unittest
from unittest.mock import PropertyMock, patch
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


	def test_public_repos_url(self):
		"""Method to unittest GithubOrgClient._public_repos_url"""
		with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
			mock_org.return_value = {"repos_url": "mocked_url"}
			test_client = GithubOrgClient("org_name")
			result = test_client._public_repos_url
			self.assertEqual(result, "mocked_url")
