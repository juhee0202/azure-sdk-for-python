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


class IntegrationAccountMapFilter(Model):
    """The integration account map filter for odata query.

    All required parameters must be populated in order to send to Azure.

    :param map_type: Required. The map type of integration account map.
     Possible values include: 'NotSpecified', 'Xslt', 'Xslt20', 'Xslt30',
     'Liquid'
    :type map_type: str or ~azure.mgmt.logic.models.MapType
    """

    _validation = {
        'map_type': {'required': True},
    }

    _attribute_map = {
        'map_type': {'key': 'mapType', 'type': 'MapType'},
    }

    def __init__(self, *, map_type, **kwargs) -> None:
        super(IntegrationAccountMapFilter, self).__init__(**kwargs)
        self.map_type = map_type
