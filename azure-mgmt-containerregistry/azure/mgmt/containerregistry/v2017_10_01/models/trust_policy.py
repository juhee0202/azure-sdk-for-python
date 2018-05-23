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


class TrustPolicy(Model):
    """An object that represents content trust policy for a container registry.

    :param type: The type of trust policy. Possible values include: 'Notary'
    :type type: str or
     ~azure.mgmt.containerregistry.v2017_10_01.models.TrustPolicyType
    :param status: The value that indicates whether the policy is enabled or
     not. Possible values include: 'enabled', 'disabled'
    :type status: str or
     ~azure.mgmt.containerregistry.v2017_10_01.models.PolicyStatus
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TrustPolicy, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.status = kwargs.get('status', None)
