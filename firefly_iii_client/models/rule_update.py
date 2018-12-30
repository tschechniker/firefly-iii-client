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


class RuleUpdate(object):
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
        'actions': 'list[RuleActionUpdate]',
        'active': 'bool',
        'description': 'str',
        'rule_group_id': 'int',
        'rule_group_title': 'str',
        'stop_processing': 'bool',
        'strict': 'bool',
        'title': 'str',
        'trigger': 'str',
        'triggers': 'list[RuleTriggerUpdate]'
    }

    attribute_map = {
        'actions': 'actions',
        'active': 'active',
        'description': 'description',
        'rule_group_id': 'rule_group_id',
        'rule_group_title': 'rule_group_title',
        'stop_processing': 'stop_processing',
        'strict': 'strict',
        'title': 'title',
        'trigger': 'trigger',
        'triggers': 'triggers'
    }

    def __init__(self, actions=None, active=None, description=None, rule_group_id=None, rule_group_title=None, stop_processing=None, strict=None, title=None, trigger=None, triggers=None):  # noqa: E501
        """RuleUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._actions = None
        self._active = None
        self._description = None
        self._rule_group_id = None
        self._rule_group_title = None
        self._stop_processing = None
        self._strict = None
        self._title = None
        self._trigger = None
        self._triggers = None
        self.discriminator = None

        self.actions = actions
        if active is not None:
            self.active = active
        if description is not None:
            self.description = description
        self.rule_group_id = rule_group_id
        if rule_group_title is not None:
            self.rule_group_title = rule_group_title
        if stop_processing is not None:
            self.stop_processing = stop_processing
        if strict is not None:
            self.strict = strict
        self.title = title
        self.trigger = trigger
        self.triggers = triggers

    @property
    def actions(self):
        """Gets the actions of this RuleUpdate.  # noqa: E501


        :return: The actions of this RuleUpdate.  # noqa: E501
        :rtype: list[RuleActionUpdate]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this RuleUpdate.


        :param actions: The actions of this RuleUpdate.  # noqa: E501
        :type: list[RuleActionUpdate]
        """
        if actions is None:
            raise ValueError("Invalid value for `actions`, must not be `None`")  # noqa: E501

        self._actions = actions

    @property
    def active(self):
        """Gets the active of this RuleUpdate.  # noqa: E501

        Whether or not the rule is even active. Default is true.  # noqa: E501

        :return: The active of this RuleUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this RuleUpdate.

        Whether or not the rule is even active. Default is true.  # noqa: E501

        :param active: The active of this RuleUpdate.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def description(self):
        """Gets the description of this RuleUpdate.  # noqa: E501


        :return: The description of this RuleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleUpdate.


        :param description: The description of this RuleUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rule_group_id(self):
        """Gets the rule_group_id of this RuleUpdate.  # noqa: E501

        ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory.  # noqa: E501

        :return: The rule_group_id of this RuleUpdate.  # noqa: E501
        :rtype: int
        """
        return self._rule_group_id

    @rule_group_id.setter
    def rule_group_id(self, rule_group_id):
        """Sets the rule_group_id of this RuleUpdate.

        ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory.  # noqa: E501

        :param rule_group_id: The rule_group_id of this RuleUpdate.  # noqa: E501
        :type: int
        """
        if rule_group_id is None:
            raise ValueError("Invalid value for `rule_group_id`, must not be `None`")  # noqa: E501

        self._rule_group_id = rule_group_id

    @property
    def rule_group_title(self):
        """Gets the rule_group_title of this RuleUpdate.  # noqa: E501

        Title of the rule group under which the rule must be stored. Either this field or rule_group_id is mandatory.  # noqa: E501

        :return: The rule_group_title of this RuleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._rule_group_title

    @rule_group_title.setter
    def rule_group_title(self, rule_group_title):
        """Sets the rule_group_title of this RuleUpdate.

        Title of the rule group under which the rule must be stored. Either this field or rule_group_id is mandatory.  # noqa: E501

        :param rule_group_title: The rule_group_title of this RuleUpdate.  # noqa: E501
        :type: str
        """

        self._rule_group_title = rule_group_title

    @property
    def stop_processing(self):
        """Gets the stop_processing of this RuleUpdate.  # noqa: E501

        If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false.  # noqa: E501

        :return: The stop_processing of this RuleUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._stop_processing

    @stop_processing.setter
    def stop_processing(self, stop_processing):
        """Sets the stop_processing of this RuleUpdate.

        If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false.  # noqa: E501

        :param stop_processing: The stop_processing of this RuleUpdate.  # noqa: E501
        :type: bool
        """

        self._stop_processing = stop_processing

    @property
    def strict(self):
        """Gets the strict of this RuleUpdate.  # noqa: E501

        If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true.  # noqa: E501

        :return: The strict of this RuleUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._strict

    @strict.setter
    def strict(self, strict):
        """Sets the strict of this RuleUpdate.

        If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true.  # noqa: E501

        :param strict: The strict of this RuleUpdate.  # noqa: E501
        :type: bool
        """

        self._strict = strict

    @property
    def title(self):
        """Gets the title of this RuleUpdate.  # noqa: E501


        :return: The title of this RuleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RuleUpdate.


        :param title: The title of this RuleUpdate.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def trigger(self):
        """Gets the trigger of this RuleUpdate.  # noqa: E501

        Which action is necessary for the rule to fire? Use either store-journal or update-journal.  # noqa: E501

        :return: The trigger of this RuleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this RuleUpdate.

        Which action is necessary for the rule to fire? Use either store-journal or update-journal.  # noqa: E501

        :param trigger: The trigger of this RuleUpdate.  # noqa: E501
        :type: str
        """
        if trigger is None:
            raise ValueError("Invalid value for `trigger`, must not be `None`")  # noqa: E501
        allowed_values = ["store-journal", "update-journal"]  # noqa: E501
        if trigger not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger, allowed_values)
            )

        self._trigger = trigger

    @property
    def triggers(self):
        """Gets the triggers of this RuleUpdate.  # noqa: E501


        :return: The triggers of this RuleUpdate.  # noqa: E501
        :rtype: list[RuleTriggerUpdate]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this RuleUpdate.


        :param triggers: The triggers of this RuleUpdate.  # noqa: E501
        :type: list[RuleTriggerUpdate]
        """
        if triggers is None:
            raise ValueError("Invalid value for `triggers`, must not be `None`")  # noqa: E501

        self._triggers = triggers

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
        if not isinstance(other, RuleUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
