# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import firefly_iii_client
from firefly_iii_client.api.users_api import UsersApi  # noqa: E501
from firefly_iii_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = firefly_iii_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete a user.  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get a single user.  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        List all users.  # noqa: E501
        """
        pass

    def test_store_user(self):
        """Test case for store_user

        Store a new user  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update an existing user's information.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
