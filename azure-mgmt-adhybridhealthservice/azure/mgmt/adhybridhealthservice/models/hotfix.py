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


class Hotfix(Model):
    """The details of the hotfix installed in the server.

    :param kb_name: The name of the hotfix KB.
    :type kb_name: str
    :param link: The link to the KB Article.
    :type link: str
    :param installed_date: The date and time, in UTC, when the KB was
     installed in the server.
    :type installed_date: datetime
    """

    _attribute_map = {
        'kb_name': {'key': 'kbName', 'type': 'str'},
        'link': {'key': 'link', 'type': 'str'},
        'installed_date': {'key': 'installedDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(Hotfix, self).__init__(**kwargs)
        self.kb_name = kwargs.get('kb_name', None)
        self.link = kwargs.get('link', None)
        self.installed_date = kwargs.get('installed_date', None)