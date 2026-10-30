#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class of the client module."""

import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests the behavior of the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json: MagicMock) -> None:
        """Check that org fetches the right URL and returns its payload."""
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """Check that _public_repos_url reads repos_url from org."""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Check that public_repos lists the repo names of the payload."""
        url = "https://api.github.com/orgs/google/repos"
        payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = payload
        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = url
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_url.assert_called_once()
        mock_get_json.assert_called_once_with(url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, license_key: str,
                         expected: bool) -> None:
        """Check that has_license matches the repo license with the key."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests of GithubOrgClient with only requests.get mocked."""

    @classmethod
    def setUpClass(cls) -> None:
        """Patch requests.get so that each known URL answers its fixture."""
        payloads = {
            "https://api.github.com/orgs/google": cls.org_payload,
            cls.org_payload["repos_url"]: cls.repos_payload,
        }

        def fake_get(url: str) -> Mock:
            """Build a fake response whose json() returns the fixture."""
            response = Mock()
            response.json.return_value = payloads[url]
            return response

        cls.get_patcher = patch("requests.get", side_effect=fake_get)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Remove the requests.get patch once all the tests have run."""
        cls.get_patcher.stop()
