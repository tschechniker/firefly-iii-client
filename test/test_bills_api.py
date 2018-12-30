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
from firefly_iii_client.api.bills_api import BillsApi  # noqa: E501
from firefly_iii_client.rest import ApiException


class TestBillsApi(unittest.TestCase):
    """BillsApi unit test stubs"""

    def setUp(self):
        self.api = firefly_iii_client.api.bills_api.BillsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_bill(self):
        """Test case for delete_bill

        Delete a bill.  # noqa: E501
        """
        pass

    def test_get_attachments_by_bill(self):
        """Test case for get_attachments_by_bill

        List all attachments uploaded to the bill.  # noqa: E501
        """
        pass

    def test_get_bill(self):
        """Test case for get_bill

        Get a single bill.  # noqa: E501
        """
        pass

    def test_get_bills(self):
        """Test case for get_bills

        List all bills.  # noqa: E501
        """
        pass

    def test_get_rules_by_bill(self):
        """Test case for get_rules_by_bill

        List all rules associated with the bill.  # noqa: E501
        """
        pass

    def test_get_transactions_by_bill(self):
        """Test case for get_transactions_by_bill

        List all transactions associated with the  bill.  # noqa: E501
        """
        pass

    def test_store_bill(self):
        """Test case for store_bill

        Store a new bill  # noqa: E501
        """
        pass

    def test_update_bill(self):
        """Test case for update_bill

        Update existing bill.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
