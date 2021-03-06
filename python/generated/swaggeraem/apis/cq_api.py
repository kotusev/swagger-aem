# coding: utf-8

"""
    Adobe Experience Manager (AEM) API

    Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API

    OpenAPI spec version: 1.1.1
    Contact: opensource@shinesolutions.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CqApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def post_cq_actions(self, authorizable_id, changelog, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_cq_actions(authorizable_id, changelog, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorizable_id:  (required)
        :param str changelog:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_cq_actions_with_http_info(authorizable_id, changelog, **kwargs)
        else:
            (data) = self.post_cq_actions_with_http_info(authorizable_id, changelog, **kwargs)
            return data

    def post_cq_actions_with_http_info(self, authorizable_id, changelog, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_cq_actions_with_http_info(authorizable_id, changelog, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorizable_id:  (required)
        :param str changelog:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorizable_id', 'changelog']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_cq_actions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorizable_id' is set
        if ('authorizable_id' not in params) or (params['authorizable_id'] is None):
            raise ValueError("Missing the required parameter `authorizable_id` when calling `post_cq_actions`")
        # verify the required parameter 'changelog' is set
        if ('changelog' not in params) or (params['changelog'] is None):
            raise ValueError("Missing the required parameter `changelog` when calling `post_cq_actions`")


        collection_formats = {}

        resource_path = '/.cqactions.html'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'authorizable_id' in params:
            query_params['authorizableId'] = params['authorizable_id']
        if 'changelog' in params:
            query_params['changelog'] = params['changelog']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['aemAuth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)
