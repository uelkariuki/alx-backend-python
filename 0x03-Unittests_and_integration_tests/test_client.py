#!/usr/bin/env python3

"""Unittests for client.GithubOrgClient class"""

import unittest
from unittest.mock import Mock, PropertyMock, patch

from requests import HTTPError
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Method to unittest GithubOrgClient.has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)

@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload":TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests for class GithubOrgClient """
    @classmethod
    def setUpClass(cls):
        """Set up class method for TestIntegrationGithubOrgClient"""

        routes_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,

        }

        def get_payload(url):
            """Method to get payload"""
            if url in routes_payload:
                # Dict used to create a Mock object that mimics
                # requests.Response object, when json method of Mock object is
                # called, it returns the payload corresponding to the URL
                return Mock(**{'json.return_value': routes_payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.mock_get = cls.get_patcher.start()

    def test_public_repos(self):
        """Method to test GithubOrgClient.public_repos"""
        self.assertEqual(GithubOrgClient("google").public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Method to test GithubOrgClient.public_repos
        with an added license argument
        """
        self.assertEqual(GithubOrgClient("google").public_repos(license="apache-2.0"), self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """
        Stops the patcher after running all the tests
        """
        return cls.get_patcher.stop()
