"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from firefly_iii_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from firefly_iii_client.exceptions import ApiAttributeError



class TransactionSplitUpdate(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'amount': (str,),  # noqa: E501
            'bill_id': (str, none_type,),  # noqa: E501
            'bill_name': (str, none_type,),  # noqa: E501
            'book_date': (datetime, none_type,),  # noqa: E501
            'budget_id': (str, none_type,),  # noqa: E501
            'budget_name': (str, none_type,),  # noqa: E501
            'bunq_payment_id': (str, none_type,),  # noqa: E501
            'category_id': (str, none_type,),  # noqa: E501
            'category_name': (str, none_type,),  # noqa: E501
            'currency_code': (str, none_type,),  # noqa: E501
            'currency_decimal_places': (int,),  # noqa: E501
            'currency_id': (str, none_type,),  # noqa: E501
            'currency_name': (str,),  # noqa: E501
            'currency_symbol': (str,),  # noqa: E501
            'date': (datetime,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'destination_iban': (str, none_type,),  # noqa: E501
            'destination_id': (str, none_type,),  # noqa: E501
            'destination_name': (str, none_type,),  # noqa: E501
            'due_date': (datetime, none_type,),  # noqa: E501
            'external_id': (str, none_type,),  # noqa: E501
            'external_url': (str, none_type,),  # noqa: E501
            'foreign_amount': (str, none_type,),  # noqa: E501
            'foreign_currency_code': (str, none_type,),  # noqa: E501
            'foreign_currency_decimal_places': (int, none_type,),  # noqa: E501
            'foreign_currency_id': (str, none_type,),  # noqa: E501
            'foreign_currency_symbol': (str, none_type,),  # noqa: E501
            'interest_date': (datetime, none_type,),  # noqa: E501
            'internal_reference': (str, none_type,),  # noqa: E501
            'invoice_date': (datetime, none_type,),  # noqa: E501
            'notes': (str, none_type,),  # noqa: E501
            'order': (int, none_type,),  # noqa: E501
            'payment_date': (datetime, none_type,),  # noqa: E501
            'process_date': (datetime, none_type,),  # noqa: E501
            'reconciled': (bool,),  # noqa: E501
            'sepa_batch_id': (str, none_type,),  # noqa: E501
            'sepa_cc': (str, none_type,),  # noqa: E501
            'sepa_ci': (str, none_type,),  # noqa: E501
            'sepa_country': (str, none_type,),  # noqa: E501
            'sepa_ct_id': (str, none_type,),  # noqa: E501
            'sepa_ct_op': (str, none_type,),  # noqa: E501
            'sepa_db': (str, none_type,),  # noqa: E501
            'sepa_ep': (str, none_type,),  # noqa: E501
            'source_iban': (str, none_type,),  # noqa: E501
            'source_id': (str, none_type,),  # noqa: E501
            'source_name': (str, none_type,),  # noqa: E501
            'tags': ([str], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'amount': 'amount',  # noqa: E501
        'bill_id': 'bill_id',  # noqa: E501
        'bill_name': 'bill_name',  # noqa: E501
        'book_date': 'book_date',  # noqa: E501
        'budget_id': 'budget_id',  # noqa: E501
        'budget_name': 'budget_name',  # noqa: E501
        'bunq_payment_id': 'bunq_payment_id',  # noqa: E501
        'category_id': 'category_id',  # noqa: E501
        'category_name': 'category_name',  # noqa: E501
        'currency_code': 'currency_code',  # noqa: E501
        'currency_decimal_places': 'currency_decimal_places',  # noqa: E501
        'currency_id': 'currency_id',  # noqa: E501
        'currency_name': 'currency_name',  # noqa: E501
        'currency_symbol': 'currency_symbol',  # noqa: E501
        'date': 'date',  # noqa: E501
        'description': 'description',  # noqa: E501
        'destination_iban': 'destination_iban',  # noqa: E501
        'destination_id': 'destination_id',  # noqa: E501
        'destination_name': 'destination_name',  # noqa: E501
        'due_date': 'due_date',  # noqa: E501
        'external_id': 'external_id',  # noqa: E501
        'external_url': 'external_url',  # noqa: E501
        'foreign_amount': 'foreign_amount',  # noqa: E501
        'foreign_currency_code': 'foreign_currency_code',  # noqa: E501
        'foreign_currency_decimal_places': 'foreign_currency_decimal_places',  # noqa: E501
        'foreign_currency_id': 'foreign_currency_id',  # noqa: E501
        'foreign_currency_symbol': 'foreign_currency_symbol',  # noqa: E501
        'interest_date': 'interest_date',  # noqa: E501
        'internal_reference': 'internal_reference',  # noqa: E501
        'invoice_date': 'invoice_date',  # noqa: E501
        'notes': 'notes',  # noqa: E501
        'order': 'order',  # noqa: E501
        'payment_date': 'payment_date',  # noqa: E501
        'process_date': 'process_date',  # noqa: E501
        'reconciled': 'reconciled',  # noqa: E501
        'sepa_batch_id': 'sepa_batch_id',  # noqa: E501
        'sepa_cc': 'sepa_cc',  # noqa: E501
        'sepa_ci': 'sepa_ci',  # noqa: E501
        'sepa_country': 'sepa_country',  # noqa: E501
        'sepa_ct_id': 'sepa_ct_id',  # noqa: E501
        'sepa_ct_op': 'sepa_ct_op',  # noqa: E501
        'sepa_db': 'sepa_db',  # noqa: E501
        'sepa_ep': 'sepa_ep',  # noqa: E501
        'source_iban': 'source_iban',  # noqa: E501
        'source_id': 'source_id',  # noqa: E501
        'source_name': 'source_name',  # noqa: E501
        'tags': 'tags',  # noqa: E501
    }

    read_only_vars = {
        'budget_name',  # noqa: E501
        'currency_decimal_places',  # noqa: E501
        'currency_name',  # noqa: E501
        'currency_symbol',  # noqa: E501
        'foreign_currency_decimal_places',  # noqa: E501
        'foreign_currency_symbol',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """TransactionSplitUpdate - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            amount (str): Amount of the transaction.. [optional]  # noqa: E501
            bill_id (str, none_type): Optional. Use either this or the bill_name. [optional]  # noqa: E501
            bill_name (str, none_type): Optional. Use either this or the bill_id. [optional]  # noqa: E501
            book_date (datetime, none_type): [optional]  # noqa: E501
            budget_id (str, none_type): The budget ID for this transaction.. [optional]  # noqa: E501
            budget_name (str, none_type): The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored.. [optional]  # noqa: E501
            bunq_payment_id (str, none_type): Internal ID of bunq transaction.. [optional]  # noqa: E501
            category_id (str, none_type): The category ID for this transaction.. [optional]  # noqa: E501
            category_name (str, none_type): The name of the category to be used. If the category is unknown, it will be created. If the ID and the name point to different categories, the ID overrules the name.. [optional]  # noqa: E501
            currency_code (str, none_type): Currency code. Default is the source account's currency, or the user's default currency. Can be used instead of currency_id.. [optional]  # noqa: E501
            currency_decimal_places (int): Number of decimals used in this currency.. [optional]  # noqa: E501
            currency_id (str, none_type): Currency ID. Default is the source account's currency, or the user's default currency. Can be used instead of currency_code.. [optional]  # noqa: E501
            currency_name (str): [optional]  # noqa: E501
            currency_symbol (str): [optional]  # noqa: E501
            date (datetime): Date of the transaction. [optional]  # noqa: E501
            description (str): Description of the transaction.. [optional]  # noqa: E501
            destination_iban (str, none_type): [optional]  # noqa: E501
            destination_id (str, none_type): ID of the destination account. For a deposit or a transfer, this must always be an asset account. For withdrawals this must be an expense account.. [optional]  # noqa: E501
            destination_name (str, none_type): Name of the destination account. You can submit the name instead of the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is enough.. [optional]  # noqa: E501
            due_date (datetime, none_type): [optional]  # noqa: E501
            external_id (str, none_type): Reference to external ID in other systems.. [optional]  # noqa: E501
            external_url (str, none_type): External, custom URL for this transaction.. [optional]  # noqa: E501
            foreign_amount (str, none_type): The amount in a foreign currency.. [optional]  # noqa: E501
            foreign_currency_code (str, none_type): Currency code of the foreign currency. Default is NULL. Can be used instead of the foreign_currency_id, but this or the ID is required when submitting a foreign amount.. [optional]  # noqa: E501
            foreign_currency_decimal_places (int, none_type): Number of decimals in the currency. [optional]  # noqa: E501
            foreign_currency_id (str, none_type): Currency ID of the foreign currency. Default is null. Is required when you submit a foreign amount.. [optional]  # noqa: E501
            foreign_currency_symbol (str, none_type): [optional]  # noqa: E501
            interest_date (datetime, none_type): [optional]  # noqa: E501
            internal_reference (str, none_type): Reference to internal reference of other systems.. [optional]  # noqa: E501
            invoice_date (datetime, none_type): [optional]  # noqa: E501
            notes (str, none_type): [optional]  # noqa: E501
            order (int, none_type): Order of this entry in the list of transactions.. [optional]  # noqa: E501
            payment_date (datetime, none_type): [optional]  # noqa: E501
            process_date (datetime, none_type): [optional]  # noqa: E501
            reconciled (bool): If the transaction has been reconciled already. When you set this, the amount can no longer be edited by the user.. [optional]  # noqa: E501
            sepa_batch_id (str, none_type): SEPA Batch ID. [optional]  # noqa: E501
            sepa_cc (str, none_type): SEPA Clearing Code. [optional]  # noqa: E501
            sepa_ci (str, none_type): SEPA Creditor Identifier. [optional]  # noqa: E501
            sepa_country (str, none_type): SEPA Country. [optional]  # noqa: E501
            sepa_ct_id (str, none_type): SEPA end-to-end Identifier. [optional]  # noqa: E501
            sepa_ct_op (str, none_type): SEPA Opposing Account Identifier. [optional]  # noqa: E501
            sepa_db (str, none_type): SEPA mandate identifier. [optional]  # noqa: E501
            sepa_ep (str, none_type): SEPA External Purpose indicator. [optional]  # noqa: E501
            source_iban (str, none_type): [optional]  # noqa: E501
            source_id (str, none_type): ID of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account.. [optional]  # noqa: E501
            source_name (str, none_type): Name of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id. If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on the name.. [optional]  # noqa: E501
            tags ([str], none_type): Array of tags.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """TransactionSplitUpdate - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            amount (str): Amount of the transaction.. [optional]  # noqa: E501
            bill_id (str, none_type): Optional. Use either this or the bill_name. [optional]  # noqa: E501
            bill_name (str, none_type): Optional. Use either this or the bill_id. [optional]  # noqa: E501
            book_date (datetime, none_type): [optional]  # noqa: E501
            budget_id (str, none_type): The budget ID for this transaction.. [optional]  # noqa: E501
            budget_name (str, none_type): The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored.. [optional]  # noqa: E501
            bunq_payment_id (str, none_type): Internal ID of bunq transaction.. [optional]  # noqa: E501
            category_id (str, none_type): The category ID for this transaction.. [optional]  # noqa: E501
            category_name (str, none_type): The name of the category to be used. If the category is unknown, it will be created. If the ID and the name point to different categories, the ID overrules the name.. [optional]  # noqa: E501
            currency_code (str, none_type): Currency code. Default is the source account's currency, or the user's default currency. Can be used instead of currency_id.. [optional]  # noqa: E501
            currency_decimal_places (int): Number of decimals used in this currency.. [optional]  # noqa: E501
            currency_id (str, none_type): Currency ID. Default is the source account's currency, or the user's default currency. Can be used instead of currency_code.. [optional]  # noqa: E501
            currency_name (str): [optional]  # noqa: E501
            currency_symbol (str): [optional]  # noqa: E501
            date (datetime): Date of the transaction. [optional]  # noqa: E501
            description (str): Description of the transaction.. [optional]  # noqa: E501
            destination_iban (str, none_type): [optional]  # noqa: E501
            destination_id (str, none_type): ID of the destination account. For a deposit or a transfer, this must always be an asset account. For withdrawals this must be an expense account.. [optional]  # noqa: E501
            destination_name (str, none_type): Name of the destination account. You can submit the name instead of the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is enough.. [optional]  # noqa: E501
            due_date (datetime, none_type): [optional]  # noqa: E501
            external_id (str, none_type): Reference to external ID in other systems.. [optional]  # noqa: E501
            external_url (str, none_type): External, custom URL for this transaction.. [optional]  # noqa: E501
            foreign_amount (str, none_type): The amount in a foreign currency.. [optional]  # noqa: E501
            foreign_currency_code (str, none_type): Currency code of the foreign currency. Default is NULL. Can be used instead of the foreign_currency_id, but this or the ID is required when submitting a foreign amount.. [optional]  # noqa: E501
            foreign_currency_decimal_places (int, none_type): Number of decimals in the currency. [optional]  # noqa: E501
            foreign_currency_id (str, none_type): Currency ID of the foreign currency. Default is null. Is required when you submit a foreign amount.. [optional]  # noqa: E501
            foreign_currency_symbol (str, none_type): [optional]  # noqa: E501
            interest_date (datetime, none_type): [optional]  # noqa: E501
            internal_reference (str, none_type): Reference to internal reference of other systems.. [optional]  # noqa: E501
            invoice_date (datetime, none_type): [optional]  # noqa: E501
            notes (str, none_type): [optional]  # noqa: E501
            order (int, none_type): Order of this entry in the list of transactions.. [optional]  # noqa: E501
            payment_date (datetime, none_type): [optional]  # noqa: E501
            process_date (datetime, none_type): [optional]  # noqa: E501
            reconciled (bool): If the transaction has been reconciled already. When you set this, the amount can no longer be edited by the user.. [optional]  # noqa: E501
            sepa_batch_id (str, none_type): SEPA Batch ID. [optional]  # noqa: E501
            sepa_cc (str, none_type): SEPA Clearing Code. [optional]  # noqa: E501
            sepa_ci (str, none_type): SEPA Creditor Identifier. [optional]  # noqa: E501
            sepa_country (str, none_type): SEPA Country. [optional]  # noqa: E501
            sepa_ct_id (str, none_type): SEPA end-to-end Identifier. [optional]  # noqa: E501
            sepa_ct_op (str, none_type): SEPA Opposing Account Identifier. [optional]  # noqa: E501
            sepa_db (str, none_type): SEPA mandate identifier. [optional]  # noqa: E501
            sepa_ep (str, none_type): SEPA External Purpose indicator. [optional]  # noqa: E501
            source_iban (str, none_type): [optional]  # noqa: E501
            source_id (str, none_type): ID of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account.. [optional]  # noqa: E501
            source_name (str, none_type): Name of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id. If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on the name.. [optional]  # noqa: E501
            tags ([str], none_type): Array of tags.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
