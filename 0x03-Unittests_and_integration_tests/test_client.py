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
    @patch('client.get_json', return_value={"key": "value"})
    def test_org(self, org_name, mock_get_json):
        """Method to ensure org method works as expected"""
        test_client = GithubOrgClient(org_name)
        result = test_client.org
        self.assertEqual(result, {"key": "value"})
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Method to unittest GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "mocked_url"}
            test_client = GithubOrgClient("org_name")
            result = test_client._public_repos_url
            self.assertEqual(result, "mocked_url")

    @patch('client.get_json', return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    def test_public_repos(self, mock_get_json):
        """Method to unittest GithubOrgClient.public_repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "mocked_url"
            test_client = GithubOrgClient("org_name")
            result = test_client.public_repos()
            self.assertEqual(result, ["repo1", "repo2"])
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
