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


class RecurrenceAttributes(object):
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
        'active': 'bool',
        'apply_rules': 'bool',
        'created_at': 'datetime',
        'description': 'str',
        'first_date': 'date',
        'latest_date': 'date',
        'meta': 'list[RecurrenceMeta]',
        'notes': 'str',
        'recurrence_repetitions': 'list[RecurrenceRepetition]',
        'repeat_until': 'date',
        'repetitions': 'int',
        'title': 'str',
        'transaction_type': 'str',
        'transaction_type_id': 'int',
        'transactions': 'list[RecurrenceTransaction]',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'apply_rules': 'apply_rules',
        'created_at': 'created_at',
        'description': 'description',
        'first_date': 'first_date',
        'latest_date': 'latest_date',
        'meta': 'meta',
        'notes': 'notes',
        'recurrence_repetitions': 'recurrence_repetitions',
        'repeat_until': 'repeat_until',
        'repetitions': 'repetitions',
        'title': 'title',
        'transaction_type': 'transaction_type',
        'transaction_type_id': 'transaction_type_id',
        'transactions': 'transactions',
        'updated_at': 'updated_at'
    }

    def __init__(self, active=None, apply_rules=None, created_at=None, description=None, first_date=None, latest_date=None, meta=None, notes=None, recurrence_repetitions=None, repeat_until=None, repetitions=None, title=None, transaction_type=None, transaction_type_id=None, transactions=None, updated_at=None):  # noqa: E501
        """RecurrenceAttributes - a model defined in OpenAPI"""  # noqa: E501

        self._active = None
        self._apply_rules = None
        self._created_at = None
        self._description = None
        self._first_date = None
        self._latest_date = None
        self._meta = None
        self._notes = None
        self._recurrence_repetitions = None
        self._repeat_until = None
        self._repetitions = None
        self._title = None
        self._transaction_type = None
        self._transaction_type_id = None
        self._transactions = None
        self._updated_at = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if apply_rules is not None:
            self.apply_rules = apply_rules
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if first_date is not None:
            self.first_date = first_date
        if latest_date is not None:
            self.latest_date = latest_date
        if meta is not None:
            self.meta = meta
        if notes is not None:
            self.notes = notes
        if recurrence_repetitions is not None:
            self.recurrence_repetitions = recurrence_repetitions
        if repeat_until is not None:
            self.repeat_until = repeat_until
        self.repetitions = repetitions
        if title is not None:
            self.title = title
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if transaction_type_id is not None:
            self.transaction_type_id = transaction_type_id
        if transactions is not None:
            self.transactions = transactions
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def active(self):
        """Gets the active of this RecurrenceAttributes.  # noqa: E501

        If the recurrence is even active.  # noqa: E501

        :return: The active of this RecurrenceAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this RecurrenceAttributes.

        If the recurrence is even active.  # noqa: E501

        :param active: The active of this RecurrenceAttributes.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def apply_rules(self):
        """Gets the apply_rules of this RecurrenceAttributes.  # noqa: E501

        If your rules will be applied when the recurrence fires.  # noqa: E501

        :return: The apply_rules of this RecurrenceAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._apply_rules

    @apply_rules.setter
    def apply_rules(self, apply_rules):
        """Sets the apply_rules of this RecurrenceAttributes.

        If your rules will be applied when the recurrence fires.  # noqa: E501

        :param apply_rules: The apply_rules of this RecurrenceAttributes.  # noqa: E501
        :type: bool
        """

        self._apply_rules = apply_rules

    @property
    def created_at(self):
        """Gets the created_at of this RecurrenceAttributes.  # noqa: E501


        :return: The created_at of this RecurrenceAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RecurrenceAttributes.


        :param created_at: The created_at of this RecurrenceAttributes.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this RecurrenceAttributes.  # noqa: E501


        :return: The description of this RecurrenceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RecurrenceAttributes.


        :param description: The description of this RecurrenceAttributes.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def first_date(self):
        """Gets the first_date of this RecurrenceAttributes.  # noqa: E501

        The first time this recurrence must fire.  # noqa: E501

        :return: The first_date of this RecurrenceAttributes.  # noqa: E501
        :rtype: date
        """
        return self._first_date

    @first_date.setter
    def first_date(self, first_date):
        """Sets the first_date of this RecurrenceAttributes.

        The first time this recurrence must fire.  # noqa: E501

        :param first_date: The first_date of this RecurrenceAttributes.  # noqa: E501
        :type: date
        """

        self._first_date = first_date

    @property
    def latest_date(self):
        """Gets the latest_date of this RecurrenceAttributes.  # noqa: E501

        The last time this recurrence fired.  # noqa: E501

        :return: The latest_date of this RecurrenceAttributes.  # noqa: E501
        :rtype: date
        """
        return self._latest_date

    @latest_date.setter
    def latest_date(self, latest_date):
        """Sets the latest_date of this RecurrenceAttributes.

        The last time this recurrence fired.  # noqa: E501

        :param latest_date: The latest_date of this RecurrenceAttributes.  # noqa: E501
        :type: date
        """

        self._latest_date = latest_date

    @property
    def meta(self):
        """Gets the meta of this RecurrenceAttributes.  # noqa: E501


        :return: The meta of this RecurrenceAttributes.  # noqa: E501
        :rtype: list[RecurrenceMeta]
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this RecurrenceAttributes.


        :param meta: The meta of this RecurrenceAttributes.  # noqa: E501
        :type: list[RecurrenceMeta]
        """

        self._meta = meta

    @property
    def notes(self):
        """Gets the notes of this RecurrenceAttributes.  # noqa: E501


        :return: The notes of this RecurrenceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this RecurrenceAttributes.


        :param notes: The notes of this RecurrenceAttributes.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def recurrence_repetitions(self):
        """Gets the recurrence_repetitions of this RecurrenceAttributes.  # noqa: E501


        :return: The recurrence_repetitions of this RecurrenceAttributes.  # noqa: E501
        :rtype: list[RecurrenceRepetition]
        """
        return self._recurrence_repetitions

    @recurrence_repetitions.setter
    def recurrence_repetitions(self, recurrence_repetitions):
        """Sets the recurrence_repetitions of this RecurrenceAttributes.


        :param recurrence_repetitions: The recurrence_repetitions of this RecurrenceAttributes.  # noqa: E501
        :type: list[RecurrenceRepetition]
        """

        self._recurrence_repetitions = recurrence_repetitions

    @property
    def repeat_until(self):
        """Gets the repeat_until of this RecurrenceAttributes.  # noqa: E501

        The date until which this recurrence will repeat itself.  # noqa: E501

        :return: The repeat_until of this RecurrenceAttributes.  # noqa: E501
        :rtype: date
        """
        return self._repeat_until

    @repeat_until.setter
    def repeat_until(self, repeat_until):
        """Sets the repeat_until of this RecurrenceAttributes.

        The date until which this recurrence will repeat itself.  # noqa: E501

        :param repeat_until: The repeat_until of this RecurrenceAttributes.  # noqa: E501
        :type: date
        """

        self._repeat_until = repeat_until

    @property
    def repetitions(self):
        """Gets the repetitions of this RecurrenceAttributes.  # noqa: E501

        How many transactions the recurrence will create, maximum.  # noqa: E501

        :return: The repetitions of this RecurrenceAttributes.  # noqa: E501
        :rtype: int
        """
        return self._repetitions

    @repetitions.setter
    def repetitions(self, repetitions):
        """Sets the repetitions of this RecurrenceAttributes.

        How many transactions the recurrence will create, maximum.  # noqa: E501

        :param repetitions: The repetitions of this RecurrenceAttributes.  # noqa: E501
        :type: int
        """

        self._repetitions = repetitions

    @property
    def title(self):
        """Gets the title of this RecurrenceAttributes.  # noqa: E501


        :return: The title of this RecurrenceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RecurrenceAttributes.


        :param title: The title of this RecurrenceAttributes.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def transaction_type(self):
        """Gets the transaction_type of this RecurrenceAttributes.  # noqa: E501

        The transaction that will be generated by the recurring transaction.  # noqa: E501

        :return: The transaction_type of this RecurrenceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this RecurrenceAttributes.

        The transaction that will be generated by the recurring transaction.  # noqa: E501

        :param transaction_type: The transaction_type of this RecurrenceAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["withdrawal", "transfer", "deposit", "opening-balance", "reconciliation"]  # noqa: E501
        if transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_type, allowed_values)
            )

        self._transaction_type = transaction_type

    @property
    def transaction_type_id(self):
        """Gets the transaction_type_id of this RecurrenceAttributes.  # noqa: E501


        :return: The transaction_type_id of this RecurrenceAttributes.  # noqa: E501
        :rtype: int
        """
        return self._transaction_type_id

    @transaction_type_id.setter
    def transaction_type_id(self, transaction_type_id):
        """Sets the transaction_type_id of this RecurrenceAttributes.


        :param transaction_type_id: The transaction_type_id of this RecurrenceAttributes.  # noqa: E501
        :type: int
        """

        self._transaction_type_id = transaction_type_id

    @property
    def transactions(self):
        """Gets the transactions of this RecurrenceAttributes.  # noqa: E501


        :return: The transactions of this RecurrenceAttributes.  # noqa: E501
        :rtype: list[RecurrenceTransaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this RecurrenceAttributes.


        :param transactions: The transactions of this RecurrenceAttributes.  # noqa: E501
        :type: list[RecurrenceTransaction]
        """

        self._transactions = transactions

    @property
    def updated_at(self):
        """Gets the updated_at of this RecurrenceAttributes.  # noqa: E501


        :return: The updated_at of this RecurrenceAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RecurrenceAttributes.


        :param updated_at: The updated_at of this RecurrenceAttributes.  # noqa: E501
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
        if not isinstance(other, RecurrenceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
