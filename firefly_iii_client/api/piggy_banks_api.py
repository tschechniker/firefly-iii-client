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
from firefly_iii_client.model.attachment_array import AttachmentArray
from firefly_iii_client.model.piggy_bank_array import PiggyBankArray
from firefly_iii_client.model.piggy_bank_event_array import PiggyBankEventArray
from firefly_iii_client.model.piggy_bank_single import PiggyBankSingle
from firefly_iii_client.model.piggy_bank_store import PiggyBankStore
from firefly_iii_client.model.piggy_bank_update import PiggyBankUpdate
from firefly_iii_client.model.validation_error import ValidationError


class PiggyBanksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_piggy_bank_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/piggy_banks/{id}',
                'operation_id': 'delete_piggy_bank',
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
        self.get_piggy_bank_endpoint = _Endpoint(
            settings={
                'response_type': (PiggyBankSingle,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/piggy_banks/{id}',
                'operation_id': 'get_piggy_bank',
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
        self.list_attachment_by_piggy_bank_endpoint = _Endpoint(
            settings={
                'response_type': (AttachmentArray,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/piggy_banks/{id}/attachments',
                'operation_id': 'list_attachment_by_piggy_bank',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'page',
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
                    'page':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'page': 'page',
                },
                'location_map': {
                    'id': 'path',
                    'page': 'query',
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
        self.list_event_by_piggy_bank_endpoint = _Endpoint(
            settings={
                'response_type': (PiggyBankEventArray,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/piggy_banks/{id}/events',
                'operation_id': 'list_event_by_piggy_bank',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'page',
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
                    'page':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'page': 'page',
                },
                'location_map': {
                    'id': 'path',
                    'page': 'query',
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
        self.list_piggy_bank_endpoint = _Endpoint(
            settings={
                'response_type': (PiggyBankArray,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/piggy_banks',
                'operation_id': 'list_piggy_bank',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
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
                },
                'attribute_map': {
                    'page': 'page',
                },
                'location_map': {
                    'page': 'query',
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
        self.store_piggy_bank_endpoint = _Endpoint(
            settings={
                'response_type': (PiggyBankSingle,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/piggy_banks',
                'operation_id': 'store_piggy_bank',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'piggy_bank_store',
                ],
                'required': [
                    'piggy_bank_store',
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
                    'piggy_bank_store':
                        (PiggyBankStore,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'piggy_bank_store': 'body',
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
        self.update_piggy_bank_endpoint = _Endpoint(
            settings={
                'response_type': (PiggyBankSingle,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/piggy_banks/{id}',
                'operation_id': 'update_piggy_bank',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'piggy_bank_update',
                ],
                'required': [
                    'id',
                    'piggy_bank_update',
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
                    'piggy_bank_update':
                        (PiggyBankUpdate,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'piggy_bank_update': 'body',
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

    def delete_piggy_bank(
        self,
        id,
        **kwargs
    ):
        """Delete a piggy bank.  # noqa: E501

        Delete a piggy bank.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_piggy_bank(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The ID of the piggy bank.

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
        return self.delete_piggy_bank_endpoint.call_with_http_info(**kwargs)

    def get_piggy_bank(
        self,
        id,
        **kwargs
    ):
        """Get a single piggy bank.  # noqa: E501

        Get a single piggy bank.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_piggy_bank(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The ID of the piggy bank.

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
            PiggyBankSingle
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
        return self.get_piggy_bank_endpoint.call_with_http_info(**kwargs)

    def list_attachment_by_piggy_bank(
        self,
        id,
        **kwargs
    ):
        """Lists all attachments.  # noqa: E501

        Lists all attachments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_attachment_by_piggy_bank(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The ID of the piggy bank.

        Keyword Args:
            page (int): Page number. The default pagination is 50.. [optional]
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
            AttachmentArray
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
        return self.list_attachment_by_piggy_bank_endpoint.call_with_http_info(**kwargs)

    def list_event_by_piggy_bank(
        self,
        id,
        **kwargs
    ):
        """List all events linked to a piggy bank.  # noqa: E501

        List all events linked to a piggy bank (adding and removing money).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_event_by_piggy_bank(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The ID of the piggy bank

        Keyword Args:
            page (int): Page number. The default pagination is 50.. [optional]
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
            PiggyBankEventArray
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
        return self.list_event_by_piggy_bank_endpoint.call_with_http_info(**kwargs)

    def list_piggy_bank(
        self,
        **kwargs
    ):
        """List all piggy banks.  # noqa: E501

        List all piggy banks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_piggy_bank(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number. The default pagination is 50.. [optional]
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
            PiggyBankArray
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
        return self.list_piggy_bank_endpoint.call_with_http_info(**kwargs)

    def store_piggy_bank(
        self,
        piggy_bank_store,
        **kwargs
    ):
        """Store a new piggy bank  # noqa: E501

        Creates a new piggy bank. The data required can be submitted as a JSON body or as a list of parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.store_piggy_bank(piggy_bank_store, async_req=True)
        >>> result = thread.get()

        Args:
            piggy_bank_store (PiggyBankStore): JSON array or key=value pairs with the necessary piggy bank information. See the model for the exact specifications.

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
            PiggyBankSingle
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
        kwargs['piggy_bank_store'] = \
            piggy_bank_store
        return self.store_piggy_bank_endpoint.call_with_http_info(**kwargs)

    def update_piggy_bank(
        self,
        id,
        piggy_bank_update,
        **kwargs
    ):
        """Update existing piggy bank.  # noqa: E501

        Update existing piggy bank.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_piggy_bank(id, piggy_bank_update, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The ID of the piggy bank
            piggy_bank_update (PiggyBankUpdate): JSON array with updated piggy bank information. See the model for the exact specifications.

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
            PiggyBankSingle
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
        kwargs['piggy_bank_update'] = \
            piggy_bank_update
        return self.update_piggy_bank_endpoint.call_with_http_info(**kwargs)

