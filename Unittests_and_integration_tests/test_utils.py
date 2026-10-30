#!/usr/bin/env python3
"""Unit tests for the helpers of the utils module."""

import unittest
from typing import Any, Dict, Mapping, Sequence
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests the behavior of the access_nested_map helper."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """Check that following the given path returns the right value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         message: str) -> None:
        """Check that a missing key raises a KeyError naming that key."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), message)


class TestGetJson(unittest.TestCase):
    """Tests the behavior of the get_json helper without any network call."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Check that get_json returns the payload of the mocked response."""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests the behavior of the memoize decorator."""

    def test_memoize(self) -> None:
        """Check that a memoized property calls its method only once."""

        class TestClass:
            """Small class whose property is memoized for the test."""

            def a_method(self) -> int:
                """Return a fixed value that a_property will cache."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Return a_method's value, cached after the first access."""
                return self.a_method()

        with patch.object(
            TestClass, "a_method", return_value=42
        ) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
        mock_method.assert_called_once()
