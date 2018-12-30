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
from firefly_iii_client.api.budgets_api import BudgetsApi  # noqa: E501
from firefly_iii_client.rest import ApiException


class TestBudgetsApi(unittest.TestCase):
    """BudgetsApi unit test stubs"""

    def setUp(self):
        self.api = firefly_iii_client.api.budgets_api.BudgetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_budget(self):
        """Test case for delete_budget

        Delete a budget.  # noqa: E501
        """
        pass

    def test_delete_budget_limit(self):
        """Test case for delete_budget_limit

        Delete a budget limit.  # noqa: E501
        """
        pass

    def test_get_budget(self):
        """Test case for get_budget

        Get a single budget.  # noqa: E501
        """
        pass

    def test_get_budget_limit(self):
        """Test case for get_budget_limit

        Get single budget limit.  # noqa: E501
        """
        pass

    def test_get_budget_limits(self):
        """Test case for get_budget_limits

        Get all limits  # noqa: E501
        """
        pass

    def test_get_budgets(self):
        """Test case for get_budgets

        List all budgets.  # noqa: E501
        """
        pass

    def test_get_transactions_by_budget(self):
        """Test case for get_transactions_by_budget

        All transactions to a budget.  # noqa: E501
        """
        pass

    def test_get_transactions_by_budget_limit(self):
        """Test case for get_transactions_by_budget_limit

        List all transactions by a budget limit ID.  # noqa: E501
        """
        pass

    def test_store_budget(self):
        """Test case for store_budget

        Store a new budget  # noqa: E501
        """
        pass

    def test_store_budget_limit(self):
        """Test case for store_budget_limit

        Store new budget limit.  # noqa: E501
        """
        pass

    def test_update_budget(self):
        """Test case for update_budget

        Update existing budget.  # noqa: E501
        """
        pass

    def test_update_budget_limit(self):
        """Test case for update_budget_limit

        Update existing budget limit.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
