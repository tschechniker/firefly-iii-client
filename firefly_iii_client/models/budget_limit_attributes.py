# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BudgetLimitAttributes(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'amount': 'float',
        'budget_id': 'int',
        'created_at': 'datetime',
        'currency_code': 'str',
        'currency_decimal_places': 'int',
        'currency_id': 'int',
        'currency_symbol': 'str',
        'end': 'date',
        'spent': 'list[BudgetSpent]',
        'start': 'date',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'amount': 'amount',
        'budget_id': 'budget_id',
        'created_at': 'created_at',
        'currency_code': 'currency_code',
        'currency_decimal_places': 'currency_decimal_places',
        'currency_id': 'currency_id',
        'currency_symbol': 'currency_symbol',
        'end': 'end',
        'spent': 'spent',
        'start': 'start',
        'updated_at': 'updated_at'
    }

    def __init__(self, amount=None, budget_id=None, created_at=None, currency_code=None, currency_decimal_places=None, currency_id=None, currency_symbol=None, end=None, spent=None, start=None, updated_at=None):  # noqa: E501
        """BudgetLimitAttributes - a model defined in OpenAPI"""  # noqa: E501

        self._amount = None
        self._budget_id = None
        self._created_at = None
        self._currency_code = None
        self._currency_decimal_places = None
        self._currency_id = None
        self._currency_symbol = None
        self._end = None
        self._spent = None
        self._start = None
        self._updated_at = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if budget_id is not None:
            self.budget_id = budget_id
        if created_at is not None:
            self.created_at = created_at
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_decimal_places is not None:
            self.currency_decimal_places = currency_decimal_places
        if currency_id is not None:
            self.currency_id = currency_id
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        if end is not None:
            self.end = end
        if spent is not None:
            self.spent = spent
        if start is not None:
            self.start = start
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def amount(self):
        """Gets the amount of this BudgetLimitAttributes.  # noqa: E501


        :return: The amount of this BudgetLimitAttributes.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BudgetLimitAttributes.


        :param amount: The amount of this BudgetLimitAttributes.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def budget_id(self):
        """Gets the budget_id of this BudgetLimitAttributes.  # noqa: E501


        :return: The budget_id of this BudgetLimitAttributes.  # noqa: E501
        :rtype: int
        """
        return self._budget_id

    @budget_id.setter
    def budget_id(self, budget_id):
        """Sets the budget_id of this BudgetLimitAttributes.


        :param budget_id: The budget_id of this BudgetLimitAttributes.  # noqa: E501
        :type: int
        """

        self._budget_id = budget_id

    @property
    def created_at(self):
        """Gets the created_at of this BudgetLimitAttributes.  # noqa: E501


        :return: The created_at of this BudgetLimitAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BudgetLimitAttributes.


        :param created_at: The created_at of this BudgetLimitAttributes.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def currency_code(self):
        """Gets the currency_code of this BudgetLimitAttributes.  # noqa: E501


        :return: The currency_code of this BudgetLimitAttributes.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this BudgetLimitAttributes.


        :param currency_code: The currency_code of this BudgetLimitAttributes.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_decimal_places(self):
        """Gets the currency_decimal_places of this BudgetLimitAttributes.  # noqa: E501


        :return: The currency_decimal_places of this BudgetLimitAttributes.  # noqa: E501
        :rtype: int
        """
        return self._currency_decimal_places

    @currency_decimal_places.setter
    def currency_decimal_places(self, currency_decimal_places):
        """Sets the currency_decimal_places of this BudgetLimitAttributes.


        :param currency_decimal_places: The currency_decimal_places of this BudgetLimitAttributes.  # noqa: E501
        :type: int
        """

        self._currency_decimal_places = currency_decimal_places

    @property
    def currency_id(self):
        """Gets the currency_id of this BudgetLimitAttributes.  # noqa: E501


        :return: The currency_id of this BudgetLimitAttributes.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this BudgetLimitAttributes.


        :param currency_id: The currency_id of this BudgetLimitAttributes.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this BudgetLimitAttributes.  # noqa: E501


        :return: The currency_symbol of this BudgetLimitAttributes.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this BudgetLimitAttributes.


        :param currency_symbol: The currency_symbol of this BudgetLimitAttributes.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def end(self):
        """Gets the end of this BudgetLimitAttributes.  # noqa: E501

        End date of the budget limit.  # noqa: E501

        :return: The end of this BudgetLimitAttributes.  # noqa: E501
        :rtype: date
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this BudgetLimitAttributes.

        End date of the budget limit.  # noqa: E501

        :param end: The end of this BudgetLimitAttributes.  # noqa: E501
        :type: date
        """

        self._end = end

    @property
    def spent(self):
        """Gets the spent of this BudgetLimitAttributes.  # noqa: E501


        :return: The spent of this BudgetLimitAttributes.  # noqa: E501
        :rtype: list[BudgetSpent]
        """
        return self._spent

    @spent.setter
    def spent(self, spent):
        """Sets the spent of this BudgetLimitAttributes.


        :param spent: The spent of this BudgetLimitAttributes.  # noqa: E501
        :type: list[BudgetSpent]
        """

        self._spent = spent

    @property
    def start(self):
        """Gets the start of this BudgetLimitAttributes.  # noqa: E501

        Start date of the budget limit.  # noqa: E501

        :return: The start of this BudgetLimitAttributes.  # noqa: E501
        :rtype: date
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this BudgetLimitAttributes.

        Start date of the budget limit.  # noqa: E501

        :param start: The start of this BudgetLimitAttributes.  # noqa: E501
        :type: date
        """

        self._start = start

    @property
    def updated_at(self):
        """Gets the updated_at of this BudgetLimitAttributes.  # noqa: E501


        :return: The updated_at of this BudgetLimitAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BudgetLimitAttributes.


        :param updated_at: The updated_at of this BudgetLimitAttributes.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BudgetLimitAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
