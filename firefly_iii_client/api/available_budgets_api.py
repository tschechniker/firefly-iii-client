"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from firefly_iii_client.api_client import ApiClient, Endpoint as _Endpoint
from firefly_iii_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from firefly_iii_client.model.available_budget_array import AvailableBudgetArray
from firefly_iii_client.model.available_budget_single import AvailableBudgetSingle
from firefly_iii_client.model.available_budget_store import AvailableBudgetStore
from firefly_iii_client.model.available_budget_update import AvailableBudgetUpdate
from firefly_iii_client.model.validation_error import ValidationError


class AvailableBudgetsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_available_budget_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/available_budgets/{id}',
                'operation_id': 'delete_available_budget',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_available_budget_endpoint = _Endpoint(
            settings={
                'response_type': (AvailableBudgetSingle,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/available_budgets/{id}',
                'operation_id': 'get_available_budget',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_available_budget_endpoint = _Endpoint(
            settings={
                'response_type': (AvailableBudgetArray,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/available_budgets',
                'operation_id': 'list_available_budget',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'start',
                    'end',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'start':
                        (date,),
                    'end':
                        (date,),
                },
                'attribute_map': {
                    'page': 'page',
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'page': 'query',
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.store_available_budget_endpoint = _Endpoint(
            settings={
                'response_type': (AvailableBudgetSingle,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/available_budgets',
                'operation_id': 'store_available_budget',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'available_budget_store',
                ],
                'required': [
                    'available_budget_store',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'available_budget_store':
                        (AvailableBudgetStore,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'available_budget_store': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json',
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )
        self.update_available_budget_endpoint = _Endpoint(
            settings={
                'response_type': (AvailableBudgetSingle,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/available_budgets/{id}',
                'operation_id': 'update_available_budget',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'available_budget_update',
                ],
                'required': [
                    'id',
                    'available_budget_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'available_budget_update':
                        (AvailableBudgetUpdate,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'available_budget_update': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json',
                    'application/json'
                ],
                'content_type': [
                    'application/vnd.api+json',
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )

    def delete_available_budget(
        self,
        id,
        **kwargs
    ):
        """Delete an available budget.  # noqa: E501

        Delete an available budget. Not much more to say.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_available_budget(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The ID of the available budget.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.delete_available_budget_endpoint.call_with_http_info(**kwargs)

    def get_available_budget(
        self,
        id,
        **kwargs
    ):
        """Get a single available budget.  # noqa: E501

        Get a single available budget, by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_available_budget(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The ID of the available budget.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AvailableBudgetSingle
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.get_available_budget_endpoint.call_with_http_info(**kwargs)

    def list_available_budget(
        self,
        **kwargs
    ):
        """List all available budget amounts.  # noqa: E501

        Firefly III allows users to set the amount that is available to be budgeted in so-called \"available budgets\". For example, the user could have 1200,- available to be divided during the coming month. This amount is used on the /budgets page. This endpoint returns all of these amounts and the periods for which they are set.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_available_budget(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number. The default pagination is 50.. [optional]
            start (date): A date formatted YYYY-MM-DD. . [optional]
            end (date): A date formatted YYYY-MM-DD. . [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AvailableBudgetArray
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_available_budget_endpoint.call_with_http_info(**kwargs)

    def store_available_budget(
        self,
        available_budget_store,
        **kwargs
    ):
        """Store a new available budget  # noqa: E501

        Creates a new available budget for a specified period. The data required can be submitted as a JSON body or as a list of parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.store_available_budget(available_budget_store, async_req=True)
        >>> result = thread.get()

        Args:
            available_budget_store (AvailableBudgetStore): JSON array or key=value pairs with the necessary available budget information. See the model for the exact specifications.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AvailableBudgetSingle
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['available_budget_store'] = \
            available_budget_store
        return self.store_available_budget_endpoint.call_with_http_info(**kwargs)

    def update_available_budget(
        self,
        id,
        available_budget_update,
        **kwargs
    ):
        """Update existing available budget, to change for example the date range of the amount or the amount itself.  # noqa: E501

        Update existing available budget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_available_budget(id, available_budget_update, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The ID of the object.X
            available_budget_update (AvailableBudgetUpdate): JSON array or form value with updated available budget information. See the model for the exact specifications.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AvailableBudgetSingle
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        kwargs['available_budget_update'] = \
            available_budget_update
        return self.update_available_budget_endpoint.call_with_http_info(**kwargs)

