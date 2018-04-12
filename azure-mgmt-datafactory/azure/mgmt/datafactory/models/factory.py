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

from .resource import Resource


class Factory(Resource):
    """Factory resource type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param identity: Managed service identity of the factory.
    :type identity: ~azure.mgmt.datafactory.models.FactoryIdentity
    :ivar provisioning_state: Factory provisioning state, example Succeeded.
    :vartype provisioning_state: str
    :ivar create_time: Time the factory was created in ISO8601 format.
    :vartype create_time: datetime
    :ivar version: Version of the factory.
    :vartype version: str
    :param vsts_configuration: VSTS repo information of the factory.
    :type vsts_configuration:
     ~azure.mgmt.datafactory.models.FactoryVSTSConfiguration
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'create_time': {'readonly': True},
        'version': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'identity': {'key': 'identity', 'type': 'FactoryIdentity'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'create_time': {'key': 'properties.createTime', 'type': 'iso-8601'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'vsts_configuration': {'key': 'properties.vstsConfiguration', 'type': 'FactoryVSTSConfiguration'},
    }

    def __init__(self, **kwargs):
        super(Factory, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.identity = kwargs.get('identity', None)
        self.provisioning_state = None
        self.create_time = None
        self.version = None
        self.vsts_configuration = kwargs.get('vsts_configuration', None)
