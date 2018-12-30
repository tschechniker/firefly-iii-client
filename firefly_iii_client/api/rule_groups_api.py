# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from firefly_iii_client.api_client import ApiClient


class RuleGroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_rule_group(self, id, **kwargs):  # noqa: E501
        """Delete a rule group.  # noqa: E501

        Delete a rule group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_rule_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_rule_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_rule_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_rule_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a rule group.  # noqa: E501

        Delete a rule group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_rule_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_rule_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_rule_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/rule_groups/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fire_rule_group(self, id, **kwargs):  # noqa: E501
        """Fire the rule group on your transactions.  # noqa: E501

        Fire the rule group on your transactions. Changes will be made by the rules in the rule group! Limit the result if you want to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fire_rule_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :param date start: A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present. 
        :param date end: A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present. 
        :param str accounts: Limit the testing of the rule group to these asset accounts. Only asset accounts will be accepted. Other types will be silently dropped. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fire_rule_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.fire_rule_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def fire_rule_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Fire the rule group on your transactions.  # noqa: E501

        Fire the rule group on your transactions. Changes will be made by the rules in the rule group! Limit the result if you want to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fire_rule_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :param date start: A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present. 
        :param date end: A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present. 
        :param str accounts: Limit the testing of the rule group to these asset accounts. Only asset accounts will be accepted. Other types will be silently dropped. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'start', 'end', 'accounts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fire_rule_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `fire_rule_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'accounts' in local_var_params:
            query_params.append(('accounts', local_var_params['accounts']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/rule_groups/{id}/trigger', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_rule_group(self, id, **kwargs):  # noqa: E501
        """Get a single rule group.  # noqa: E501

        Get a single rule group. This does not include the rules. For that, see below.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rule_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :return: RuleGroupSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rule_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rule_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_rule_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a single rule group.  # noqa: E501

        Get a single rule group. This does not include the rules. For that, see below.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rule_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :return: RuleGroupSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rule_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_rule_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/rule_groups/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RuleGroupSingle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_rule_groups(self, **kwargs):  # noqa: E501
        """List all rule groups.  # noqa: E501

        List all rule groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rule_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number. The default pagination is 50
        :return: RuleGroupArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rule_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_rule_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_rule_groups_with_http_info(self, **kwargs):  # noqa: E501
        """List all rule groups.  # noqa: E501

        List all rule groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rule_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number. The default pagination is 50
        :return: RuleGroupArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rule_groups" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/rule_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RuleGroupArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_rules_by_group(self, id, **kwargs):  # noqa: E501
        """List rules in this rule group.  # noqa: E501

        List rules in this rule group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rules_by_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :param int page: Page number. The default pagination is 50.
        :return: RuleArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rules_by_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rules_by_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_rules_by_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """List rules in this rule group.  # noqa: E501

        List rules in this rule group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rules_by_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :param int page: Page number. The default pagination is 50.
        :return: RuleArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rules_by_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_rules_by_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/rule_groups/{id}/rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RuleArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def store_rule_group(self, rule_group_update, **kwargs):  # noqa: E501
        """Store a new rule group.  # noqa: E501

        Creates a new rule group. The data required can be submitted as a JSON body or as a list of parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_rule_group(rule_group_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RuleGroupUpdate rule_group_update: JSON array or key=value pairs with the necessary rule group information. See the model for the exact specifications. (required)
        :return: RuleGroupSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.store_rule_group_with_http_info(rule_group_update, **kwargs)  # noqa: E501
        else:
            (data) = self.store_rule_group_with_http_info(rule_group_update, **kwargs)  # noqa: E501
            return data

    def store_rule_group_with_http_info(self, rule_group_update, **kwargs):  # noqa: E501
        """Store a new rule group.  # noqa: E501

        Creates a new rule group. The data required can be submitted as a JSON body or as a list of parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_rule_group_with_http_info(rule_group_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RuleGroupUpdate rule_group_update: JSON array or key=value pairs with the necessary rule group information. See the model for the exact specifications. (required)
        :return: RuleGroupSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['rule_group_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method store_rule_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rule_group_update' is set
        if ('rule_group_update' not in local_var_params or
                local_var_params['rule_group_update'] is None):
            raise ValueError("Missing the required parameter `rule_group_update` when calling `store_rule_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule_group_update' in local_var_params:
            body_params = local_var_params['rule_group_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/rule_groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RuleGroupSingle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def test_rule_group(self, id, **kwargs):  # noqa: E501
        """Test which transactions would be hit by the rule group. No changes will be made.  # noqa: E501

        Test which transactions would be hit by the rule group. No changes will be made. Limit the result if you want to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_rule_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :param int page: Page number. The default pagination is 50 items.
        :param str start: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present. 
        :param str end: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present. 
        :param int search_limit: Maximum number of transactions Firefly III will try. Don't set this too high, or it will take Firefly III very long to run the test. I suggest a max of 200. 
        :param int triggered_limit: Maximum number of transactions the rule group can actually trigger on, before Firefly III stops. I would suggest setting this to 10 or 15. Don't go above the user's page size, because browsing to page 2 or 3 of a test result would fire the test again, making any navigation efforts very slow. 
        :param str accounts: Limit the testing of the rule group to these asset accounts. Only asset accounts will be accepted. Other types will be silently dropped. 
        :return: TransactionArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.test_rule_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.test_rule_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def test_rule_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Test which transactions would be hit by the rule group. No changes will be made.  # noqa: E501

        Test which transactions would be hit by the rule group. No changes will be made. Limit the result if you want to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_rule_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :param int page: Page number. The default pagination is 50 items.
        :param str start: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present. 
        :param str end: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present. 
        :param int search_limit: Maximum number of transactions Firefly III will try. Don't set this too high, or it will take Firefly III very long to run the test. I suggest a max of 200. 
        :param int triggered_limit: Maximum number of transactions the rule group can actually trigger on, before Firefly III stops. I would suggest setting this to 10 or 15. Don't go above the user's page size, because browsing to page 2 or 3 of a test result would fire the test again, making any navigation efforts very slow. 
        :param str accounts: Limit the testing of the rule group to these asset accounts. Only asset accounts will be accepted. Other types will be silently dropped. 
        :return: TransactionArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'page', 'start', 'end', 'search_limit', 'triggered_limit', 'accounts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_rule_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `test_rule_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'search_limit' in local_var_params:
            query_params.append(('search_limit', local_var_params['search_limit']))  # noqa: E501
        if 'triggered_limit' in local_var_params:
            query_params.append(('triggered_limit', local_var_params['triggered_limit']))  # noqa: E501
        if 'accounts' in local_var_params:
            query_params.append(('accounts', local_var_params['accounts']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/rule_groups/{id}/test', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_rule_group(self, id, rule_group_update, **kwargs):  # noqa: E501
        """Update existing rule group.  # noqa: E501

        Update existing rule group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_rule_group(id, rule_group_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :param RuleGroupUpdate rule_group_update: JSON array with updated rule group information. See the model for the exact specifications. (required)
        :return: RuleGroupSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_rule_group_with_http_info(id, rule_group_update, **kwargs)  # noqa: E501
        else:
            (data) = self.update_rule_group_with_http_info(id, rule_group_update, **kwargs)  # noqa: E501
            return data

    def update_rule_group_with_http_info(self, id, rule_group_update, **kwargs):  # noqa: E501
        """Update existing rule group.  # noqa: E501

        Update existing rule group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_rule_group_with_http_info(id, rule_group_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the rule group. (required)
        :param RuleGroupUpdate rule_group_update: JSON array with updated rule group information. See the model for the exact specifications. (required)
        :return: RuleGroupSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'rule_group_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_rule_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_rule_group`")  # noqa: E501
        # verify the required parameter 'rule_group_update' is set
        if ('rule_group_update' not in local_var_params or
                local_var_params['rule_group_update'] is None):
            raise ValueError("Missing the required parameter `rule_group_update` when calling `update_rule_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule_group_update' in local_var_params:
            body_params = local_var_params['rule_group_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/rule_groups/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RuleGroupSingle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
