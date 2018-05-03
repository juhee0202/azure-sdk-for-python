# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServiceMember(Model):
    """The details of the server for a given onboarded service.

    :param continuation_token: The page-continuation token to use with a paged
     version of this API.
    :type continuation_token: str
    :param total_count: The total number of servers onboarded for a given
     service.
    :type total_count: int
    :param next_link: The link used to get the next page of the operation.
    :type next_link: str
    :param value: The server properties.
    :type value:
     list[~azure.mgmt.adhybridhealthservice.models.ServiceMemberProperties]
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'total_count': {'key': 'totalCount', 'type': 'int'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[ServiceMemberProperties]'},
    }

    def __init__(self, **kwargs):
        super(ServiceMember, self).__init__(**kwargs)
        self.continuation_token = kwargs.get('continuation_token', None)
        self.total_count = kwargs.get('total_count', None)
        self.next_link = kwargs.get('next_link', None)
        self.value = kwargs.get('value', None)