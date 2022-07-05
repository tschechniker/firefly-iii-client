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
from firefly_iii_client.model.chart_line import ChartLine


class ChartsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_chart_account_overview_endpoint = _Endpoint(
            settings={
                'response_type': (ChartLine,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/chart/account/overview',
                'operation_id': 'get_chart_account_overview',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'start',
                    'end',
                ],
                'required': [
                    'start',
                    'end',
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
                    'start':
                        (date,),
                    'end':
                        (date,),
                },
                'attribute_map': {
                    'start': 'start',
                    'end': 'end',
                },
                'location_map': {
                    'start': 'query',
                    'end': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_chart_account_overview(
        self,
        start,
        end,
        **kwargs
    ):
        """Dashboard chart with asset account balance information.  # noqa: E501

        This endpoint returns the data required to generate a chart with basic asset account balance information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_chart_account_overview(start, end, async_req=True)
        >>> result = thread.get()

        Args:
            start (date): A date formatted YYYY-MM-DD. 
            end (date): A date formatted YYYY-MM-DD. 

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
            ChartLine
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
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        return self.get_chart_account_overview_endpoint.call_with_http_info(**kwargs)

