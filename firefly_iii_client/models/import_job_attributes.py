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


class ImportJobAttributes(object):
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
        'configuration': 'str',
        'created_at': 'datetime',
        'errors': 'str',
        'extended_status': 'str',
        'file_type': 'str',
        'key': 'str',
        'provider': 'str',
        'stage': 'str',
        'status': 'str',
        'tag_id': 'int',
        'tag_tag': 'str',
        'transactions': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'configuration': 'configuration',
        'created_at': 'created_at',
        'errors': 'errors',
        'extended_status': 'extended_status',
        'file_type': 'file_type',
        'key': 'key',
        'provider': 'provider',
        'stage': 'stage',
        'status': 'status',
        'tag_id': 'tag_id',
        'tag_tag': 'tag_tag',
        'transactions': 'transactions',
        'updated_at': 'updated_at'
    }

    def __init__(self, configuration=None, created_at=None, errors=None, extended_status=None, file_type=None, key=None, provider=None, stage=None, status=None, tag_id=None, tag_tag=None, transactions=None, updated_at=None):  # noqa: E501
        """ImportJobAttributes - a model defined in OpenAPI"""  # noqa: E501

        self._configuration = None
        self._created_at = None
        self._errors = None
        self._extended_status = None
        self._file_type = None
        self._key = None
        self._provider = None
        self._stage = None
        self._status = None
        self._tag_id = None
        self._tag_tag = None
        self._transactions = None
        self._updated_at = None
        self.discriminator = None

        if configuration is not None:
            self.configuration = configuration
        if created_at is not None:
            self.created_at = created_at
        if errors is not None:
            self.errors = errors
        if extended_status is not None:
            self.extended_status = extended_status
        if file_type is not None:
            self.file_type = file_type
        if key is not None:
            self.key = key
        if provider is not None:
            self.provider = provider
        if stage is not None:
            self.stage = stage
        if status is not None:
            self.status = status
        if tag_id is not None:
            self.tag_id = tag_id
        if tag_tag is not None:
            self.tag_tag = tag_tag
        if transactions is not None:
            self.transactions = transactions
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def configuration(self):
        """Gets the configuration of this ImportJobAttributes.  # noqa: E501

        JSON string with job-specific configuration.  # noqa: E501

        :return: The configuration of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ImportJobAttributes.

        JSON string with job-specific configuration.  # noqa: E501

        :param configuration: The configuration of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def created_at(self):
        """Gets the created_at of this ImportJobAttributes.  # noqa: E501


        :return: The created_at of this ImportJobAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ImportJobAttributes.


        :param created_at: The created_at of this ImportJobAttributes.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def errors(self):
        """Gets the errors of this ImportJobAttributes.  # noqa: E501

        JSON string with a list of errors.  # noqa: E501

        :return: The errors of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ImportJobAttributes.

        JSON string with a list of errors.  # noqa: E501

        :param errors: The errors of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._errors = errors

    @property
    def extended_status(self):
        """Gets the extended_status of this ImportJobAttributes.  # noqa: E501

        JSON string with job-specific status.  # noqa: E501

        :return: The extended_status of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._extended_status

    @extended_status.setter
    def extended_status(self, extended_status):
        """Sets the extended_status of this ImportJobAttributes.

        JSON string with job-specific status.  # noqa: E501

        :param extended_status: The extended_status of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._extended_status = extended_status

    @property
    def file_type(self):
        """Gets the file_type of this ImportJobAttributes.  # noqa: E501

        File type, if relevant.  # noqa: E501

        :return: The file_type of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ImportJobAttributes.

        File type, if relevant.  # noqa: E501

        :param file_type: The file_type of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def key(self):
        """Gets the key of this ImportJobAttributes.  # noqa: E501

        Import job unique identifier.  # noqa: E501

        :return: The key of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ImportJobAttributes.

        Import job unique identifier.  # noqa: E501

        :param key: The key of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def provider(self):
        """Gets the provider of this ImportJobAttributes.  # noqa: E501

        Import provider that did the import.  # noqa: E501

        :return: The provider of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ImportJobAttributes.

        Import provider that did the import.  # noqa: E501

        :param provider: The provider of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def stage(self):
        """Gets the stage of this ImportJobAttributes.  # noqa: E501

        Current stage.  # noqa: E501

        :return: The stage of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this ImportJobAttributes.

        Current stage.  # noqa: E501

        :param stage: The stage of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._stage = stage

    @property
    def status(self):
        """Gets the status of this ImportJobAttributes.  # noqa: E501

        Status of import job.  # noqa: E501

        :return: The status of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImportJobAttributes.

        Status of import job.  # noqa: E501

        :param status: The status of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tag_id(self):
        """Gets the tag_id of this ImportJobAttributes.  # noqa: E501

        ID of the tag related to the import job, if present.  # noqa: E501

        :return: The tag_id of this ImportJobAttributes.  # noqa: E501
        :rtype: int
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this ImportJobAttributes.

        ID of the tag related to the import job, if present.  # noqa: E501

        :param tag_id: The tag_id of this ImportJobAttributes.  # noqa: E501
        :type: int
        """

        self._tag_id = tag_id

    @property
    def tag_tag(self):
        """Gets the tag_tag of this ImportJobAttributes.  # noqa: E501

        Tag related to the import job, if present.  # noqa: E501

        :return: The tag_tag of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._tag_tag

    @tag_tag.setter
    def tag_tag(self, tag_tag):
        """Sets the tag_tag of this ImportJobAttributes.

        Tag related to the import job, if present.  # noqa: E501

        :param tag_tag: The tag_tag of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._tag_tag = tag_tag

    @property
    def transactions(self):
        """Gets the transactions of this ImportJobAttributes.  # noqa: E501

        JSON string with a count of transactions in the job.  # noqa: E501

        :return: The transactions of this ImportJobAttributes.  # noqa: E501
        :rtype: str
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this ImportJobAttributes.

        JSON string with a count of transactions in the job.  # noqa: E501

        :param transactions: The transactions of this ImportJobAttributes.  # noqa: E501
        :type: str
        """

        self._transactions = transactions

    @property
    def updated_at(self):
        """Gets the updated_at of this ImportJobAttributes.  # noqa: E501


        :return: The updated_at of this ImportJobAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ImportJobAttributes.


        :param updated_at: The updated_at of this ImportJobAttributes.  # noqa: E501
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
        if not isinstance(other, ImportJobAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
