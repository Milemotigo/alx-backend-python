#!/usr/bin/env python3
"""
module: test_client.py
"""
import unittest


import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    unittest for GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_result, mock_get_json):
        """
        org method unittest
        """
        client = GithubOrgClient(org_name)
        mock_get_json.return_value = Mock(return_value=expected_result)
        result = client.org()

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )

        self.assertEqual(result, expected_result)

    def test_public_repos_url(self):
        """
        Test for _punlic_repos_url
        """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock) as mock_check:

            GithubOrgClient('google')._public_repos_url
            mock_check.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }

            expected_url = "https://api.github.com/orgs/google/repos"

            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                expected_url
                )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        test for public_repos method
        """
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        }
                },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        }
                }
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(GithubOrgClient('google').public_repos(),
                             ["episodes.dart", "cpp-netlib",])

            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

        @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
        
        ])
        def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
            """Tests the `has_license` method."""
            gh_org_client = GithubOrgClient("google")
            client_has_licence = gh_org_client.has_license(repo, key)
            self.assertEqual(client_has_licence, expected)
            
        @parameterized_class([
            {
                'org_payload': TEST_PAYLOAD[0][0],
                'repos_payload': TEST_PAYLOAD[0][1],
                'expected_repos': TEST_PAYLOAD[0][2],
                'apache2_repos': TEST_PAYLOAD[0][3],
                },
            ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
         """Sets up class fixtures before running tests."""
         route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
            }
    def get_payload(url):
        if url in route_payload:
            return Mock(**{'json.return_value': route_payload[url]})
        return HTTPError
                
    cls.get_patcher = patch("requests.get", side_effect=get_payload)
    cls.get_patcher.start()
    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
        GithubOrgClient("google").public_repos(),
        self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
        GithubOrgClient("google").public_repos(license="apache-2.0"),
        self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
 