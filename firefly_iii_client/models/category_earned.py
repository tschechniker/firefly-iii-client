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


class CategoryEarned(object):
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
        'currency_code': 'str',
        'currency_decimal_places': 'int',
        'currency_id': 'int',
        'currency_symbol': 'str',
        'end': 'date',
        'start': 'date'
    }

    attribute_map = {
        'amount': 'amount',
        'currency_code': 'currency_code',
        'currency_decimal_places': 'currency_decimal_places',
        'currency_id': 'currency_id',
        'currency_symbol': 'currency_symbol',
        'end': 'end',
        'start': 'start'
    }

    def __init__(self, amount=None, currency_code=None, currency_decimal_places=None, currency_id=None, currency_symbol=None, end=None, start=None):  # noqa: E501
        """CategoryEarned - a model defined in OpenAPI"""  # noqa: E501

        self._amount = None
        self._currency_code = None
        self._currency_decimal_places = None
        self._currency_id = None
        self._currency_symbol = None
        self._end = None
        self._start = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
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
        if start is not None:
            self.start = start

    @property
    def amount(self):
        """Gets the amount of this CategoryEarned.  # noqa: E501

        The amount earned.  # noqa: E501

        :return: The amount of this CategoryEarned.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CategoryEarned.

        The amount earned.  # noqa: E501

        :param amount: The amount of this CategoryEarned.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency_code(self):
        """Gets the currency_code of this CategoryEarned.  # noqa: E501


        :return: The currency_code of this CategoryEarned.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CategoryEarned.


        :param currency_code: The currency_code of this CategoryEarned.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_decimal_places(self):
        """Gets the currency_decimal_places of this CategoryEarned.  # noqa: E501

        Number of decimals supported by the currency  # noqa: E501

        :return: The currency_decimal_places of this CategoryEarned.  # noqa: E501
        :rtype: int
        """
        return self._currency_decimal_places

    @currency_decimal_places.setter
    def currency_decimal_places(self, currency_decimal_places):
        """Sets the currency_decimal_places of this CategoryEarned.

        Number of decimals supported by the currency  # noqa: E501

        :param currency_decimal_places: The currency_decimal_places of this CategoryEarned.  # noqa: E501
        :type: int
        """

        self._currency_decimal_places = currency_decimal_places

    @property
    def currency_id(self):
        """Gets the currency_id of this CategoryEarned.  # noqa: E501


        :return: The currency_id of this CategoryEarned.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this CategoryEarned.


        :param currency_id: The currency_id of this CategoryEarned.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this CategoryEarned.  # noqa: E501


        :return: The currency_symbol of this CategoryEarned.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this CategoryEarned.


        :param currency_symbol: The currency_symbol of this CategoryEarned.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def end(self):
        """Gets the end of this CategoryEarned.  # noqa: E501


        :return: The end of this CategoryEarned.  # noqa: E501
        :rtype: date
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this CategoryEarned.


        :param end: The end of this CategoryEarned.  # noqa: E501
        :type: date
        """

        self._end = end

    @property
    def start(self):
        """Gets the start of this CategoryEarned.  # noqa: E501


        :return: The start of this CategoryEarned.  # noqa: E501
        :rtype: date
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this CategoryEarned.


        :param start: The start of this CategoryEarned.  # noqa: E501
        :type: date
        """

        self._start = start

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
        if not isinstance(other, CategoryEarned):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
