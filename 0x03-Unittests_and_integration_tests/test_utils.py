#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""

import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Testing the access_nested_map"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """manager to test that a KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


# @parameterized.expand([
#     ("http://example.com", {"payload": True}),
#     ("http://holberton.io", {"payload": False}),
# ])
# @patch("request.get")
# class TestGetJson(unittest.TestCase):
#     def test_get_json(self, test_url, payload, mock_data):
#         """ Mock HTTP calls"""
#         mock_response = Mock()
#         mock_response.json.return_value = payload
#         mock_data.return_value = mock_response
#         result = get_json(test_url)
#         mock_data.assert_called_once_with(test_url)

#         self.assertEqual(result, payload)

class TestGetJson(unittest.TestCase):
    """
    unitest for the method utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, payload, mockrequests):
        """"""
        mock_response = mockrequests.return_value
        mock_response.json.return_value = payload

        result = get_json(test_url)

        mockrequests.assert_called_once_with(test_url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """mock a method"""
    class TestClass:

        def a_method(self):
            """to mock a_method. Test that when calling a_property twice"""
            return 42

        @memoize
        def a_property(self):
            """mock a method"""
            return self.a_method()

    @patch.object(TestClass, "a_method")
    def test_memoize(self, mockmethod):
        """to mock a_method. Test that when calling a_property twice"""
        test = self.TestClass()

        test.a_property()
        test.a_property()

        mockmethod.assert_called_once()


if __name__ == "__main__":
    unittest.main()
